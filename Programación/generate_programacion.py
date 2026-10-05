# -*- coding: utf-8 -*-
"""
Generador integral de la Programación Didáctica para Sostenibilidad aplicada al sistema productivo (1708)
Ciclos: DAW y DAM (Andalucía)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def build_programacion():
    doc = docx.Document()
    
    # Page setup - Margins (Normal 2.5 cm = ~0.98 inches)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.9)
        section.bottom_margin = Inches(0.9)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        
    # Styles config
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
    
    # Helper functions
    def set_cell_background(cell, fill_hex):
        tcPr = cell._element.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
        tcPr = cell._element.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="D1D5DB", sz="4", val="single"):
        tblPr = table._element.xpath('w:tblPr')
        if tblPr:
            borders = parse_xml(
                f'<w:tblBorders {nsdecls("w")}>'
                f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:left w:val="none"/>'
                f'<w:right w:val="none"/>'
                f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                f'<w:insideV w:val="none"/>'
                f'</w:tblBorders>'
            )
            tblPr[0].append(borders)

    def add_callout(text_list, title="MARCO DESTACADO", bg_hex="F0FDF4", border_hex="16A34A", text_color=(0x16, 0x65, 0x34)):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        table.columns[0].width = Inches(6.7)
        
        cell = table.cell(0, 0)
        set_cell_background(cell, bg_hex)
        set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
        
        tcPr = cell._element.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>'
            f'<w:top w:val="none"/>'
            f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/>'
            f'<w:bottom w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run_title = p.add_run(f"📌 {title}\n")
        run_title.bold = True
        run_title.font.name = "Calibri"
        run_title.font.size = Pt(10)
        run_title.font.color.rgb = RGBColor(*text_color)
        
        for idx, line in enumerate(text_list):
            if idx > 0:
                p = cell.add_paragraph()
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.line_spacing = 1.15
            r = p.add_run(line)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(2)
        p_after.paragraph_format.space_after = Pt(4)

    def heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(14.5)
        r.bold = True
        r.font.color.rgb = RGBColor(0x0F, 0x4C, 0x81) # Deep Blue
        return p

    def heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(12)
        r.bold = True
        r.font.color.rgb = RGBColor(0x04, 0x78, 0x57) # Forest Green
        return p

    def heading_3(text):
        p = doc.add_paragraph()
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10.5)
        r.bold = True
        r.font.color.rgb = RGBColor(0x37, 0x41, 0x51) # Slate Gray
        return p

    def body_p(text, bold_prefix=None, space_after=4):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        return p

    def bullet_p(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.bold = True
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(10)
            r_pre.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
        return p

    def styled_table(headers, data, col_widths=None, header_bg="0F4C81", header_fg=(0xFF, 0xFF, 0xFF)):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        
        # Header
        hdr_cells = table.rows[0].cells
        for i, title in enumerate(headers):
            hdr_cells[i].text = title
            set_cell_background(hdr_cells[i], header_bg)
            set_cell_margins(hdr_cells[i], top=120, bottom=120, left=140, right=140)
            p = hdr_cells[i].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            for run in p.runs:
                run.font.name = "Calibri"
                run.font.size = Pt(9.5)
                run.font.bold = True
                run.font.color.rgb = RGBColor(*header_fg)
                
        # Data rows
        for row_idx, row_data in enumerate(data):
            row_cells = table.rows[row_idx + 1].cells
            bg_color = "F9FAFB" if row_idx % 2 == 1 else "FFFFFF"
            for col_idx, cell_value in enumerate(row_data):
                row_cells[col_idx].text = str(cell_value)
                set_cell_background(row_cells[col_idx], bg_color)
                set_cell_margins(row_cells[col_idx], top=100, bottom=100, left=140, right=140)
                p = row_cells[col_idx].paragraphs[0]
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.1
                for run in p.runs:
                    run.font.name = "Calibri"
                    run.font.size = Pt(9)
                    run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
                    
        # Column widths
        if col_widths:
            for i, col in enumerate(table.columns):
                w = Inches(col_widths[i])
                for cell in col.cells:
                    cell.width = w
                    
        set_table_borders(table)
        
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(2)
        p_after.paragraph_format.space_after = Pt(4)
        return table

    # -------------------------------------------------------------
    # PORTADA Y ENCABEZADO
    # -------------------------------------------------------------
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(24)
    p_title.paragraph_format.space_after = Pt(4)
    p_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_title.add_run("PROGRAMACIÓN DIDÁCTICA")
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = RGBColor(0x0F, 0x4C, 0x81)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(8)
    p_sub.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Módulo Profesional: Sostenibilidad Aplicada al Sistema Productivo (Código 1708)")
    r_sub.bold = True
    r_sub.font.size = Pt(13)
    r_sub.font.color.rgb = RGBColor(0x04, 0x78, 0x57)

    p_cycles = doc.add_paragraph()
    p_cycles.paragraph_format.space_before = Pt(0)
    p_cycles.paragraph_format.space_after = Pt(16)
    p_cycles.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_c = p_cycles.add_run("Ciclos Formativos de Grado Superior:\n• Desarrollo de Aplicaciones Web (DAW)\n• Desarrollo de Aplicaciones Multiplataforma (DAM)\nFamilia Profesional: Informática y Comunicaciones\nComunidad Autónoma de Andalucía · Curso 2025 / 2026")
    r_c.font.size = Pt(11)
    r_c.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    # Tabla Ficha Técnica del Módulo
    info_headers = ["Elemento", "Especificación y Datos del Módulo"]
    info_data = [
        ["Denominación oficial", "Sostenibilidad aplicada al sistema productivo"],
        ["Código oficial del módulo", "1708 (Real Decreto 659/2023 y Real Decreto 500/2024)"],
        ["Ciclos formativos de aplicación", "1º curso de Técnico Superior en DAW y 1º curso de Técnico Superior en DAM"],
        ["Carga horaria total", "30 horas lectivas presenciales (1 hora semanal a lo largo del curso académico)"],
        ["Equivalencia crediticia", "3 créditos ECTS (Grado Superior)"],
        ["Régimen de impartición", "Formación Profesional Grado D - Régimen Dual General (incorporando estancia en empresa)"],
        ["Departamento didáctico", "Departamento de Informática y Comunicaciones"],
        ["Repositorio y Materiales de aula", "Carpeta digital del módulo: apuntes (01-10), prácticas y casos reales en docs/"]
    ]
    styled_table(info_headers, info_data, col_widths=[2.3, 4.4], header_bg="0F4C81")

    # -------------------------------------------------------------
    # 1. INTRODUCCIÓN Y JUSTIFICACIÓN PEDAGÓGICA
    # -------------------------------------------------------------
    heading_1("1. INTRODUCCIÓN Y JUSTIFICACIÓN PEDAGÓGICA DEL MÓDULO")
    body_p("La presente Programación Didáctica organiza e instrumenta la docencia del módulo profesional de Sostenibilidad aplicada al sistema productivo (Código 1708), común a los ciclos formativos de Grado Superior de Desarrollo de Aplicaciones Web (DAW) y Desarrollo de Aplicaciones Multiplataforma (DAM), pertenecientes a la familia profesional de Informática y Comunicaciones en los centros educativos de la Comunidad Autónoma de Andalucía.")
    body_p("La promulgación de la Ley Orgánica 3/2022, de 31 de marzo, y su posterior desarrollo mediante el Real Decreto 659/2023, de 18 de julio, y el Real Decreto 500/2024, de 21 de mayo, ha transformado la arquitectura curricular de la Formación Profesional española para responder de forma contundente a los grandes vectores de transformación del tejido productivo: la digitalización y la transición ecológica justa.")
    body_p("De conformidad con el artículo 100 del Real Decreto 659/2023:")
    
    add_callout([
        "«El módulo de Sostenibilidad aplicada al sistema productivo tendrá como finalidad el desarrollo de conocimiento y competencias básicas en economía verde, sostenibilidad e impacto ambiental de la actividad, así como las condiciones en que las exigencias de la transición ecológica modifican los procesos productivos del sector correspondiente.»",
        "En el marco de la familia de Informática y Comunicaciones (DAW/DAM), el módulo adquiere una relevancia crítica ante el crecimiento exponencial del consumo energético de centros de datos, la huella de carbono del Cloud Computing, el impacto ambiental y social del entrenamiento de modelos de Inteligencia Artificial, la gestión de Residuos de Aparatos Eléctricos y Electrónicos (RAEE), y la exigencia regulatoria europea (Directiva CSRD, normas ESRS y Taxonomía Verde) de medir y reportar criterios ASG (Ambientales, Sociales y de Gobernanza)."
    ], title="Finalidad del Módulo 1708 (Art. 100 RD 659/2023)")

    body_p("La programación está estrictamente compaginada y alineada con los materiales didácticos desarrollados para el módulo en la carpeta del repositorio (unidades 01 a 10), garantizando que todo concepto teórico se aterrice directamente en el contexto tecnológico del desarrollador de software (Green Coding, optimización de algoritmos, arquitecturas web sostenibles, servitización y economía circular).")

    # -------------------------------------------------------------
    # 2. MARCO NORMATIVO VIGENTE
    # -------------------------------------------------------------
    heading_1("2. MARCO NORMATIVO VIGENTE")
    body_p("La programación didáctica se fundamenta y ajusta de manera rigurosa a la siguiente jerarquía normativa estatal, autonómica andaluza y sectorial:")

    heading_2("2.1 Normativa General del Sistema Educativo y Formación Profesional")
    bullet_p("Garantiza el derecho fundamental a la educación y la libertad de enseñanza.", "Constitución Española de 1978 (Artículo 27): ")
    bullet_p("Regula los principios y fines de la educación no universitaria, con las modificaciones sustanciales de la Ley Orgánica 3/2020 (LOMLOE) en materia de sostenibilidad, digitalización y atención a la diversidad.", "Ley Orgánica 2/2006, de 3 de mayo, de Educación (LOE / LOMLOE): ")
    bullet_p("Establece el marco legal unificado del Sistema de Formación Profesional, consolidando el carácter dual general de todas las enseñanzas de Grado D.", "Ley Orgánica 3/2022, de 31 de marzo, de ordenación e integración de la Formación Profesional: ")
    bullet_p("Regula la ordenación del Sistema de FP. En su Artículo 100 y en el Anexo VIII fija los 6 Resultados de Aprendizaje y Criterios de Evaluación del módulo 1708.", "Real Decreto 659/2023, de 18 de julio: ")
    bullet_p("Modifica los reales decretos de los títulos de FP para incorporar formalmente los módulos de Digitalización y Sostenibilidad aplicada al sistema productivo a los currículos oficiales.", "Real Decreto 500/2024, de 21 de mayo: ")
    bullet_p("Por los que se establecen, respectivamente, los títulos de Técnico Superior en DAM y DAW y se fijan sus enseñanzas mínimas, actualizados por el Real Decreto 405/2023 y el Real Decreto 500/2024.", "Reales Decretos de Título 686/2010 (DAM) y 687/2010 (DAW): ")

    heading_2("2.2 Normativa Autonómica de la Comunidad Autónoma de Andalucía")
    bullet_p("Artículos 21 y 52, garantizando la calidad, equidad y adecuación de las enseñanzas profesionales al desarrollo socioeconómico andaluz.", "Estatuto de Autonomía para Andalucía (Ley Orgánica 2/2007, de 19 de marzo): ")
    bullet_p("Marco legal educativo de la Comunidad Autónoma de Andalucía.", "Ley 17/2007, de 10 de diciembre, de Educación de Andalucía (LEA): ")
    bullet_p("Norma marco andaluza que deroga el antiguo Decreto 436/2008 y establece la ordenación de las enseñanzas de FP en Andalucía, su carácter dual y la autonomía pedagógica de los centros.", "Decreto 104/2024, de 28 de mayo: ")
    bullet_p("Regula con carácter vinculante la evaluación formativa, continua, criterial y colegiada, así como las convocatorias, certificaciones y acreditaciones en los grados D y E en Andalucía.", "Orden de 18 de septiembre de 2025: ")
    bullet_p("Desarrollan los currículos autonómicos de ambos títulos en Andalucía.", "Órdenes de 16 de junio de 2011 (Currículo de DAW y DAM en Andalucía): ")
    bullet_p("Reglamento Orgánico de los IES y normas de organización, funcionamiento y horarios del profesorado y alumnado en Andalucía.", "Decreto 327/2010, de 13 de julio, y Orden de 20 de agosto de 2010: ")

    heading_2("2.3 Normativa en Materia de Protección de Datos y Derechos Digitales")
    bullet_p("Marco de protección de las personas físicas respecto al tratamiento de sus datos personales y a la libre circulación de estos datos.", "Reglamento (UE) 2016/679 (RGPD): ")
    bullet_p("Garantiza la privacidad, ciberseguridad y los derechos digitales en entornos educativos y laborales (sustituye a la derogada LOPD 15/1999).", "Ley Orgánica 3/2018, de 5 de diciembre (LOPDGDD): ")

    heading_2("2.4 Normativa Medioambiental, de Economía Circular y Sostenibilidad Corporativa (ASG)")
    bullet_p("Directiva de información corporativa sobre sostenibilidad y estándares europeos de reporte (ESRS).", "Directiva (UE) 2022/2464 (CSRD): ")
    bullet_p("Directiva sobre diligencia debida de las empresas en materia de sostenibilidad.", "Directiva (UE) 2024/1760 (CSDDD): ")
    bullet_p("Sistema de clasificación de actividades económicas medioambientalmente sostenibles.", "Reglamento (UE) 2020/852 (Taxonomía Verde de la UE): ")
    bullet_p("Nuevo marco de diseño ecológico para productos sostenibles y neutralidad climática.", "Reglamento (UE) 2024/1781 (Ecodiseño - ESPR): ")
    bullet_p("Regulación de la gestión y valorización de residuos de aparatos eléctricos y electrónicos.", "Directiva 2012/19/UE y Real Decreto 110/2015 (RAEE): ")
    bullet_p("Regula la gestión de residuos, el impuesto al plástico de un solo uso y el principio de jerarquía de residuos.", "Ley 7/2022, de 8 de abril, de residuos y suelos contaminados para una economía circular: ")
    bullet_p("Fija los objetivos de neutralidad climática y descarbonización para 2050 en España.", "Ley 7/2021, de 20 de mayo, de cambio climático y transición energética: ")
    bullet_p("Marco autonómico andaluz para la transición ecológica, la circularidad y la eficiencia en el uso de recursos.", "Ley 3/2023, de 30 de marzo, de Economía Circular de Andalucía (LECA): ")
    bullet_p("Marco autonómico de acción climática, mitigación y adaptación energética en Andalucía.", "Ley 8/2018, de 8 de octubre, de medidas frente al cambio climático en Andalucía: ")
    bullet_p("Marco universal de 17 Objetivos de Desarrollo Sostenible para erradicar la pobreza y proteger el planeta.", "Resolución 70/1 de la Asamblea General de la ONU (Agenda 2030): ")

    # -------------------------------------------------------------
    # 3. ENTORNO PROFESIONAL Y CONTEXTO DEL GRUPO
    # -------------------------------------------------------------
    heading_1("3. ENTORNO PROFESIONAL Y CONTEXTUALIZACIÓN DEL AULA")
    body_p("Los Técnicos Superiores en Desarrollo de Aplicaciones Web (DAW) y Desarrollo de Aplicaciones Multiplataforma (DAM) desempeñan su actividad en empresas de consultoría tecnológica, factorías de software, departamentos de TI corporativos, agencias digitales y empresas del sector público y privado.")
    body_p("En el contexto actual, el perfil del programador no solo requiere destreza técnica en lenguajes como Java, Python, JavaScript/TypeScript o SQL, sino una sólida competencia para diseñar aplicaciones eficientes, con bajo consumo de CPU/memoria y optimización de transferencias de red (Green Coding), utilizar servicios Cloud con certificación de energía renovable, garantizar la protección de datos por diseño y cumplir con los requisitos de sostenibilidad corporativa exigidos por los clientes e inversores.")

    heading_2("3.1 Contexto del Grupo de Alumnado (1º DAW / DAM)")
    body_p("El grupo de 1º curso está integrado por 22 alumnos/as procedentes de diversos municipios del entorno comarcal (Martos, Torredelcampo, Torredonjimeno, Fuensanta de Martos, Escañuela, Jaén capital). Presenta una notable heterogeneidad académica, laboral y competencial que orienta las medidas de inclusión:")
    bullet_p("El rango de edad abarca de los 18 a los 32 años. Coexisten alumnos de acceso directo desde Ciclo Formativo de Grado Medio (SMR), Bachillerato (Ciencias y Tecnología / Humanidades), prueba de acceso, y graduados universitarios (Grado en Psicología, Ciclo Superior de Sonido y Producción Mecánica).", "Perfil académico previo: ")
    bullet_p("Se identifican 7 alumnos repetidores con diversas situaciones modulares. Un alumno repetidor con solo Programación pendiente y otro con Programación y Bases de Datos. Asimismo, 2 alumnos procedentes de planes de estudio anteriores (ASIR y DAM) se incorporan para cursar los nuevos módulos de Digitalización y Sostenibilidad.", "Repetidores y adaptación: ")
    bullet_p("Dos alumnos compaginan la formación con actividad laboral activa en régimen presencial/modular, requiriendo seguimiento telemático y tutorización flexible a través del aula virtual.", "Compatibilidad laboral: ")
    bullet_p("1 alumno con Necesidades Específicas de Apoyo Educativo (NEAE) asociadas a Altas Capacidades Intelectuales (Sobredotación); 1 alumno procedente de programas de atención a la diversidad (PMAR); y 1 alumno con Necesidades Educativas Especiales (NEE) derivadas de discapacidad física motriz (incorporado al Plan de Autoprotección con evacuación asistida mediante ascensor/acompañamiento).", "Atención a la Diversidad: ")
    bullet_p("8 alumnos cuentan con acreditación oficial de idiomas (B1, B2 y C1). 10 alumnos solicitan beca general del Ministerio y 8 precisan préstamo de equipamiento informático (portátiles y almacenamiento).", "Recursos y ayudas: ")

    # -------------------------------------------------------------
    # 4. OBJETIVOS GENERALES Y COMPETENCIAS
    # -------------------------------------------------------------
    heading_1("4. OBJETIVOS GENERALES Y COMPETENCIAS")
    body_p("El módulo de Sostenibilidad aplicada al sistema productivo contribuye a la consecución de los siguientes Objetivos Generales y Competencias del título (establecidos en el RD 659/2023 y en los Reales Decretos de Título de DAW y DAM):")

    heading_2("4.1 Objetivos Generales del Ciclo Vinculados al Módulo")
    bullet_p("Describir los roles de los miembros del equipo de trabajo, identificando la responsabilidad asociada a la sostenibilidad y la gobernanza para establecer relaciones profesionales eficientes.", "a) Coordinación y roles: ")
    bullet_p("Identificar los cambios tecnológicos, normativos, organizativos y ambientales en el desarrollo de software para mantener el espíritu de innovación y mejora continua.", "b) Innovación y transición ecológica: ")
    bullet_p("Reconocer las oportunidades de negocio circular, Green IT y servitización en el mercado tecnológico para crear, gestionar o asesorar a empresas del sector.", "c) Oportunidades y modelos circulares: ")
    bullet_p("Reconocer sus derechos, deberes y código deontológico como profesional y ciudadano activo en la transición ecosocial y la gobernanza justa.", "d) Ciudadanía y ética profesional: ")

    heading_2("4.2 Competencias Profesionales, Personales y Sociales")
    bullet_p("Diseñar aplicaciones y arquitecturas de software aplicando criterios de ecodiseño, minimizando la huella de carbono digital y el consumo de recursos computacionales.", "Competencia técnica en ecodiseño: ")
    bullet_p("Evaluar y seleccionar proveedores de servicios Cloud, hardware y componentes con certificaciones ambientales y estándares ASG (ISO 14001, GRI, SASB).", "Gestión de compras y proveedores verdes: ")
    bullet_p("Analizar los aspectos ASG de una organización tecnológica y colaborar activamente en la elaboración y seguimiento de su Plan e Informe de Sostenibilidad corporativo.", "Auditoría y reporte ASG: ")
    bullet_p("Fomentar el trabajo en equipo, la equidad de género en el sector TIC, la accesibilidad digital universal y el cumplimiento ético de la privacidad y protección de datos.", "Responsabilidad social y ética digital: ")

    # -------------------------------------------------------------
    # 5. RESULTADOS DE APRENDIZAJE Y CRITERIOS DE EVALUACIÓN
    # -------------------------------------------------------------
    heading_1("5. RESULTADOS DE APRENDIZAJE Y CRITERIOS DE EVALUACIÓN (ANEXO VIII RD 659/2023)")
    body_p("Los 6 Resultados de Aprendizaje (RA) y sus correspondientes Criterios de Evaluación (CE) oficiales, con su ponderación porcentual asignada dentro de la calificación global del módulo, se detallan a continuación:")

    ra_headers = ["RA", "Resultado de Aprendizaje Oficial", "Criterios de Evaluación Oficiales (CE)", "Pond. Total"]
    ra_data = [
        [
            "RA1",
            "Identifica los aspectos ambientales, sociales y de gobernanza (ASG) relativos a la sostenibilidad teniendo en cuenta el concepto de desarrollo sostenible y los marcos internacionales que contribuyen a su consecución.",
            "a) Se ha descrito el concepto de sostenibilidad y los marcos internacionales asociados.\nb) Se han identificado los asuntos ASG que influyen en las organizaciones.\nc) Se han relacionado los ODS con la Agenda 2030.\nd) Se ha analizado la relevancia de los ASG para los grupos de interés (riesgos/oportunidades).\ne) Se han identificado los estándares de métricas (ISO, GRI, SASB, CSRD).\nf) Se ha descrito la inversión socialmente responsable (ISR) y las agencias de rating ESG.",
            "18 % (3% / CE)"
        ],
        [
            "RA2",
            "Caracteriza los retos ambientales y sociales a los que se enfrenta la sociedad, describiendo los impactos sobre las personas y los sectores productivos y proponiendo acciones para minimizarlos.",
            "a) Se han identificado los principales retos ambientales y sociales del sector TIC.\nb) Se han relacionado los retos con el desarrollo de la actividad económica y digital.\nc) Se ha analizado el impacto ambiental y social sobre personas y sectores productivos.\nd) Se han identificado medidas y acciones para minimizar los impactos.\ne) Se ha analizado la importancia de alianzas transversales (ODS 17).",
            "15 % (3% / CE)"
        ],
        [
            "RA3",
            "Establece la aplicación de criterios de sostenibilidad en el desempeño profesional y personal, identificando los elementos necesarios.",
            "a) Se han identificado los ODS más relevantes para la actividad profesional TIC.\nb) Se han analizado los riesgos y oportunidades que representan los ODS en informática.\nc) Se han identificado acciones prácticas para retos ambientales/sociales en el ámbito personal y laboral.",
            "9 % (3% / CE)"
        ],
        [
            "RA4",
            "Propone productos y servicios responsables teniendo en cuenta los principios de la economía circular.",
            "a) Se ha caracterizado el modelo de producción y consumo lineal frente al circular.\nb) Se han identificado los principios de la economía verde y circular.\nc) Se han contrastado los beneficios de la economía circular frente al modelo clásico.\nd) Se han aplicado principios de ecodiseño (hardware y software).\ne) Se ha analizado el ciclo de vida del producto (LCA/ACV).\nf) Se han identificado los procesos productivos y criterios de sostenibilidad aplicados.",
            "18 % (3% / CE)"
        ],
        [
            "RA5",
            "Realiza actividades sostenibles minimizando el impacto de las mismas en el medio ambiente.",
            "a) Se ha caracterizado el modelo de consumo actual.\nb) Se han identificado principios de economía verde/circular.\nc) Se han contrastado los beneficios del modelo circular.\nd) Se ha evaluado el impacto ambiental de actividades personales y profesionales (huella de carbono/agua).\ne) Se han aplicado principios de ecodiseño.\nf) Se han aplicado estrategias sostenibles (Green IT, eficiencia energética, cloud verde).\ng) Se ha analizado el ciclo de vida.\nh) Se han identificado procesos productivos y criterios de sostenibilidad.\ni) Se ha aplicado la normativa ambiental (RAEE, Ley 7/2022, LECA, ESPR).",
            "18 % (2% / CE)"
        ],
        [
            "RA6",
            "Analiza un plan de sostenibilidad de una empresa del sector, identificando sus grupos de interés, los aspectos ASG materiales y justificando acciones para su gestión y medición.",
            "a) Se han identificado los principales grupos de interés de la empresa TIC (stakeholders).\nb) Se han analizado los aspectos ASG materiales y la matriz de doble materialidad.\nc) Se han definido acciones de mitigación de impactos negativos y aprovechamiento de oportunidades.\nd) Se han determinado las métricas e indicadores de desempeño (GRI / ESRS / PUE / SCI).\ne) Se ha elaborado un informe formal de sostenibilidad con el plan propuesto.",
            "22 % (4,4% / CE)"
        ]
    ]
    styled_table(ra_headers, ra_data, col_widths=[0.6, 2.2, 3.2, 0.7], header_bg="0F4C81")

    # -------------------------------------------------------------
    # 6. ORGANIZACIÓN Y SECUENCIACIÓN DE UNIDADES DIDÁCTICAS
    # (COMPAGINADAS CON LOS MATERIALES DE DOCS/)
    # -------------------------------------------------------------
    heading_1("6. SECUENCIACIÓN DIDÁCTICA Y COMPAGINACIÓN CON LOS MATERIALES DEL MÓDULO")
    body_p("El módulo se estructura temporalmente en 3 Unidades de Trabajo (UT) distribuidas a lo largo de los tres trimestres del curso académico (10 horas lectivas por trimestre). Cada UT se compagina de manera unívoca con los 10 documentos de apuntes, prácticas y casos reales existentes en la carpeta docs/ del módulo:")

    # UT 1
    heading_2("6.1 TRIMESTRE 1 · Unidad de Trabajo 1: Fundamentos de Sostenibilidad, Marcos Internacionales, Aspectos ASG, Retos y Métricas en el Sector TIC (10 horas)")
    body_p("Esta unidad asienta las bases conceptuales, éticas y regulatorias de la sostenibilidad, analiza los pilares ASG y aterriza los grandes retos socioambientales en la industria del software, centros de datos y dispositivos digitales.")
    
    bullet_p("Concepto de desarrollo sostenible (Informe Brundtland 1987) y triple balance (E-S-G). Marcos globales: Cumbres de la Tierra, Río+20, Acuerdo de París (COP21) y neutralidad climática. La Agenda 2030 y los 17 ODS, identificando metas críticas en TIC (ODS 7 Energía asequible, ODS 9 Innovación/infraestructuras, ODS 12 Consumo responsable, ODS 13 Acción por el clima, ODS 5 Igualdad de género, ODS 8 Trabajo decente, ODS 10 Reducción de desigualdades, ODS 16 Paz y transparencia). Taxonomía Verde Europea (Reglamento UE 2020/852).", "Contenidos Teóricos y Normativos: ")
    bullet_p("Pilares ASG aplicados a empresas tecnológicas: Ambiental (huella de carbono, Scope 1, 2 y 3, consumo eléctrico, refrigeración por agua, residuos RAEE), Social (condiciones en extracción de minerales, privacidad de datos, ciberseguridad, ética de algoritmos de IA, brecha digital, igualdad), y Gobernanza (transparencia corporativa, comités de sostenibilidad, auditorías, código ético). Grupos de interés (stakeholders internos y externos) y Matriz de Materialidad de Mendelow. Estándares y métricas: ISO 14001, ISO 14064 (GEI), GRI Standards, SASB/ISSB, CDP, KPIs técnicos (PUE, WUE, CUE, SCI - Software Carbon Intensity). Inversión Socialmente Responsable (ISR), índices ASG y directiva CSRD (Directiva UE 2022/2464) con normas ESRS.", "Contenidos Específicos TIC: ")
    
    bullet_p("docs/01-fundamentos-sostenibilidad.md (Fundamentos, Brundtland, ODS, París, Taxonomía).", "Materiales vinculados en docs/: ")
    bullet_p("docs/02-aspectos-ASG-y-grupos-de-interes.md (Pilares ASG, stakeholders, riesgos y oportunidades).", " ")
    bullet_p("docs/03-estandares-metricas-e-inversion-responsable.md (ISO, GRI, SASB, PUE, ISR, CSRD/ESRS).", " ")
    bullet_p("docs/04-retos-ambientales-y-sociales-sector-informatico.md (Retos TIC: energía, agua, RAEE, minerales, IA, brecha digital, alianzas ODS 17).", " ")
    bullet_p("docs/09-casos-empresas-sector-informatico.md (Casos reales: HP, Microsoft, Google, Dell, Indra/Minsait, IBM, Amazon).", " ")
    bullet_p("docs/10-glosario-recursos-bibliografia.md (Glosario y fuentes oficiales).", " ")

    add_callout([
        "• Denominación: «Mapa ASG + Diagnóstico ODS en una empresa del sector informático» (docs/08-practicas-y-trabajos-sector-informatico.md §2).",
        "• Agrupamiento: Trabajo en parejas (equipos de 2 alumnos).",
        "• Desarrollo: Elección de una empresa del sector (según banco de casos de docs/09 o empresa tecnológica propuesta). Elaboración del perfil de actividad, mapeo de stakeholders, matriz de materialidad (doble materialidad ASG), diagnóstico de contribución e impacto en los ODS clave, e identificación de riesgos/oportunidades financieras y de sostenibilidad.",
        "• Entregables: Informe técnico estructurado (máx. 10 págs.) + Matriz visual ASG/ODS + Presentación oral en clase con soporte digital (10-15 min por equipo) y debate guiado.",
        "• Criterios evaluados: RA1 (a, b, c, d, e, f), RA2 (a, b, c, d, e) y RA3 (a, b, c)."
    ], title="Proyecto Integrador Trimestre 1 (T1)")

    # UT 2
    heading_2("6.2 TRIMESTRE 2 · Unidad de Trabajo 2: Economía Circular, Ecodiseño de Software/Hardware y Actividades Sostenibles en TI (10 horas)")
    body_p("Esta unidad profundiza en la transición del modelo lineal al circular, los principios del ecodiseño aplicados tanto al equipamiento físico como al desarrollo de software (Green Coding / Software Verde), la gestión de residuos y la normativa ambiental aplicable.")
    
    bullet_p("Agotamiento del modelo lineal ('extraer-fabricar-usar-tirar') en la industria digital. Principios de la economía circular (Fundación Ellen MacArthur) y las 9R (Rechazar, Rediseñar, Reducir, Reutilizar, Reparar, Restaurar, Remanufacturar, Repropósito, Reciclar, Recuperar). Modelos circulares en informática: Device-as-a-Service (DaaS), reacondicionamiento garantizado, modularidad y derecho a reparar. Análisis de Ciclo de Vida (LCA / ACV, normas ISO 14040 e ISO 14044): fases cradle-to-grave y cradle-to-cradle en servidores, portátiles y servicios cloud.", "Contenidos Teóricos y Circulares: ")
    bullet_p("Ecodiseño de Hardware (desmontabilidad, uso de plásticos reciclados, eliminación de sustancias peligrosas RoHS/REACH, eficiencia Energy Star/EPEAT). Ecodiseño de Software y Servicios Cloud (Green Software Engineering): optimización de algoritmos, reducción de complejidad computacional O(n), compresión de activos web, minimización de peticiones HTTP/API, uso de temas oscuros (Dark Mode) en pantallas OLED, selección de regiones cloud con mix eléctrico 100% renovable, destilación de modelos de IA y apagado automático de entornos no productivos. Evaluación de la huella personal y profesional del programador (teletrabajo, streaming, servidores). Compras públicas y privadas verdes (e-procurement).", "Ecodiseño y Green IT: ")
    bullet_p("Normativa ambiental y de circularidad: Directiva RAEE (2012/19/UE) y Real Decreto 110/2015 sobre residuos electrónicos; Ley 7/2022 de residuos y suelos contaminados; Reglamento europeo de Ecodiseño (UE 2024/1781 - ESPR); Ley 3/2023 de Economía Circular de Andalucía (LECA) y Ley 8/2018 de Cambio Climático de Andalucía.", "Marco Legal Aplicable: ")

    bullet_p("docs/05-economia-circular-verde-y-ecodisenio.md (Modelo lineal vs circular, LCA, checklist de ecodiseño, Green Coding).", "Materiales vinculados en docs/: ")
    bullet_p("docs/06-actividades-sostenibles-en-ti.md (Huella de carbono digital, Green IT, compras sostenibles, normativa RAEE, Ley 7/2022, LECA).", " ")
    bullet_p("docs/08-practicas-y-trabajos-sector-informatico.md (Prácticas P1-P6: cálculo de huella digital y auditoría verde de aula).", " ")

    add_callout([
        "• Denominación: «Diseño conceptual y técnico de un Producto o Servicio TIC Sostenible con Ecodiseño y Análisis de Ciclo de Vida (LCA)» (docs/08-practicas-y-trabajos-sector-informatico.md §3).",
        "• Agrupamiento: Parejas o tríos de trabajo.",
        "• Desarrollo: Diseño de una solución tecnológica responsable (ejemplos: arquitectura web optimizada para baja emisión de carbono, servicio cloud optimizado con auto-scaling y servidores de bajo consumo, plataforma de reacondicionamiento y donación de hardware escolar, sistema de sensorización IoT para eficiencia energética). Realización del Análisis de Ciclo de Vida (LCA) simplificado, checklist de ecodiseño, justificación de circularidad y cálculo de reducción estimada de huella de carbono y energía.",
        "• Entregables: Informe técnico de ecodiseño y LCA + Prototipo conceptual/técnico de la solución + Presentación oral en clase (10-12 min) con demostración del prototipo.",
        "• Criterios evaluados: RA4 (a, b, c, d, e, f) y RA5 (a, b, c, d, e, f, g, h, i)."
    ], title="Proyecto Integrador Trimestre 2 (T2)")

    # UT 3
    heading_2("6.3 TRIMESTRE 3 · Unidad de Trabajo 3: Plan de Sostenibilidad Corporativo e Informe de Rendición de Cuentas (GRI / CSRD) en TI y Formación en Empresa (10 horas)")
    body_p("Esta unidad culmina el módulo integrando todos los conocimientos adquiridos mediante la redacción de un Plan Integral de Sostenibilidad Corporativo y su correspondiente Informe de Sostenibilidad alineado a los estándares internacionales GRI y la directiva europea CSRD, conectándolo con la estancia de Formación en Empresa (Dual).")
    
    bullet_p("Estructura metodológica de un Plan de Sostenibilidad Corporativo: 1) Diagnóstico inicial de partida; 2) Mapa exhaustivo de stakeholders; 3) Matriz de doble materialidad (impacto y financiera); 4) Definición de objetivos estratégicos cuantitativos SMART a 2030; 5) Plan de acción detallado desglosado en ejes Ambiental (E), Social (S) y Gobernanza (G); 6) Asignación de recursos, presupuesto, responsables y cronograma; 7) Cuadro de mando integral de métricas y KPIs (GRI, ESRS, GHG Protocol).", "Metodología del Plan: ")
    bullet_p("Redacción del Informe de Sostenibilidad / Estado de Información No Financiera (EINF): Estructura según GRI Standards y directiva CSRD (Directiva UE 2022/2464). Comunicación transparente, prevención del Greenwashing / Bluewashing, aseguramiento de datos y rendición de cuentas ante el Consejo de Administración y la sociedad.", "Informe de Sostenibilidad: ")
    bullet_p("Desarrollo de competencias de análisis ASG en la empresa del sector TIC donde el alumnado realiza su estancia formativa dual en 1º curso (identificación de políticas de reciclaje de RAEE, uso de energía en servidores locales/cloud, condiciones laborales y accesibilidad).", "Vinculación con Formación en Empresa: ")

    bullet_p("docs/07-plan-sostenibilidad-e-informe.md (Guía paso a paso del plan, estructura GRI/CSRD, ejemplo de redacción, role-play).", "Materiales vinculados en docs/: ")
    bullet_p("docs/08-practicas-y-trabajos-sector-informatico.md §4 (Rúbricas T3, orientaciones de informe y defensa ejecutiva).", " ")
    bullet_p("docs/09-casos-empresas-sector-informatico.md y docs/10-glosario-recursos-bibliografia.md.", " ")

    add_callout([
        "• Denominación: «Plan Integral de Sostenibilidad e Informe de Rendición de Cuentas (GRI/ESRS) para una Organización del Sector Informático / Empresa Colaboradora Dual» (docs/08-practicas-y-trabajos-sector-informatico.md §4).",
        "• Agrupamiento: Grupos de 2–3 alumnos.",
        "• Desarrollo: Redacción completa de un Plan de Sostenibilidad a 3 años para una empresa u organización TIC (pudiendo tomarse como referencia la empresa de prácticas duales o una empresa del banco de casos). Incluye diagnóstico, matriz de materialidad, catálogo de acciones E/S/G con KPIs medibles (PUE, emisiones Scope 1-2-3, % mujeres en puestos técnicos, auditorías éticas de código/IA) y redacción del Informe de Sostenibilidad formal.",
        "• Entregables: Documento formal del Plan e Informe de Sostenibilidad + Presentación ejecutiva en formato Role-Play (defensa del plan ante el 'Comité de Dirección / Inversores', 12-15 min de exposición + ronda de preguntas del tribunal).",
        "• Criterios evaluados: RA6 (a, b, c, d, e) y consolidación integrada de RA1 a RA5."
    ], title="Proyecto Integrador Trimestre 3 (T3)")

    # -------------------------------------------------------------
    # 7. METODOLOGÍA DIDÁCTICA Y PRINCIPIOS PEDAGÓGICOS
    # -------------------------------------------------------------
    heading_1("7. METODOLOGÍA DIDÁCTICA Y PRINCIPIOS PEDAGÓGICOS")
    body_p("La metodología adoptada en el módulo responde a un enfoque activo, constructivista, cooperativo y orientado al desarrollo de competencias profesionales reales en el sector informático:")

    bullet_p("Cada trimestre se articula en torno a un proyecto integrador real que culmina en un producto tangible (Informe ASG, Prototipo Ecodiseñado, Plan Corporativo GRI/CSRD). El alumnado asume un rol protagonista en su propio aprendizaje.", "Aprendizaje Basado en Proyectos (ABP): ")
    bullet_p("Se trabaja en equipos heterogéneos de 2 a 3 alumnos, asignando roles coordinados (analista ASG, desarrollador/Green Coder, responsable de métricas, coordinador de informe) para fomentar la corresponsabilidad y el debate constructivo.", "Aprendizaje Cooperativo: ")
    bullet_p("Uso intensivo de las fichas de casos reales de la industria tecnológica (docs/09-casos-empresas-sector-informatico.md) para analizar aciertos, controversias y estrategias reales de compañías como HP, Microsoft, Google, Dell, Indra/Minsait, IBM y startups españolas/andaluzas.", "Método del Caso y Benchmarking: ")
    bullet_p("Manejo de herramientas de estimación de huella de carbono digital, calculadoras de emisiones de software (Green Software Foundation), herramientas de benchmarking de hardware (Energy Star, EPEAT), simuladores de PUE en centros de datos y plataformas de gestión del aula virtual (Moodle Centros / Google Classroom).", "Herramientas Técnicas y Software Real: ")
    bullet_p("En las presentaciones trimestrales se implementan dinámicas de Role-Playing en las que los alumnos adoptan el papel de consultores ASG, directores de tecnología (CTO) o auditores medioambientales defendiendo sus propuestas ante el resto del grupo.", "Simulación Profesional y Role-Playing: ")

    # -------------------------------------------------------------
    # 8. EVALUACIÓN Y CALIFICACIÓN
    # -------------------------------------------------------------
    heading_1("8. EVALUACIÓN, INSTRUMENTOS Y CRITERIOS DE CALIFICACIÓN")
    body_p("De acuerdo con el Decreto 104/2024, de 28 de mayo, y la Orden de 18 de septiembre de 2025 de la Junta de Andalucía, la evaluación en Formación Profesional es continua, formativa, integradora y basada en la consecución de los Resultados de Aprendizaje y Criterios de Evaluación oficiales.")

    heading_2("8.1 Instrumentos y Procedimientos de Evaluación")
    bullet_p("Evaluación del informe técnico, rigor conceptual, fuentes contrastadas, diseño de matrices y prototipos técnicos (70% de la nota de cada proyecto). Se aplican las rúbricas analíticas oficiales detalladas en docs/08-practicas-y-trabajos-sector-informatico.md.", "Proyectos Trimestrales Integradores (T1, T2, T3): ")
    bullet_p("Cuestionarios de autoevaluación al final de cada unidad (docs/01 a 07), ejercicios prácticos de clase (cálculo de huella, auditoría verde del aula de informática, fichas de casos de docs/09) y actividades intermedias (20% de la nota del trimestre).", "Actividades de Aula y Cuestionarios Técnicos: ")
    bullet_p("Valoración de la claridad expositiva, vocabulario técnico, capacidad de argumentación y respuesta a las preguntas del tribunal (integrado en la rúbrica del proyecto trimestral).", "Defensa Oral y Presentación Pública: ")
    bullet_p("Registro sistemático del trabajo en equipo, puntualidad en las entregas, respeto a la propiedad intelectual, rigor deontológico y participación activa en debates (10% de la nota del trimestre).", "Observación y Competencias Transversales: ")

    heading_2("8.2 Criterios de Calificación y Superación del Módulo")
    bullet_p("La calificación de cada trimestre se obtiene de la media ponderada de los Criterios de Evaluación trabajados en el periodo (T1 = 33,33%; T2 = 33,33%; T3 = 33,33%).", "Ponderación Trimestral: ")
    bullet_p("Para superar el módulo profesional, es preceptivo que la media aritmética ponderada de los Criterios de Evaluación asociados a cada uno de los 6 Resultados de Aprendizaje (RA1 a RA6) alcance una calificación igual o superior a 5,0 puntos sobre 10.", "Requisito de Superación Criterial: ")
    bullet_p("La calificación final del módulo será la media aritmética ponderada de las calificaciones obtenidas en los tres trimestres (o media global de los 6 RAs), redondeada a un número entero entre 1 y 10 conforme a la normativa andaluza.", "Calificación Final Ordinaria: ")

    heading_2("8.3 Procedimientos de Recuperación Continua y Extraordinaria")
    bullet_p("El alumnado que no alcance una calificación mínima de 5,0 en una Unidad Didáctica / Proyecto Trimestral dispondrá de un plan de recuperación individualizado consistente en la corrección, ampliación y defensa individual del proyecto no superado, garantizando la adquisición de los CE deficientes.", "Recuperación de Proyectos Trimestrales: ")
    bullet_p("En caso de no superar el módulo en la evaluación final ordinaria de mayo, el alumno/a realizará una prueba extraordinaria/proyecto integrador global que evaluará exclusivamente los Resultados de Aprendizaje no superados durante el curso.", "Evaluación Extraordinaria: ")

    # -------------------------------------------------------------
    # 9. FORMACIÓN EN EMPRESA U ORGANISMO EQUIPARADO (RÉGIMEN DUAL)
    # -------------------------------------------------------------
    heading_1("9. FORMACIÓN EN EMPRESA U ORGANISMO EQUIPARADO (RÉGIMEN DUAL EN GRADO D)")
    body_p("En aplicación de la Ley Orgánica 3/2022, el Real Decreto 659/2023 y el Decreto 104/2024 de la Junta de Andalucía, todas las enseñanzas de FP de Grado D tienen carácter dual. El régimen general establece un mínimo del 25% de las horas totales del ciclo formativo en empresas colaboradoras (500 horas totales):")

    bullet_p("80 horas lectivas de estancia formativa en empresas del sector TIC (distribuidas en marzo/abril durante 10-13 jornadas laborales de 6 a 8 horas diarias).", "Primer Curso (1º DAW / 1º DAM): ")
    bullet_p("420 horas de formación en centros de trabajo y empresas tecnológicas colaboradoras.", "Segundo Curso (2º DAW / 2º DAM): ")

    heading_2("9.1 Resultados de Aprendizaje y Actividades en la Empresa Colaboradora")
    body_p("Durante la estancia dual de primer curso, el módulo de Sostenibilidad aplicada al sistema productivo se vincula directamente con la actividad en la empresa mediante las siguientes actuaciones recogidas en el Plan de Formación Individualizado:")
    bullet_p("Identificación de los grupos de interés de la empresa tecnológica receptora (clientes, empleados, proveedores cloud/hardware, administración).", "RA6.a (Grupos de Interés): ")
    bullet_p("Análisis de los aspectos ASG materiales en la empresa: políticas de consumo energético en oficinas/servidores, gestión y reciclaje de RAEE (equipos obsoletos, cables, monitores), política de teletrabajo y huella de transporte, medidas de conciliación e igualdad de género, y protocolos de ciberseguridad y protección de datos.", "RA6.b y RA6.c (Aspectos ASG y Acciones): ")
    bullet_p("Propuesta constructiva de buenas prácticas de Green Coding, optimización de recursos en el desarrollo de software y compra responsable de componentes.", "RA3.c y RA5.f (Estrategias sostenibles): ")

    body_p("El tutor docente del centro educativo y el tutor laboral de la empresa mantendrán una coordinación periódica para el seguimiento del cuaderno de prácticas y la evaluación formativa de estas competencias.")

    # -------------------------------------------------------------
    # 10. ATENCIÓN A LA DIVERSIDAD Y DISEÑO UNIVERSAL PARA EL APRENDIZAJE (DUA)
    # -------------------------------------------------------------
    heading_1("10. ATENCIÓN A LA DIVERSIDAD Y DISEÑO UNIVERSAL PARA EL APRENDIZAJE (DUA)")
    body_p("En coherencia con los principios del Diseño Universal para el Aprendizaje (DUA), la programación garantiza la accesibilidad cognitiva, sensorial y física a todos los estudiantes mediante:")
    bullet_p("Textos claros, resúmenes conceptuales, esquemas gráficos, vídeos técnicos, fichas resumen (docs/01 a 07) y glosario terminológico (docs/10).", "Múltiples formas de representación: ")
    bullet_p("Posibilidad de elaborar entregables en diversos formatos (documentos técnicos, presentaciones interactivas, infografías, prototipos de software, grabaciones de defensa).", "Múltiples formas de acción y expresión: ")
    bullet_p("Vinculación de los proyectos con intereses profesionales reales (IA, videojuegos, ciberseguridad, cloud, sostenibilidad comarcal), debates participativos y aprendizaje cooperativo.", "Múltiples formas de implicación y compromiso: ")

    heading_2("10.1 Medidas Concretas de Adaptación para el Grupo")
    bullet_p("Desglose pormenorizado de las tareas del proyecto, rúbricas de autoevaluación paso a paso, refuerzo conceptual en tutorías y asignación de roles colaborativos complementarios.", "Alumnado con dificultades o ritmo lento: ")
    bullet_p("Se plantean retos de ampliación e investigación avanzada: cálculo formal del índice SCI (Software Carbon Intensity) en proyectos de programación Java/Web, análisis avanzado de la Taxonomía Verde Europea aplicada a Fintech, diseño de algoritmos de optimización energética de servidores y mentoría voluntaria a compañeros de grupo.", "Alumnado con Altas Capacidades Intelectuales (NEAE Sobredotación): ")
    bullet_p("Adaptación de puesto ergonómico en el aula de informática, acceso a herramientas digitales accesibles y aplicación estricta del protocolo del Plan de Autoprotección del Centro (evacuación asistida en ascensor o acompañamiento por equipo de 3 compañeros designados).", "Alumnado con Discapacidad Física Motriz (NEE): ")
    bullet_p("Seguimiento intensivo a través del aula virtual (Moodle Centros), repositorio de materiales online (docs/), flexibilización en tutorías virtuales individuales y posibilidad de entregas asíncronas justificadas.", "Alumnado Trabajador o con Matrícula Modular: ")
    bullet_p("Plan de acogida, acceso inmediato al repositorio digital de materiales y adaptación de plazos para la realización de las actividades de evaluación.", "Alumnado de Incorporación Tardía o Repetidor: ")

    # -------------------------------------------------------------
    # 11. ELEMENTOS TRANSVERSALES Y PROYECTO LINGÜÍSTICO DE CENTRO
    # -------------------------------------------------------------
    heading_1("11. ELEMENTOS TRANSVERSALES Y PROYECTO LINGÜÍSTICO DE CENTRO")
    body_p("En cumplimiento de los artículos 39 y 40 de la Ley 17/2007 (LEA) y del Real Decreto 659/2023, la programación incorpora de forma sistemática los siguientes valores transversales:")
    bullet_p("Constituye el eje vertebrador del módulo (análisis del cambio climático, descarbonización, economía circular y preservación de la biodiversidad).", "Transición Ecológica y Educación Ambiental: ")
    bullet_p("Fomento de la presencia de mujeres en el sector tecnológico y visibilización de referentes femeninos en ingeniería informática y sostenibilidad (ODS 5). Lenguaje no sexista e inclusivo en toda la documentación técnica.", "Igualdad Efectiva entre Hombres y Mujeres: ")
    bullet_p("Sensibilización en el respeto a la privacidad, la protección de datos personales (RGPD / LOPDGDD), la lucha contra la desinformación y el uso ético de la Inteligencia Artificial.", "Derechos Digitales y Ética Tecnológica: ")
    bullet_p("Ergonomía postural ante pantallas de visualización de datos (PVD), prevención de riesgos psicosociales y desconexión digital.", "Salud Laboral y Ergonomía en Informática: ")
    bullet_p("En coherencia con el PLC, se fomenta la lectura y análisis crítico de documentación técnica en español e inglés (informes ASG, directivas europeas, documentación de APIs). En las pruebas escritas y memorias de proyectos se cuidará la corrección ortográfica y sintáctica, pudiendo penalizarse hasta un máximo de 2 puntos (0,2 por falta grave) con posibilidad de reescritura formativa.", "Proyecto Lingüístico de Centro (Comprensión y Expresión): ")

    # -------------------------------------------------------------
    # 12. ACTIVIDADES COMPLEMENTARIAS Y EXTRAESCOLARES
    # -------------------------------------------------------------
    heading_1("12. ACTIVIDADES COMPLEMENTARIAS Y EXTRAESCOLARES")
    body_p("Con el propósito de conectar la formación en el aula con el ecosistema tecnológico y empresarial de Andalucía, se proyectan las siguientes actividades complementarias y extraescolares (sujetas a aprobación por el Consejo Escolar):")
    bullet_p("Visita a las instalaciones de centros de procesamiento de datos con certificación de eficiencia energética (PUE bajo) o plantas de tratamiento y valorización de RAEE en Andalucía.", "Visitas Técnicas a Data Centers e Instalaciones Circulares: ")
    bullet_p("Participación en conferencias, jornadas técnicas y webinars sobre Green Software Engineering, Cloud Sostenible y gobernanza ASG con profesionales de empresas del sector (Indra, Minsait, Telefónica Tech, Google Developer Groups, etc.).", "Jornadas Técnicas y Encuentros con Profesionales: ")
    bullet_p("Mesa redonda con antiguos alumnos/as de DAW y DAM que se encuentren trabajando en desarrollo de software, DevOps o consultoría digital, compartiendo su experiencia sobre sostenibilidad y prácticas corporativas.", "Encuentros con Antiguos Alumnos del Centro: ")

    # -------------------------------------------------------------
    # 13. RECURSOS DIDÁCTICOS, BIBLIOGRAFÍA Y MATERIALES DEL MÓDULO
    # -------------------------------------------------------------
    heading_1("13. RECURSOS DIDÁCTICOS, BIBLIOGRAFÍA Y MATERIALES DEL MÓDULO")
    body_p("El desarrollo del módulo cuenta con un conjunto integral de materiales didácticos preparados y organizados en la carpeta del módulo, estructurados en 10 bloques temáticos:")

    mat_headers = ["Documento", "Título del Recurso en docs/", "Contenido Principal y Utilidad Didáctica"]
    mat_data = [
        ["01", "01-fundamentos-sostenibilidad.md", "Fundamentos, Informe Brundtland, pilares E/S/G, Cumbres de la Tierra, Acuerdo de París COP21, Agenda 2030, ODS prioritarios en TIC y Taxonomía Verde Europea."],
        ["02", "02-aspectos-ASG-y-grupos-de-interes.md", "Aspectos ASG en empresas tecnológicas, mapa de grupos de interés (Mendelow), matriz de materialidad y análisis de riesgos/oportunidades."],
        ["03", "03-estandares-metricas-e-inversion-responsable.md", "Estándares ISO 14001, ISO 14064, GRI Standards, SASB/ISSB, CDP, métricas técnicas TIC (PUE, WUE, CUE, Scope 1-2-3, SCI), Inversión Responsable (ISR) y CSRD/ESRS."],
        ["04", "04-retos-ambientales-y-sociales-sector-informatico.md", "Retos ambientales y sociales del sector TIC: consumo energético, IA, agua, RAEE, minerales críticos, obsolescencia, brecha digital, ética, privacidad y alianzas ODS 17."],
        ["05", "05-economia-circular-verde-y-ecodisenio.md", "Modelo lineal vs circular, principios de Ellen MacArthur, 9R, servitización (DaaS), Ecodiseño de hardware y Green Coding / software verde, Análisis de Ciclo de Vida (LCA/ACV)."],
        ["06", "06-actividades-sostenibles-en-ti.md", "Evaluación de huella personal/profesional del programador, Green IT, compras sostenibles y marco normativo ambiental (Directiva RAEE, RD 110/2015, Ley 7/2022, LECA)."],
        ["07", "07-plan-sostenibilidad-e-informe.md", "Guía para la elaboración de un Plan de Sostenibilidad Corporativo para una empresa TIC y redacción del Informe de Sostenibilidad (formato GRI / CSRD)."],
        ["08", "08-practicas-y-trabajos-sector-informatico.md", "Propuesta completa de proyectos integradores por trimestre (T1, T2, T3), prácticas intermedias y rúbricas oficiales de calificación sobre 10 puntos."],
        ["09", "09-casos-empresas-sector-informatico.md", "Fichas técnicas y análisis ASG de grandes multinacionales TIC (HP, Microsoft, Google, Dell, Indra/Minsait, IBM, Amazon) y casos españoles."],
        ["10", "10-glosario-recursos-bibliografia.md", "Glosario técnico de términos de sostenibilidad, enlaces oficiales a estándares internacionales y soluciones orientativas a los cuestionarios."]
    ]
    styled_table(mat_headers, mat_data, col_widths=[0.6, 2.5, 3.6], header_bg="0F4C81")

    # Enlaces y bibliografía
    body_p("Recursos y portales oficiales de referencia para el módulo:")
    bullet_p("Naciones Unidas: un.org/sustainabledevelopment (Portal oficial de los 17 ODS y metas de la Agenda 2030).", "• ")
    bullet_p("Global Reporting Initiative (GRI): globalreporting.org (Estándares universales y temáticos de reporte de sostenibilidad).", "• ")
    bullet_p("Green Software Foundation: greensoftware.foundation (Especificación del Software Carbon Intensity - SCI y guías de Green Coding).", "• ")
    bullet_p("The Green Grid: thegreengrid.org (Estándares métricos PUE, WUE y CUE para centros de datos).", "• ")
    bullet_p("Fundación Ellen MacArthur: ellenmacarthurfoundation.org (Casos y principios de economía circular).", "• ")
    bullet_p("Comisión Europea - Pacto Verde y CSRD: finance.ec.europa.eu (Directiva CSRD y normas técnicas ESRS).", "• ")
    bullet_p("Junta de Andalucía - Consejería de Sostenibilidad y Medio Ambiente: juntadeandalucia.es (Ley de Economía Circular y Estrategia Andaluza de Cambio Climático).", "• ")

    # Guardar archivo docx
    output_docx_1 = r"Programación\PD_Sostenibilidad_DAW_DAM_Andalucia_2025_2026.docx"
    output_docx_2 = r"Programación\PD_Sostenibilidad_1DAW_2025_2026.docx"
    
    doc.save(output_docx_1)
    doc.save(output_docx_2)
    print(f"Documentos Word guardados con éxito en:\n1. {output_docx_1}\n2. {output_docx_2}")

if __name__ == "__main__":
    build_programacion()
