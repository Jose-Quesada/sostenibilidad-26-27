import sys
import os
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.Workbook()
wb.remove(wb.active)  # Remove default sheet

# -------------------------------------------------------------
# Color Palette & Visual System Tokens (Emerald / Eco Theme for Sustainability)
# -------------------------------------------------------------
NAVY_HEADER = "064E3B"       # Emerald 900
NAVY_SUBHEADER = "065F46"    # Emerald 800
EMERALD_HEADER = "047857"    # Emerald 700
EMERALD_LIGHT = "D1FAE5"     # Emerald 100
TEAL_HEADER = "0F766E"       # Teal 700
TEAL_LIGHT = "CCFBF1"        # Teal 100
BLUE_HEADER = "1D4ED8"       # Blue 700
BLUE_LIGHT = "DBEAFE"        # Blue 100
GREEN_HEADER = "15803D"      # Green 700
GREEN_LIGHT = "DCFCE7"       # Green 100
PURPLE_HEADER = "6B21A8"     # Purple 700
PURPLE_LIGHT = "F3E8FF"      # Purple 100
AMBER_HEADER = "B45309"      # Amber 700
AMBER_LIGHT = "FEF3C7"       # Amber 100
LIME_HEADER = "4D7C0F"       # Lime 700
LIME_LIGHT = "ECFCCB"        # Lime 100
ZEBRA_FILL = "F8FAFC"        # Slate 50
TOTAL_FILL = "FEF3C7"        # Amber 100
HIGHLIGHT_ROW = "FEF9C3"     # Yellow 100

FILL_NAVY = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type="solid")
FILL_SUBHEADER = PatternFill(start_color=NAVY_SUBHEADER, end_color=NAVY_SUBHEADER, fill_type="solid")
FILL_EMERALD_HEADER = PatternFill(start_color=EMERALD_HEADER, end_color=EMERALD_HEADER, fill_type="solid")
FILL_EMERALD_LIGHT = PatternFill(start_color=EMERALD_LIGHT, end_color=EMERALD_LIGHT, fill_type="solid")
FILL_TEAL_HEADER = PatternFill(start_color=TEAL_HEADER, end_color=TEAL_HEADER, fill_type="solid")
FILL_TEAL_LIGHT = PatternFill(start_color=TEAL_LIGHT, end_color=TEAL_LIGHT, fill_type="solid")
FILL_BLUE_HEADER = PatternFill(start_color=BLUE_HEADER, end_color=BLUE_HEADER, fill_type="solid")
FILL_BLUE_LIGHT = PatternFill(start_color=BLUE_LIGHT, end_color=BLUE_LIGHT, fill_type="solid")
FILL_GREEN_HEADER = PatternFill(start_color=GREEN_HEADER, end_color=GREEN_HEADER, fill_type="solid")
FILL_GREEN_LIGHT = PatternFill(start_color=GREEN_LIGHT, end_color=GREEN_LIGHT, fill_type="solid")
FILL_PURPLE_HEADER = PatternFill(start_color=PURPLE_HEADER, end_color=PURPLE_HEADER, fill_type="solid")
FILL_PURPLE_LIGHT = PatternFill(start_color=PURPLE_LIGHT, end_color=PURPLE_LIGHT, fill_type="solid")
FILL_AMBER_HEADER = PatternFill(start_color=AMBER_HEADER, end_color=AMBER_HEADER, fill_type="solid")
FILL_AMBER_LIGHT = PatternFill(start_color=AMBER_LIGHT, end_color=AMBER_LIGHT, fill_type="solid")
FILL_LIME_HEADER = PatternFill(start_color=LIME_HEADER, end_color=LIME_HEADER, fill_type="solid")
FILL_LIME_LIGHT = PatternFill(start_color=LIME_LIGHT, end_color=LIME_LIGHT, fill_type="solid")
FILL_ZEBRA = PatternFill(start_color=ZEBRA_FILL, end_color=ZEBRA_FILL, fill_type="solid")
FILL_TOTAL = PatternFill(start_color=TOTAL_FILL, end_color=TOTAL_FILL, fill_type="solid")
FILL_HIGHLIGHT = PatternFill(start_color=HIGHLIGHT_ROW, end_color=HIGHLIGHT_ROW, fill_type="solid")

FONT_TITLE = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
FONT_SUBTITLE = Font(name="Segoe UI", size=10, italic=True, color="E2E8F0")
FONT_HEADER = Font(name="Segoe UI", size=9, bold=True, color="FFFFFF")
FONT_HEADER_DARK = Font(name="Segoe UI", size=9, bold=True, color="064E3B")
FONT_BODY = Font(name="Segoe UI", size=9)
FONT_BODY_BOLD = Font(name="Segoe UI", size=9, bold=True)
FONT_KPI_VAL = Font(name="Segoe UI", size=16, bold=True, color="064E3B")
FONT_KPI_LBL = Font(name="Segoe UI", size=8, bold=True, color="475569")

BORDER_THIN = Side(border_style="thin", color="CBD5E1")
BORDER_MEDIUM = Side(border_style="medium", color="64748B")
BORDER_DOUBLE = Side(border_style="double", color="064E3B")

CELL_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_THIN)
TOTAL_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_DOUBLE)
HEADER_BORDER = Border(left=BORDER_THIN, right=BORDER_THIN, top=BORDER_THIN, bottom=BORDER_MEDIUM)

ALIGN_CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
ALIGN_LEFT = Alignment(horizontal="left", vertical="center")
ALIGN_RIGHT = Alignment(horizontal="right", vertical="center")

# 15 Students (Realistic for 1º DAW / DAM)
STUDENTS = [
    ("Álvarez Gómez", "Laura"),
    ("Benítez Romero", "Carlos"),
    ("Castillo Morales", "Elena"),
    ("Delgado Santos", "Alejandro"),
    ("Fernández Navarro", "Lucía"),
    ("García Serrano", "David"),
    ("Herrera Cruz", "Marta"),
    ("Jiménez Ortiz", "Pablo"),
    ("López Molina", "Sara"),
    ("Martín Vega", "Javier"),
    ("Navarro Gil", "Ana"),
    ("Pérez Rubio", "Álvaro"),
    ("Ramírez Soto", "Carmen"),
    ("Sánchez Vidal", "Daniel"),
    ("Torres Lozano", "Irene")
]

# 34 Official CEs for Sostenibilidad Aplicada al Sistema Productivo (Código 1708 - RD 659/2023 Anexo VIII)
# Format: (RA_code, RA_weight, CE_code, CE_description, UDs, exact_ce_weight, default_tasks_x)
# Tasks indices:
# T1 (T01:0, T02:1, T03:2, T04:3)
# T2 (T05:4, T06:5, T07:6, T08:7)
# T3 (T09:8, T10:9, T11:10, T12:11)
CRITERIA_DATA = [
    # RA1: Identifica aspectos ASG, desarrollo sostenible y marcos internacionales (18% total, 3% each)
    ("RA1", 0.18, "CE1.a", "Se ha descrito el concepto de sostenibilidad y los marcos internacionales.", "UD01", 0.03, [0, 2]),
    ("RA1", 0.18, "CE1.b", "Se han identificado los asuntos ASG en las organizaciones TIC.", "UD02", 0.03, [0, 2, 3]),
    ("RA1", 0.18, "CE1.c", "Se han relacionado los ODS con la Agenda 2030 en el sector tecnológico.", "UD01", 0.03, [0, 2]),
    ("RA1", 0.18, "CE1.d", "Se ha analizado la relevancia de los ASG para los grupos de interés (riesgos/oportunidades).", "UD02", 0.03, [2, 10]),
    ("RA1", 0.18, "CE1.e", "Se han identificado estándares de métricas e información (ISO, GRI, SASB, CSRD).", "UD03", 0.03, [0, 2, 8]),
    ("RA1", 0.18, "CE1.f", "Se ha descrito la inversión socialmente responsable (ISR) y las agencias ESG.", "UD03", 0.03, [0, 2]),

    # RA2: Caracteriza retos ambientales y sociales en el sector productivo y propone acciones (15% total, 3% each)
    ("RA2", 0.15, "CE2.a", "Se han identificado los principales retos ambientales y sociales del sector TIC.", "UD04", 0.03, [1, 2]),
    ("RA2", 0.15, "CE2.b", "Se han relacionado los retos con la actividad económica y digital.", "UD04", 0.03, [1, 2]),
    ("RA2", 0.15, "CE2.c", "Se ha analizado el impacto ambiental y social sobre personas y sectores productivos.", "UD04", 0.03, [1, 2]),
    ("RA2", 0.15, "CE2.d", "Se han identificado medidas y acciones para minimizar impactos.", "UD04", 0.03, [1, 2, 10]),
    ("RA2", 0.15, "CE2.e", "Se ha analizado la importancia de alianzas transversales (ODS 17).", "UD01, UD04", 0.03, [2, 3, 10]),

    # RA3: Establece la aplicación de criterios de sostenibilidad en desempeño profesional y personal (9% total, 3% each)
    ("RA3", 0.09, "CE3.a", "Se han identificado los ODS más relevantes para la actividad profesional TIC.", "UD01, UD04", 0.03, [1, 2]),
    ("RA3", 0.09, "CE3.b", "Se han analizado los riesgos y oportunidades de los ODS en informática.", "UD04", 0.03, [1, 2]),
    ("RA3", 0.09, "CE3.c", "Se han identificado acciones prácticas para retos ambientales/sociales personal y laboral.", "UD04, UD06", 0.03, [2, 3, 5, 11]),

    # RA4: Propone productos y servicios responsables aplicando principios de economía circular (18% total, 3% each)
    ("RA4", 0.18, "CE4.a", "Se ha caracterizado el modelo de producción y consumo lineal frente al circular.", "UD05", 0.03, [4, 6]),
    ("RA4", 0.18, "CE4.b", "Se han identificado los principios de la economía verde y circular.", "UD05", 0.03, [4, 6]),
    ("RA4", 0.18, "CE4.c", "Se han contrastado los beneficios de la economía circular frente al modelo clásico.", "UD05", 0.03, [4, 6]),
    ("RA4", 0.18, "CE4.d", "Se han aplicado principios de ecodiseño (hardware y software).", "UD05, UD06", 0.03, [4, 6, 7]),
    ("RA4", 0.18, "CE4.e", "Se ha analizado el ciclo de vida del producto TIC (LCA/ACV).", "UD05", 0.03, [6, 10]),
    ("RA4", 0.18, "CE4.f", "Se han identificado procesos productivos y criterios de sostenibilidad aplicados.", "UD05, UD06", 0.03, [6, 10]),

    # RA5: Realiza actividades sostenibles minimizando el impacto en el medio ambiente (18% total, 2% each)
    ("RA5", 0.18, "CE5.a", "Se ha caracterizado el modelo de consumo actual.", "UD05", 0.02, [4]),
    ("RA5", 0.18, "CE5.b", "Se han identificado principios de economía verde/circular.", "UD05", 0.02, [4]),
    ("RA5", 0.18, "CE5.c", "Se han contrastado los beneficios del modelo circular.", "UD05", 0.02, [4, 5]),
    ("RA5", 0.18, "CE5.d", "Se ha evaluado el impacto de actividades personales y profesionales (huella digital).", "UD06", 0.02, [5, 6, 7]),
    ("RA5", 0.18, "CE5.e", "Se han aplicado principios de ecodiseño.", "UD05, UD06", 0.02, [6]),
    ("RA5", 0.18, "CE5.f", "Se han aplicado estrategias sostenibles (Green IT, cloud verde, eficiencia energética).", "UD06", 0.02, [5, 6, 10, 11]),
    ("RA5", 0.18, "CE5.g", "Se ha analizado el ciclo de vida.", "UD05", 0.02, [5, 6]),
    ("RA5", 0.18, "CE5.h", "Se han identificado procesos productivos sostenibles.", "UD06", 0.02, [6, 10]),
    ("RA5", 0.18, "CE5.i", "Se ha aplicado la normativa ambiental (RAEE, Ley 7/2022, LECA, ESPR).", "UD06", 0.02, [4, 5, 6]),

    # RA6: Analiza un plan de sostenibilidad de empresa TIC y elabora informe (22% total, 4.4% each)
    ("RA6", 0.22, "CE6.a", "Se han identificado los principales grupos de interés de la empresa TIC (stakeholders).", "UD07, UD09", 0.044, [8, 10, 11]),
    ("RA6", 0.22, "CE6.b", "Se han analizado los aspectos ASG materiales y la matriz de doble materialidad.", "UD07", 0.044, [8, 10]),
    ("RA6", 0.22, "CE6.c", "Se han definido acciones de mitigación de impactos negativos y oportunidades.", "UD07", 0.044, [9, 10, 11]),
    ("RA6", 0.22, "CE6.d", "Se han determinado métricas e indicadores de desempeño (GRI, ESRS, PUE, SCI).", "UD07, UD08", 0.044, [9, 10]),
    ("RA6", 0.22, "CE6.e", "Se ha elaborado un informe formal de sostenibilidad con el plan propuesto.", "UD07, UD08", 0.044, [10])
]

# Task metadata: (TaskCode, ShortTitle, FullName, UDs, Trimestre)
TASKS_INFO = [
    # Trimestre 1 (Cols H to K in Matriz, Cols D to G in Registro)
    ("T01", "Fundamentos ASG", "Cuestionario 1: Fundamentos de Sostenibilidad, ODS y Marcos Internacionales", "UD01-03", "T1"),
    ("T02", "Retos Sector TIC", "Tarea Práctica 1: Análisis de Retos Ambientales y Sociales en Informática", "UD03-04", "T1"),
    ("T03", "Proyecto Mapa ASG", "Proyecto Integrador T1: Mapa ASG y Diagnóstico ODS de Empresa Tecnológica", "UD01-04, 09", "T1"),
    ("T04", "Debate & Actitud T1", "Participación en Debates ASG, Deontología y Trabajo en Equipo T1", "Transversal", "T1"),

    # Trimestre 2 (Cols L to O in Matriz, Cols H to K in Registro)
    ("T05", "Economía Circular", "Cuestionario 2: Principios de Economía Circular, Normativa RAEE y LECA", "UD05-06", "T2"),
    ("T06", "Green IT & Huella", "Tarea Práctica 2: Auditoría de Huella Digital y Métricas Green Coding", "UD06, 08", "T2"),
    ("T07", "Proyecto Ecodiseño", "Proyecto Integrador T2: Ecodiseño y Análisis de Ciclo de Vida (LCA) TIC", "UD05-06, 08", "T2"),
    ("T08", "Rigor & Actitud T2", "Rigor Técnico en Mediciones, Buenas Prácticas y Trabajo en Equipo T2", "Transversal", "T2"),

    # Trimestre 3 (Cols P to S in Matriz, Cols L to O in Registro)
    ("T09", "Estándares GRI", "Cuestionario 3: Estándares de Reporte (GRI / ESRS) y Doble Materialidad", "UD07", "T3"),
    ("T10", "KPIs Sostenibilidad", "Tarea Práctica 3: Definición de KPIs de Desempeño Energético y Ambiental", "UD07-08", "T3"),
    ("T11", "Plan Sostenibilidad", "Proyecto Integrador T3: Plan Integral de Sostenibilidad e Informe CSRD", "UD07-10", "T3"),
    ("T12", "Vinculación Dual T3", "Transferencia a Empresa Colaboradora Dual, Ética y Defensa Final T3", "Transversal", "T3")
]

# Realistic grades for the 15 students across the 12 tasks
STUDENT_TASK_GRADES = [
    [8.5, 9.0, 8.5, 9.0,   8.5, 9.0, 8.5, 9.5,   9.0, 8.5, 9.0, 9.5],
    [6.0, 6.5, 6.0, 7.0,   6.5, 6.0, 6.5, 7.0,   6.0, 6.5, 6.0, 7.0],
    [9.5, 9.5, 10.0, 10.0, 10.0, 9.5, 10.0, 10.0, 9.5, 10.0, 10.0, 10.0],
    [4.5, 5.0, 4.5, 6.0,   5.0, 4.5, 4.5, 5.5,   5.0, 4.5, 4.0, 5.0],
    [7.5, 8.0, 7.5, 8.5,   7.5, 8.0, 7.5, 8.5,   8.0, 7.5, 8.0, 8.5],
    [8.0, 8.5, 8.0, 8.5,   8.0, 8.5, 8.0, 8.5,   8.5, 8.0, 8.5, 8.5],
    [9.0, 9.0, 9.5, 9.5,   9.0, 9.5, 9.0, 9.5,   9.5, 9.0, 9.5, 9.5],
    [5.5, 5.5, 6.0, 6.5,   5.5, 6.0, 5.5, 6.5,   6.0, 5.5, 5.5, 6.5],
    [10.0, 9.5, 10.0, 10.0, 10.0, 9.5, 10.0, 10.0, 10.0, 9.5, 10.0, 10.0],
    [3.5, 4.0, 4.0, 5.0,   4.0, 4.5, 4.0, 4.5,   4.0, 4.0, 4.0, 4.5],
    [8.0, 8.5, 8.0, 9.0,   8.5, 8.0, 8.5, 9.0,   8.0, 8.5, 8.5, 9.0],
    [7.0, 7.0, 7.5, 7.5,   7.5, 7.0, 7.5, 7.5,   7.0, 7.5, 7.0, 7.5],
    [6.5, 6.5, 7.0, 7.0,   7.0, 6.5, 7.0, 7.0,   6.5, 7.0, 6.5, 7.0],
    [8.5, 9.0, 8.5, 9.5,   9.0, 8.5, 9.0, 9.5,   9.0, 8.5, 9.0, 9.5],
    [9.0, 9.5, 9.0, 9.5,   9.5, 9.0, 9.5, 10.0,  9.0, 9.5, 9.5, 10.0]
]


# =============================================================
# SHEET 1: MATRIZ DE CRITERIOS (SELECTOR AVANZADO DE TAREAS)
# =============================================================
ws_mat = wb.create_sheet(title="Matriz Criterios")
ws_mat.views.sheetView[0].showGridLines = True

# Title
ws_mat.merge_cells("A1:T1")
ws_mat["A1"] = "MATRIZ DE SELECCIÓN DE CRITERIOS DE EVALUACIÓN POR TAREA — SOSTENIBILIDAD (1º DAW / DAM)"
ws_mat["A1"].font = FONT_TITLE
ws_mat["A1"].fill = FILL_NAVY
ws_mat["A1"].alignment = ALIGN_CENTER
ws_mat.row_dimensions[1].height = 36

ws_mat.merge_cells("A2:T2")
ws_mat["A2"] = "Marca con una 'X' en la casilla correspondiente para activar los criterios evaluados en cada tarea. Las filas 41 y 42 se calculan automáticamente."
ws_mat["A2"].font = FONT_SUBTITLE
ws_mat["A2"].fill = FILL_SUBHEADER
ws_mat["A2"].alignment = ALIGN_CENTER
ws_mat.row_dimensions[2].height = 20

# Header groups (Row 4)
ws_mat.merge_cells("A4:G4")
ws_mat["A4"] = "CRITERIOS OFICIALES DE EVALUACIÓN (RD 659/2023 ANEXO VIII & DECRETO 104/2024)"
ws_mat["A4"].font = FONT_HEADER
ws_mat["A4"].alignment = ALIGN_CENTER
ws_mat["A4"].fill = FILL_NAVY

ws_mat.merge_cells("H4:K4")
ws_mat["H4"] = "1er TRIMESTRE (T1) — ASG & RETOS"
ws_mat["H4"].font = FONT_HEADER
ws_mat["H4"].alignment = ALIGN_CENTER
ws_mat["H4"].fill = FILL_EMERALD_HEADER

ws_mat.merge_cells("L4:O4")
ws_mat["L4"] = "2º TRIMESTRE (T2) — CIRCULAR & GREEN IT"
ws_mat["L4"].font = FONT_HEADER
ws_mat["L4"].alignment = ALIGN_CENTER
ws_mat["L4"].fill = FILL_TEAL_HEADER

ws_mat.merge_cells("P4:S4")
ws_mat["P4"] = "3er TRIMESTRE (T3) — PLAN & REPORTE"
ws_mat["P4"].font = FONT_HEADER
ws_mat["P4"].alignment = ALIGN_CENTER
ws_mat["P4"].fill = FILL_BLUE_HEADER

ws_mat.merge_cells("T4:T5")
ws_mat["T4"] = "Pond. CE\nOficial"
ws_mat["T4"].font = FONT_HEADER
ws_mat["T4"].alignment = ALIGN_CENTER
ws_mat["T4"].fill = FILL_PURPLE_HEADER

# Column subheaders (Row 5)
col_defs_mat = [
    ("RA", 8),
    ("Peso RA", 9),
    ("Código CE", 10),
    ("Descripción Oficial del Criterio de Evaluación", 44),
    ("UDs", 14),
    ("Total\nTareas", 8),
    ("Estado Cobertura", 14)
]

for col_idx, (name, width) in enumerate(col_defs_mat, start=1):
    col_let = get_column_letter(col_idx)
    ws_mat.column_dimensions[col_let].width = width
    cell = ws_mat.cell(row=5, column=col_idx, value=name)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.fill = FILL_SUBHEADER
    cell.border = HEADER_BORDER

# Task headers (Cols H to S, idx 8 to 19)
for t_idx, t_info in enumerate(TASKS_INFO, start=8):
    col_let = get_column_letter(t_idx)
    ws_mat.column_dimensions[col_let].width = 12
    cell = ws_mat.cell(row=5, column=t_idx, value=f"{t_info[0]}\n{t_info[1]}")
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    if t_idx <= 11:
        cell.fill = FILL_EMERALD_HEADER
    elif t_idx <= 15:
        cell.fill = FILL_TEAL_HEADER
    else:
        cell.fill = FILL_BLUE_HEADER
    cell.border = HEADER_BORDER

ws_mat.column_dimensions["T"].width = 12
ws_mat.row_dimensions[5].height = 36

# Fill 34 Criterios (Rows 6 to 39)
for c_idx, crit in enumerate(CRITERIA_DATA, start=6):
    ws_mat.row_dimensions[c_idx].height = 24
    ra_code, ra_weight, ce_code, ce_desc, uds, ce_w, tasks_x = crit
    is_zebra = (c_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Col A: RA
    cA = ws_mat.cell(row=c_idx, column=1, value=ra_code)
    cA.font = FONT_BODY_BOLD
    cA.alignment = ALIGN_CENTER
    cA.fill = row_fill
    cA.border = CELL_BORDER
    
    # Col B: Peso RA
    cB = ws_mat.cell(row=c_idx, column=2, value=ra_weight)
    cB.font = FONT_BODY
    cB.alignment = ALIGN_CENTER
    cB.fill = row_fill
    cB.border = CELL_BORDER
    cB.number_format = "0.0%"
    
    # Col C: Codigo CE
    cC = ws_mat.cell(row=c_idx, column=3, value=ce_code)
    cC.font = FONT_BODY_BOLD
    cC.alignment = ALIGN_CENTER
    cC.fill = row_fill
    cC.border = CELL_BORDER
    
    # Col D: Descripcion
    cD = ws_mat.cell(row=c_idx, column=4, value=ce_desc)
    cD.font = FONT_BODY
    cD.alignment = ALIGN_LEFT
    cD.fill = row_fill
    cD.border = CELL_BORDER
    
    # Col E: UDs
    cE = ws_mat.cell(row=c_idx, column=5, value=uds)
    cE.font = FONT_BODY
    cE.alignment = ALIGN_CENTER
    cE.fill = row_fill
    cE.border = CELL_BORDER
    
    # Col F: Total Tareas que evaluan este criterio =COUNTIF(H{c_idx}:S{c_idx}, "X")
    cF = ws_mat.cell(row=c_idx, column=6)
    cF.value = f'=COUNTIF(H{c_idx}:S{c_idx}, "X")'
    cF.font = FONT_BODY_BOLD
    cF.alignment = ALIGN_CENTER
    cF.fill = FILL_TOTAL
    cF.border = CELL_BORDER
    
    # Col G: Estado Cobertura =IF(F{c_idx}>0, "EVALUADO", "SIN EVALUAR")
    cG = ws_mat.cell(row=c_idx, column=7)
    cG.value = f'=IF(F{c_idx}>0, "EVALUADO", "SIN EVALUAR")'
    cG.font = FONT_BODY_BOLD
    cG.alignment = ALIGN_CENTER
    cG.fill = row_fill
    cG.border = CELL_BORDER
    
    # Cols H to S: Tasks selection "X" (12 tasks)
    for t_i in range(12):
        col_target = 8 + t_i
        cell_x = ws_mat.cell(row=c_idx, column=col_target)
        if t_i in tasks_x:
            cell_x.value = "X"
            cell_x.font = Font(name="Segoe UI", size=10, bold=True, color="065F46")
            if col_target <= 11:
                cell_x.fill = FILL_EMERALD_LIGHT
            elif col_target <= 15:
                cell_x.fill = FILL_TEAL_LIGHT
            else:
                cell_x.fill = FILL_BLUE_LIGHT
        else:
            cell_x.value = ""
            cell_x.font = FONT_BODY
            cell_x.fill = row_fill
        cell_x.alignment = ALIGN_CENTER
        cell_x.border = CELL_BORDER
        
    # Col T: Ponderacion Oficial de este CE
    cT = ws_mat.cell(row=c_idx, column=20, value=ce_w)
    cT.font = FONT_BODY
    cT.alignment = ALIGN_CENTER
    cT.fill = row_fill
    cT.border = CELL_BORDER
    cT.number_format = "0.00%"

# Row 40: Total criterios evaluados por tarea
row_crit_count = 40
ws_mat.row_dimensions[row_crit_count].height = 24
ws_mat.merge_cells(f"A{row_crit_count}:G{row_crit_count}")
ws_mat[f"A{row_crit_count}"] = "TOTAL CRITERIOS EVALUADOS POR ESTA TAREA"
ws_mat[f"A{row_crit_count}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_crit_count}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_crit_count}"].fill = FILL_TOTAL
ws_mat[f"A{row_crit_count}"].border = TOTAL_BORDER

for t_i in range(12):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_tot = ws_mat.cell(row=row_crit_count, column=col_t)
    c_tot.value = f'=COUNTIF({col_let}$6:{col_let}$39, "X")'
    c_tot.font = FONT_BODY_BOLD
    c_tot.alignment = ALIGN_CENTER
    c_tot.fill = FILL_TOTAL
    c_tot.border = TOTAL_BORDER

c_tot_w = ws_mat.cell(row=row_crit_count, column=20, value="100.0%")
c_tot_w.font = FONT_BODY_BOLD
c_tot_w.alignment = ALIGN_CENTER
c_tot_w.fill = FILL_GREEN_LIGHT
c_tot_w.border = TOTAL_BORDER

# Row 41: SUMA DE PESOS DE CRITERIOS EVALUADOS EN LA TAREA (Dinámico según las 'X')
row_weight = 41
ws_mat.row_dimensions[row_weight].height = 26
ws_mat.merge_cells(f"A{row_weight}:G{row_weight}")
ws_mat[f"A{row_weight}"] = "SUMA DE CRITERIOS EVALUADOS EN ESTA TAREA (Suma Directa con 'X')"
ws_mat[f"A{row_weight}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_weight}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_weight}"].fill = FILL_HIGHLIGHT
ws_mat[f"A{row_weight}"].border = TOTAL_BORDER

for t_i in range(12):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_w = ws_mat.cell(row=row_weight, column=col_t)
    # SUMIF: Sum the CE global weights from col T where that task has an "X"
    c_w.value = f'=SUMIF({col_let}$6:{col_let}$39, "X", $T$6:$T$39)'
    c_w.font = Font(name="Segoe UI", size=9, bold=True, color="065F46")
    c_w.alignment = ALIGN_CENTER
    c_w.fill = FILL_HIGHLIGHT
    c_w.border = TOTAL_BORDER
    c_w.number_format = "0.00%"

c_w_sum = ws_mat.cell(row=row_weight, column=20)
c_w_sum.value = f"=SUM(H{row_weight}:S{row_weight})"
c_w_sum.font = FONT_BODY_BOLD
c_w_sum.alignment = ALIGN_CENTER
c_w_sum.fill = FILL_HIGHLIGHT
c_w_sum.border = TOTAL_BORDER
c_w_sum.number_format = "0.00%"

# Row 42: % PONDERACIÓN EN EL TRIMESTRE (Normalizado a 100% de T1 / T2 / T3)
row_norm = 42
ws_mat.row_dimensions[row_norm].height = 26
ws_mat.merge_cells(f"A{row_norm}:G{row_norm}")
ws_mat[f"A{row_norm}"] = "% PONDERACIÓN EN EL TRIMESTRE (Normalizado a 100% para boletín de notas)"
ws_mat[f"A{row_norm}"].font = FONT_HEADER_DARK
ws_mat[f"A{row_norm}"].alignment = ALIGN_RIGHT
ws_mat[f"A{row_norm}"].fill = FILL_GREEN_LIGHT
ws_mat[f"A{row_norm}"].border = TOTAL_BORDER

for t_i in range(12):
    col_t = 8 + t_i
    col_let = get_column_letter(col_t)
    c_norm = ws_mat.cell(row=row_norm, column=col_t)
    if t_i < 4:    # T1: T01 to T04 (Cols H to K)
        c_norm.value = f'=IF(SUM($H${row_weight}:$K${row_weight})=0, 0, {col_let}${row_weight} / SUM($H${row_weight}:$K${row_weight}))'
    elif t_i < 8:  # T2: T05 to T08 (Cols L to O)
        c_norm.value = f'=IF(SUM($L${row_weight}:$O${row_weight})=0, 0, {col_let}${row_weight} / SUM($L${row_weight}:$O${row_weight}))'
    else:          # T3: T09 to T12 (Cols P to S)
        c_norm.value = f'=IF(SUM($P${row_weight}:$S${row_weight})=0, 0, {col_let}${row_weight} / SUM($P${row_weight}:$S${row_weight}))'
    c_norm.font = Font(name="Segoe UI", size=9, bold=True, color="15803D")
    c_norm.alignment = ALIGN_CENTER
    c_norm.fill = FILL_GREEN_LIGHT
    c_norm.border = TOTAL_BORDER
    c_norm.number_format = "0.00%"

c_norm_sum = ws_mat.cell(row=row_norm, column=20)
c_norm_sum.value = "100% T1/T2/T3"
c_norm_sum.font = Font(name="Segoe UI", size=8, bold=True, color="15803D")
c_norm_sum.alignment = ALIGN_CENTER
c_norm_sum.fill = FILL_GREEN_LIGHT
c_norm_sum.border = TOTAL_BORDER

# Conditional Formatting on Matrix
ws_mat.conditional_formatting.add("G6:G39", CellIsRule(operator="equal", formula=['"EVALUADO"'], stopIfTrue=True, fill=FILL_GREEN_LIGHT, font=Font(color="15803D", bold=True)))
ws_mat.conditional_formatting.add("G6:G39", CellIsRule(operator="equal", formula=['"SIN EVALUAR"'], stopIfTrue=True, fill=PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid"), font=Font(color="DC2626", bold=True)))
ws_mat.conditional_formatting.add("H6:S39", CellIsRule(operator="equal", formula=['"X"'], stopIfTrue=True, fill=FILL_EMERALD_LIGHT, font=Font(color="065F46", bold=True)))


# =============================================================
# SHEET 2: REGISTRO DE NOTAS (CALIFICADOR POR TAREAS)
# =============================================================
ws_reg = wb.create_sheet(title="Registro Notas")
ws_reg.views.sheetView[0].showGridLines = True

# Title
ws_reg.merge_cells("A1:S1")
ws_reg["A1"] = "REGISTRO DE CALIFICACIONES POR TAREA — SOSTENIBILIDAD (1º DAW / DAM)"
ws_reg["A1"].font = FONT_TITLE
ws_reg["A1"].fill = FILL_NAVY
ws_reg["A1"].alignment = ALIGN_CENTER
ws_reg.row_dimensions[1].height = 36

ws_reg.merge_cells("A2:S2")
ws_reg["A2"] = "Introduce las notas obtenidas (0 a 10). Las columnas trimestrales y finales calculan los resultados con los pesos derivados dinámicamente de 'Matriz Criterios'."
ws_reg["A2"].font = FONT_SUBTITLE
ws_reg["A2"].fill = FILL_SUBHEADER
ws_reg["A2"].alignment = ALIGN_CENTER
ws_reg.row_dimensions[2].height = 20

# Subgroups headers (Row 4)
ws_reg.merge_cells("A4:C4")
ws_reg["A4"] = "DATOS DEL ALUMNADO"
ws_reg["A4"].font = FONT_HEADER
ws_reg["A4"].alignment = ALIGN_CENTER
ws_reg["A4"].fill = FILL_NAVY

ws_reg.merge_cells("D4:G4")
ws_reg["D4"] = "1er TRIMESTRE (T1)"
ws_reg["D4"].font = FONT_HEADER
ws_reg["D4"].alignment = ALIGN_CENTER
ws_reg["D4"].fill = FILL_EMERALD_HEADER

ws_reg.merge_cells("H4:K4")
ws_reg["H4"] = "2º TRIMESTRE (T2)"
ws_reg["H4"].font = FONT_HEADER
ws_reg["H4"].alignment = ALIGN_CENTER
ws_reg["H4"].fill = FILL_TEAL_HEADER

ws_reg.merge_cells("L4:O4")
ws_reg["L4"] = "3er TRIMESTRE (T3)"
ws_reg["L4"].font = FONT_HEADER
ws_reg["L4"].alignment = ALIGN_CENTER
ws_reg["L4"].fill = FILL_BLUE_HEADER

ws_reg.merge_cells("P4:S4")
ws_reg["P4"] = "CALIFICACIONES TRIMESTRALES Y MEDIA"
ws_reg["P4"].font = FONT_HEADER
ws_reg["P4"].alignment = ALIGN_CENTER
ws_reg["P4"].fill = FILL_PURPLE_HEADER

# Row 5: Column headers
reg_cols = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("Grupo", 8),
    # T01 to T04 (T1)
    ("T01\nFundam. ASG", 12),
    ("T02\nRetos TIC", 12),
    ("T03\nProy. Mapa", 13),
    ("T04\nDebate T1", 11),
    # T05 to T08 (T2)
    ("T05\nCircularidad", 12),
    ("T06\nGreen IT", 12),
    ("T07\nProy. Ecodiseño", 13),
    ("T08\nRigor T2", 11),
    # T09 to T12 (T3)
    ("T09\nReporte GRI", 12),
    ("T10\nKPIs PUE", 12),
    ("T11\nPlan CSRD", 13),
    ("T12\nDual & Ética", 11),
    # Trimester totals
    ("1º TRIMESTRE\n(100% T1)", 14),
    ("2º TRIMESTRE\n(100% T2)", 14),
    ("3er TRIMESTRE\n(100% T3)", 14),
    ("MEDIA CONTINUA\n(Trimestres)", 15)
]

ws_reg.row_dimensions[5].height = 36
for col_idx, (col_name, width) in enumerate(reg_cols, start=1):
    col_let = get_column_letter(col_idx)
    ws_reg.column_dimensions[col_let].width = width
    cell = ws_reg.cell(row=5, column=col_idx, value=col_name)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 3:
        cell.fill = FILL_NAVY
    elif col_idx <= 7:
        cell.fill = FILL_EMERALD_HEADER
    elif col_idx <= 11:
        cell.fill = FILL_TEAL_HEADER
    elif col_idx <= 15:
        cell.fill = FILL_BLUE_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

# Student rows (Rows 6 to 20)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_reg.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº
    c1 = ws_reg.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    # Nombre
    c2 = ws_reg.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Grupo
    c3 = ws_reg.cell(row=r_idx, column=3, value="1º DAW/M")
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = row_fill
    c3.font = FONT_BODY
    
    # Grades for 12 tasks (Cols D to O, index 4 to 15)
    grades = STUDENT_TASK_GRADES[r_idx-6]
    for g_i, grade_val in enumerate(grades):
        c_task = ws_reg.cell(row=r_idx, column=4 + g_i, value=grade_val)
        c_task.alignment = ALIGN_CENTER
        c_task.border = CELL_BORDER
        c_task.fill = row_fill
        c_task.font = FONT_BODY
        c_task.number_format = "0.00"
        
    # Col P: NOTA 1º TRIMESTRE (T1) -> dynamically uses weights from 'Matriz Criterios'!H$42:K$42
    cP = ws_reg.cell(row=r_idx, column=16)
    cP.value = f"=D{r_idx}*'Matriz Criterios'!H$42 + E{r_idx}*'Matriz Criterios'!I$42 + F{r_idx}*'Matriz Criterios'!J$42 + G{r_idx}*'Matriz Criterios'!K$42"
    cP.alignment = ALIGN_CENTER
    cP.border = CELL_BORDER
    cP.fill = FILL_EMERALD_LIGHT
    cP.font = FONT_BODY_BOLD
    cP.number_format = "0.00"
    
    # Col Q: NOTA 2º TRIMESTRE (T2) -> dynamically uses weights from 'Matriz Criterios'!L$42:O$42
    cQ = ws_reg.cell(row=r_idx, column=17)
    cQ.value = f"=H{r_idx}*'Matriz Criterios'!L$42 + I{r_idx}*'Matriz Criterios'!M$42 + J{r_idx}*'Matriz Criterios'!N$42 + K{r_idx}*'Matriz Criterios'!O$42"
    cQ.alignment = ALIGN_CENTER
    cQ.border = CELL_BORDER
    cQ.fill = FILL_TEAL_LIGHT
    cQ.font = FONT_BODY_BOLD
    cQ.number_format = "0.00"

    # Col R: NOTA 3er TRIMESTRE (T3) -> dynamically uses weights from 'Matriz Criterios'!P$42:S$42
    cR = ws_reg.cell(row=r_idx, column=18)
    cR.value = f"=L{r_idx}*'Matriz Criterios'!P$42 + M{r_idx}*'Matriz Criterios'!Q$42 + N{r_idx}*'Matriz Criterios'!R$42 + O{r_idx}*'Matriz Criterios'!S$42"
    cR.alignment = ALIGN_CENTER
    cR.border = CELL_BORDER
    cR.fill = FILL_BLUE_LIGHT
    cR.font = FONT_BODY_BOLD
    cR.number_format = "0.00"
    
    # Col S: MEDIA CONTINUA TRIMESTRES
    cS = ws_reg.cell(row=r_idx, column=19)
    cS.value = f"=AVERAGE(P{r_idx}, Q{r_idx}, R{r_idx})"
    cS.alignment = ALIGN_CENTER
    cS.border = CELL_BORDER
    cS.fill = FILL_TOTAL
    cS.font = FONT_BODY_BOLD
    cS.number_format = "0.00"

# Average row for Tasks (Row 21)
row_reg_avg = 21
ws_reg.row_dimensions[row_reg_avg].height = 24
ws_reg.merge_cells(f"A{row_reg_avg}:C{row_reg_avg}")
c_avg_lbl = ws_reg.cell(row=row_reg_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl.font = FONT_HEADER_DARK
c_avg_lbl.alignment = ALIGN_CENTER
c_avg_lbl.fill = FILL_TOTAL
c_avg_lbl.border = TOTAL_BORDER
ws_reg.cell(row=row_reg_avg, column=2).border = TOTAL_BORDER
ws_reg.cell(row=row_reg_avg, column=3).border = TOTAL_BORDER

for col_idx in range(4, 20):
    col_let = get_column_letter(col_idx)
    c_avg = ws_reg.cell(row=row_reg_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

# Conditional formatting on Trimester notes
green_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
green_font = Font(color="15803D", bold=True)
red_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
red_font = Font(color="DC2626", bold=True)

ws_reg.conditional_formatting.add("P6:S20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_reg.conditional_formatting.add("P6:S20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 3: CÁLCULO POR CRITERIOS (CEs) — AUTOMATIZACIÓN TOTAL
# =============================================================
ws_ces = wb.create_sheet(title="Calculo CEs")
ws_ces.views.sheetView[0].showGridLines = True

# Title
ws_ces.merge_cells("A1:AL1")
ws_ces["A1"] = "CALIFICACIÓN DETALLADA POR CRITERIOS DE EVALUACIÓN (CE1.a a CE6.e) — SOSTENIBILIDAD"
ws_ces["A1"].font = FONT_TITLE
ws_ces["A1"].fill = FILL_NAVY
ws_ces["A1"].alignment = ALIGN_CENTER
ws_ces.row_dimensions[1].height = 36

ws_ces.merge_cells("A2:AL2")
ws_ces["A2"] = "Cálculo matemático automático: cada criterio se calcula promediando exclusivamente las tareas donde tiene marcada una 'X' en la 'Matriz Criterios'."
ws_ces["A2"].font = FONT_SUBTITLE
ws_ces["A2"].fill = FILL_SUBHEADER
ws_ces["A2"].alignment = ALIGN_CENTER
ws_ces.row_dimensions[2].height = 20

# Header groups (Row 4)
ws_ces.merge_cells("A4:B4")
ws_ces["A4"] = "ALUMNADO"
ws_ces["A4"].font = FONT_HEADER
ws_ces["A4"].alignment = ALIGN_CENTER
ws_ces["A4"].fill = FILL_NAVY

# 6 RA groups across the 34 CEs:
# RA1: cols C to H (6 CEs, idx 3 to 8)
ws_ces.merge_cells("C4:H4")
ws_ces["C4"] = "RA1 (18%) — Aspectos ASG, Desarrollo Sostenible y Marcos Internacionales"
ws_ces["C4"].font = FONT_HEADER
ws_ces["C4"].alignment = ALIGN_CENTER
ws_ces["C4"].fill = FILL_EMERALD_HEADER

# RA2: cols I to M (5 CEs, idx 9 to 13)
ws_ces.merge_cells("I4:M4")
ws_ces["I4"] = "RA2 (15%) — Retos Ambientales y Sociales en el Sector TIC"
ws_ces["I4"].font = FONT_HEADER
ws_ces["I4"].alignment = ALIGN_CENTER
ws_ces["I4"].fill = FILL_TEAL_HEADER

# RA3: cols N to P (3 CEs, idx 14 to 16)
ws_ces.merge_cells("N4:P4")
ws_ces["N4"] = "RA3 (9%) — Criterios Personales y Profesionales"
ws_ces["N4"].font = FONT_HEADER
ws_ces["N4"].alignment = ALIGN_CENTER
ws_ces["N4"].fill = FILL_PURPLE_HEADER

# RA4: cols Q to V (6 CEs, idx 17 to 22)
ws_ces.merge_cells("Q4:V4")
ws_ces["Q4"] = "RA4 (18%) — Economía Circular y Ecodiseño TIC"
ws_ces["Q4"].font = FONT_HEADER
ws_ces["Q4"].alignment = ALIGN_CENTER
ws_ces["Q4"].fill = FILL_AMBER_HEADER

# RA5: cols W to AE (9 CEs, idx 23 to 31)
ws_ces.merge_cells("W4:AE4")
ws_ces["W4"] = "RA5 (18%) — Actividades Sostenibles, Green IT y Normativa RAEE"
ws_ces["W4"].font = FONT_HEADER
ws_ces["W4"].alignment = ALIGN_CENTER
ws_ces["W4"].fill = FILL_GREEN_HEADER

# RA6: cols AF to AJ (5 CEs, idx 32 to 36)
ws_ces.merge_cells("AF4:AJ4")
ws_ces["AF4"] = "RA6 (22%) — Plan de Sostenibilidad e Informe CSRD/GRI"
ws_ces["AF4"].font = FONT_HEADER
ws_ces["AF4"].alignment = ALIGN_CENTER
ws_ces["AF4"].fill = FILL_BLUE_HEADER

# Summary of CEs
ws_ces.merge_cells("AK4:AL4")
ws_ces["AK4"] = "RESUMEN DE CRITERIOS"
ws_ces["AK4"].font = FONT_HEADER
ws_ces["AK4"].alignment = ALIGN_CENTER
ws_ces["AK4"].fill = FILL_NAVY

# Row 5: Column headers with CE codes
ws_ces.column_dimensions["A"].width = 5
ws_ces.cell(row=5, column=1, value="Nº").font = FONT_HEADER
ws_ces.cell(row=5, column=1).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=1).fill = FILL_NAVY
ws_ces.cell(row=5, column=1).border = HEADER_BORDER

ws_ces.column_dimensions["B"].width = 24
ws_ces.cell(row=5, column=2, value="Apellidos, Nombre").font = FONT_HEADER
ws_ces.cell(row=5, column=2).alignment = ALIGN_LEFT
ws_ces.cell(row=5, column=2).fill = FILL_NAVY
ws_ces.cell(row=5, column=2).border = HEADER_BORDER

ws_ces.row_dimensions[5].height = 30
for c_i, crit in enumerate(CRITERIA_DATA, start=3):
    col_let = get_column_letter(c_i)
    ws_ces.column_dimensions[col_let].width = 9
    cell = ws_ces.cell(row=5, column=c_i, value=crit[2])
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    ra_code = crit[0]
    if ra_code == "RA1":
        cell.fill = FILL_EMERALD_HEADER
    elif ra_code == "RA2":
        cell.fill = FILL_TEAL_HEADER
    elif ra_code == "RA3":
        cell.fill = FILL_PURPLE_HEADER
    elif ra_code == "RA4":
        cell.fill = FILL_AMBER_HEADER
    elif ra_code == "RA5":
        cell.fill = FILL_GREEN_HEADER
    else:
        cell.fill = FILL_BLUE_HEADER

ws_ces.column_dimensions["AK"].width = 12
ws_ces.cell(row=5, column=37, value="Media CEs\nSuperados").font = FONT_HEADER
ws_ces.cell(row=5, column=37).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=37).fill = FILL_NAVY
ws_ces.cell(row=5, column=37).border = HEADER_BORDER

ws_ces.column_dimensions["AL"].width = 12
ws_ces.cell(row=5, column=38, value="Nº CEs >= 5\n(de 34)").font = FONT_HEADER
ws_ces.cell(row=5, column=38).alignment = ALIGN_CENTER
ws_ces.cell(row=5, column=38).fill = FILL_NAVY
ws_ces.cell(row=5, column=38).border = HEADER_BORDER

# Student rows (Rows 6 to 20 in Calculo CEs)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_ces.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº & Nombre
    c1 = ws_ces.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_ces.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    for c_i in range(34):
        target_col = 3 + c_i
        mat_row = 6 + c_i
        cell_ce = ws_ces.cell(row=r_idx, column=target_col)
        
        # Dynamic formula averaging tasks where 'Matriz Criterios' has "X"
        formula = f'=IF(SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$S${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$O{r_idx}))=0, "-", SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$S${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$O{r_idx})*\'Registro Notas\'!$D{r_idx}:$O{r_idx})/SUMPRODUCT((\'Matriz Criterios\'!$H${mat_row}:$S${mat_row}="X")*ISNUMBER(\'Registro Notas\'!$D{r_idx}:$O{r_idx})))'
        cell_ce.value = formula
        cell_ce.alignment = ALIGN_CENTER
        cell_ce.border = CELL_BORDER
        cell_ce.fill = row_fill
        cell_ce.font = FONT_BODY
        cell_ce.number_format = "0.00"
        
    # Col AK: Media CEs Superados
    cAK = ws_ces.cell(row=r_idx, column=37)
    cAK.value = f"=AVERAGE(C{r_idx}:AJ{r_idx})"
    cAK.alignment = ALIGN_CENTER
    cAK.border = CELL_BORDER
    cAK.fill = FILL_TOTAL
    cAK.font = FONT_BODY_BOLD
    cAK.number_format = "0.00"
    
    # Col AL: Nº CEs >= 5
    cAL = ws_ces.cell(row=r_idx, column=38)
    cAL.value = f'=COUNTIF(C{r_idx}:AJ{r_idx}, ">=5")'
    cAL.alignment = ALIGN_CENTER
    cAL.border = CELL_BORDER
    cAL.fill = FILL_GREEN_LIGHT
    cAL.font = FONT_BODY_BOLD

# Group Average Row
row_ce_avg = 21
ws_ces.row_dimensions[row_ce_avg].height = 24
ws_ces.merge_cells(f"A{row_ce_avg}:B{row_ce_avg}")
c_avg_lbl_ce = ws_ces.cell(row=row_ce_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_ce.font = FONT_HEADER_DARK
c_avg_lbl_ce.alignment = ALIGN_CENTER
c_avg_lbl_ce.fill = FILL_TOTAL
c_avg_lbl_ce.border = TOTAL_BORDER
ws_ces.cell(row=row_ce_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 39):
    col_let = get_column_letter(col_idx)
    c_avg = ws_ces.cell(row=row_ce_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_ces.conditional_formatting.add("C6:AJ20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_ces.conditional_formatting.add("C6:AJ20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 4: CÁLCULO POR RESULTADOS DE APRENDIZAJE (RAs)
# =============================================================
ws_ras = wb.create_sheet(title="Calculo RAs")
ws_ras.views.sheetView[0].showGridLines = True

ws_ras.merge_cells("A1:I1")
ws_ras["A1"] = "CALIFICACIÓN POR RESULTADOS DE APRENDIZAJE (RA1 a RA6) — PONDERACIÓN OFICIAL"
ws_ras["A1"].font = FONT_TITLE
ws_ras["A1"].fill = FILL_NAVY
ws_ras["A1"].alignment = ALIGN_CENTER
ws_ras.row_dimensions[1].height = 36

ws_ras.merge_cells("A2:I2")
ws_ras["A2"] = "Cada Resultado de Aprendizaje se obtiene promediando sus Criterios de Evaluación. La Nota Final aplica los pesos oficiales del RD 659/2023."
ws_ras["A2"].font = FONT_SUBTITLE
ws_ras["A2"].fill = FILL_SUBHEADER
ws_ras["A2"].alignment = ALIGN_CENTER
ws_ras.row_dimensions[2].height = 20

headers_ras = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("RA1 (18%)\nAspectos ASG &\nMarcos Internac.", 16),
    ("RA2 (15%)\nRetos Ambientales\ny Sociales TIC", 16),
    ("RA3 (9%)\nCriterios Personales\ny Profesionales", 16),
    ("RA4 (18%)\nEconomía Circular\ny Ecodiseño TIC", 16),
    ("RA5 (18%)\nActividades Sostenibles\nGreen IT & RAEE", 16),
    ("RA6 (22%)\nPlan Sostenibilidad\ne Informe CSRD/GRI", 16),
    ("CALIFICACIÓN FINAL\nORDINARIA (100%)", 18)
]

ws_ras.row_dimensions[4].height = 42
for col_idx, (h_text, width) in enumerate(headers_ras, start=1):
    col_let = get_column_letter(col_idx)
    ws_ras.column_dimensions[col_let].width = width
    cell = ws_ras.cell(row=4, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 8:
        cell.fill = FILL_EMERALD_HEADER
    else:
        cell.fill = FILL_GREEN_HEADER

# Fill Student Rows for RAs
for r_idx, (apell, nom) in enumerate(STUDENTS, start=6):
    ws_ras.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    
    # Nº & Nombre
    c1 = ws_ras.cell(row=r_idx, column=1, value=r_idx-5)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_ras.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # RA1 (18%): CE1.a to CE1.f -> 'Calculo CEs'!C{r_idx}:H{r_idx}
    c_ra1 = ws_ras.cell(row=r_idx, column=3)
    c_ra1.value = f"=AVERAGE('Calculo CEs'!C{r_idx}:H{r_idx})"
    c_ra1.alignment = ALIGN_CENTER
    c_ra1.border = CELL_BORDER
    c_ra1.fill = row_fill
    c_ra1.font = FONT_BODY
    c_ra1.number_format = "0.00"
    
    # RA2 (15%): CE2.a to CE2.e -> 'Calculo CEs'!I{r_idx}:M{r_idx}
    c_ra2 = ws_ras.cell(row=r_idx, column=4)
    c_ra2.value = f"=AVERAGE('Calculo CEs'!I{r_idx}:M{r_idx})"
    c_ra2.alignment = ALIGN_CENTER
    c_ra2.border = CELL_BORDER
    c_ra2.fill = row_fill
    c_ra2.font = FONT_BODY
    c_ra2.number_format = "0.00"
    
    # RA3 (9%): CE3.a to CE3.c -> 'Calculo CEs'!N{r_idx}:P{r_idx}
    c_ra3 = ws_ras.cell(row=r_idx, column=5)
    c_ra3.value = f"=AVERAGE('Calculo CEs'!N{r_idx}:P{r_idx})"
    c_ra3.alignment = ALIGN_CENTER
    c_ra3.border = CELL_BORDER
    c_ra3.fill = row_fill
    c_ra3.font = FONT_BODY
    c_ra3.number_format = "0.00"
    
    # RA4 (18%): CE4.a to CE4.f -> 'Calculo CEs'!Q{r_idx}:V{r_idx}
    c_ra4 = ws_ras.cell(row=r_idx, column=6)
    c_ra4.value = f"=AVERAGE('Calculo CEs'!Q{r_idx}:V{r_idx})"
    c_ra4.alignment = ALIGN_CENTER
    c_ra4.border = CELL_BORDER
    c_ra4.fill = row_fill
    c_ra4.font = FONT_BODY
    c_ra4.number_format = "0.00"
    
    # RA5 (18%): CE5.a to CE5.i -> 'Calculo CEs'!W{r_idx}:AE{r_idx}
    c_ra5 = ws_ras.cell(row=r_idx, column=7)
    c_ra5.value = f"=AVERAGE('Calculo CEs'!W{r_idx}:AE{r_idx})"
    c_ra5.alignment = ALIGN_CENTER
    c_ra5.border = CELL_BORDER
    c_ra5.fill = row_fill
    c_ra5.font = FONT_BODY
    c_ra5.number_format = "0.00"
    
    # RA6 (22%): CE6.a to CE6.e -> 'Calculo CEs'!AF{r_idx}:AJ{r_idx}
    c_ra6 = ws_ras.cell(row=r_idx, column=8)
    c_ra6.value = f"=AVERAGE('Calculo CEs'!AF{r_idx}:AJ{r_idx})"
    c_ra6.alignment = ALIGN_CENTER
    c_ra6.border = CELL_BORDER
    c_ra6.fill = row_fill
    c_ra6.font = FONT_BODY
    c_ra6.number_format = "0.00"
    
    # Calificacion Final Ordinaria Oficial Sostenibilidad (18% + 15% + 9% + 18% + 18% + 22% = 100%)
    c_tot = ws_ras.cell(row=r_idx, column=9)
    c_tot.value = f"=C{r_idx}*0.18 + D{r_idx}*0.15 + E{r_idx}*0.09 + F{r_idx}*0.18 + G{r_idx}*0.18 + H{r_idx}*0.22"
    c_tot.alignment = ALIGN_CENTER
    c_tot.border = CELL_BORDER
    c_tot.fill = FILL_TOTAL
    c_tot.font = Font(name="Segoe UI", size=10, bold=True, color="064E3B")
    c_tot.number_format = "0.00"

# Average Row
row_ras_avg = 21
ws_ras.row_dimensions[row_ras_avg].height = 24
ws_ras.merge_cells(f"A{row_ras_avg}:B{row_ras_avg}")
c_avg_lbl_ras = ws_ras.cell(row=row_ras_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_ras.font = FONT_HEADER_DARK
c_avg_lbl_ras.alignment = ALIGN_CENTER
c_avg_lbl_ras.fill = FILL_TOTAL
c_avg_lbl_ras.border = TOTAL_BORDER
ws_ras.cell(row=row_ras_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 10):
    col_let = get_column_letter(col_idx)
    c_avg = ws_ras.cell(row=row_ras_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}6:{col_let}20)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_ras.conditional_formatting.add("I6:I20", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_ras.conditional_formatting.add("I6:I20", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 5: PANEL DE CONTROL Y RESUMEN EJECUTIVO
# =============================================================
ws_dash = wb.create_sheet(title="Panel de Control")
ws_dash.views.sheetView[0].showGridLines = True

# Title Header
ws_dash.merge_cells("A1:O1")
ws_dash["A1"] = "PANEL DE CONTROL GENERAL — SOSTENIBILIDAD APLICADA (1º DAW / DAM)"
ws_dash["A1"].font = FONT_TITLE
ws_dash["A1"].fill = FILL_NAVY
ws_dash["A1"].alignment = ALIGN_CENTER
ws_dash.row_dimensions[1].height = 36

ws_dash.merge_cells("A2:O2")
ws_dash["A2"] = "Síntesis Integral: 3 Trimestres (T1, T2, T3), Resultados de Aprendizaje Oficiales (RA1-RA6) y Calificación Ordinaria"
ws_dash["A2"].font = FONT_SUBTITLE
ws_dash["A2"].fill = FILL_SUBHEADER
ws_dash["A2"].alignment = ALIGN_CENTER
ws_dash.row_dimensions[2].height = 20

# Top KPI Cards (Rows 4 to 6)
ws_dash.merge_cells("B4:C4")
ws_dash["B4"] = "ALUMNADO MATRICULADO"
ws_dash["B4"].font = FONT_KPI_LBL
ws_dash["B4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("B5:C6")
ws_dash["B5"] = '=COUNTA(A9:A23)'
ws_dash["B5"].font = FONT_KPI_VAL
ws_dash["B5"].alignment = ALIGN_CENTER
ws_dash["B5"].fill = FILL_EMERALD_LIGHT

ws_dash.merge_cells("E4:F4")
ws_dash["E4"] = "APROBADOS EVAL. ORDINARIA"
ws_dash["E4"].font = FONT_KPI_LBL
ws_dash["E4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("E5:F6")
ws_dash["E5"] = '=COUNTIF(M9:M23, ">=5")'
ws_dash["E5"].font = Font(name="Segoe UI", size=16, bold=True, color="15803D")
ws_dash["E5"].alignment = ALIGN_CENTER
ws_dash["E5"].fill = FILL_GREEN_LIGHT

ws_dash.merge_cells("H4:I4")
ws_dash["H4"] = "SUSPENSOS EVAL. ORDINARIA"
ws_dash["H4"].font = FONT_KPI_LBL
ws_dash["H4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("H5:I6")
ws_dash["H5"] = '=COUNTIF(M9:M23, "<5")'
ws_dash["H5"].font = Font(name="Segoe UI", size=16, bold=True, color="DC2626")
ws_dash["H5"].alignment = ALIGN_CENTER
ws_dash["H5"].fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")

ws_dash.merge_cells("K4:L4")
ws_dash["K4"] = "NOTA MEDIA DEL GRUPO"
ws_dash["K4"].font = FONT_KPI_LBL
ws_dash["K4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("K5:L6")
ws_dash["K5"] = '=AVERAGE(M9:M23)'
ws_dash["K5"].font = FONT_KPI_VAL
ws_dash["K5"].alignment = ALIGN_CENTER
ws_dash["K5"].fill = FILL_TOTAL
ws_dash["K5"].number_format = "0.00"

ws_dash.merge_cells("N4:O4")
ws_dash["N4"] = "TASA DE ÉXITO ACADÉMICO"
ws_dash["N4"].font = FONT_KPI_LBL
ws_dash["N4"].alignment = ALIGN_CENTER
ws_dash.merge_cells("N5:O6")
ws_dash["N5"] = '=E5/B5'
ws_dash["N5"].font = Font(name="Segoe UI", size=16, bold=True, color="065F46")
ws_dash["N5"].alignment = ALIGN_CENTER
ws_dash["N5"].fill = FILL_TEAL_LIGHT
ws_dash["N5"].number_format = "0.0%"

# Table Headers (Row 8)
headers_dash = [
    ("Nº", 5),
    ("Apellidos, Nombre", 24),
    ("1º Trim\n(T1)", 9),
    ("2º Trim\n(T2)", 9),
    ("3º Trim\n(T3)", 9),
    ("RA1\n(18%)", 8),
    ("RA2\n(15%)", 8),
    ("RA3\n(9%)", 8),
    ("RA4\n(18%)", 8),
    ("RA5\n(18%)", 8),
    ("RA6\n(22%)", 8),
    ("Media\nT1-T3", 9),
    ("Nota Final\nOrdinaria (Mayo)", 16),
    ("Calificación Cualitativa", 18),
    ("Estado de Superación", 22)
]

ws_dash.row_dimensions[8].height = 40
for col_idx, (h_text, width) in enumerate(headers_dash, start=1):
    col_let = get_column_letter(col_idx)
    ws_dash.column_dimensions[col_let].width = width
    cell = ws_dash.cell(row=8, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 5:
        cell.fill = FILL_TEAL_HEADER
    elif col_idx <= 11:
        cell.fill = FILL_EMERALD_HEADER
    elif col_idx <= 13:
        cell.fill = FILL_GREEN_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

# Student rows (Rows 9 to 23 in Panel de Control)
for r_idx, (apell, nom) in enumerate(STUDENTS, start=9):
    ws_dash.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    src_row = r_idx - 3  # Maps row 9 to row 6 in other sheets
    
    # Nº & Nombre
    c1 = ws_dash.cell(row=r_idx, column=1, value=r_idx-8)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_dash.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # 1º Trimestre (from 'Registro Notas'!P{src_row})
    c3 = ws_dash.cell(row=r_idx, column=3)
    c3.value = f"='Registro Notas'!P{src_row}"
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = FILL_EMERALD_LIGHT if is_zebra else PatternFill(start_color="ECFDF5", end_color="ECFDF5", fill_type="solid")
    c3.font = FONT_BODY_BOLD
    c3.number_format = "0.00"
    
    # 2º Trimestre (from 'Registro Notas'!Q{src_row})
    c4 = ws_dash.cell(row=r_idx, column=4)
    c4.value = f"='Registro Notas'!Q{src_row}"
    c4.alignment = ALIGN_CENTER
    c4.border = CELL_BORDER
    c4.fill = FILL_TEAL_LIGHT if is_zebra else PatternFill(start_color="F0FDFA", end_color="F0FDFA", fill_type="solid")
    c4.font = FONT_BODY_BOLD
    c4.number_format = "0.00"

    # 3er Trimestre (from 'Registro Notas'!R{src_row})
    c5 = ws_dash.cell(row=r_idx, column=5)
    c5.value = f"='Registro Notas'!R{src_row}"
    c5.alignment = ALIGN_CENTER
    c5.border = CELL_BORDER
    c5.fill = FILL_BLUE_LIGHT if is_zebra else PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")
    c5.font = FONT_BODY_BOLD
    c5.number_format = "0.00"
    
    # RA1 to RA6 (from 'Calculo RAs'!C{src_row}:H{src_row})
    for ra_i in range(6):
        c_target = 6 + ra_i
        ra_col_let = get_column_letter(3 + ra_i)
        c_ra = ws_dash.cell(row=r_idx, column=c_target)
        c_ra.value = f"='Calculo RAs'!{ra_col_let}{src_row}"
        c_ra.alignment = ALIGN_CENTER
        c_ra.border = CELL_BORDER
        c_ra.fill = row_fill
        c_ra.font = FONT_BODY
        c_ra.number_format = "0.00"
        
    # Media T1-T3 (Col L, 12)
    c_med = ws_dash.cell(row=r_idx, column=12)
    c_med.value = f"=AVERAGE(C{r_idx}, D{r_idx}, E{r_idx})"
    c_med.alignment = ALIGN_CENTER
    c_med.border = CELL_BORDER
    c_med.fill = row_fill
    c_med.font = FONT_BODY
    c_med.number_format = "0.00"
    
    # Nota Final Ordinaria (from 'Calculo RAs'!I{src_row})
    c_fin = ws_dash.cell(row=r_idx, column=13)
    c_fin.value = f"='Calculo RAs'!I{src_row}"
    c_fin.alignment = ALIGN_CENTER
    c_fin.border = CELL_BORDER
    c_fin.fill = FILL_TOTAL
    c_fin.font = Font(name="Segoe UI", size=10, bold=True, color="064E3B")
    c_fin.number_format = "0.00"
    
    # Calificacion Cualitativa (Col N, 14)
    c_cual = ws_dash.cell(row=r_idx, column=14)
    c_cual.value = f'=IF(M{r_idx}>=9, "SOBRESALIENTE", IF(M{r_idx}>=7, "NOTABLE", IF(M{r_idx}>=6, "BIEN", IF(M{r_idx}>=5, "SUFICIENTE", "INSUFICIENTE"))))'
    c_cual.alignment = ALIGN_CENTER
    c_cual.border = CELL_BORDER
    c_cual.fill = row_fill
    c_cual.font = FONT_BODY_BOLD
    
    # Estado de Superacion (Col O, 15)
    c_est = ws_dash.cell(row=r_idx, column=15)
    c_est.value = f'=IF(M{r_idx}>=5, "SUPERADO", "PENDIENTE EXTRAORD.")'
    c_est.alignment = ALIGN_CENTER
    c_est.border = CELL_BORDER
    c_est.fill = row_fill
    c_est.font = FONT_BODY_BOLD

# Group Average Row
row_dash_avg = 24
ws_dash.row_dimensions[row_dash_avg].height = 24
ws_dash.merge_cells(f"A{row_dash_avg}:B{row_dash_avg}")
c_avg_lbl_d = ws_dash.cell(row=row_dash_avg, column=1, value="PROMEDIO DEL GRUPO")
c_avg_lbl_d.font = FONT_HEADER_DARK
c_avg_lbl_d.alignment = ALIGN_CENTER
c_avg_lbl_d.fill = FILL_TOTAL
c_avg_lbl_d.border = TOTAL_BORDER
ws_dash.cell(row=row_dash_avg, column=2).border = TOTAL_BORDER

for col_idx in range(3, 14):
    col_let = get_column_letter(col_idx)
    c_avg = ws_dash.cell(row=row_dash_avg, column=col_idx)
    c_avg.value = f"=AVERAGE({col_let}9:{col_let}23)"
    c_avg.font = FONT_BODY_BOLD
    c_avg.alignment = ALIGN_CENTER
    c_avg.fill = FILL_TOTAL
    c_avg.border = TOTAL_BORDER
    c_avg.number_format = "0.00"

ws_dash.cell(row=row_dash_avg, column=14, value="").fill = FILL_TOTAL
ws_dash.cell(row=row_dash_avg, column=14).border = TOTAL_BORDER
ws_dash.cell(row=row_dash_avg, column=15, value="").fill = FILL_TOTAL
ws_dash.cell(row=row_dash_avg, column=15).border = TOTAL_BORDER

ws_dash.conditional_formatting.add("M9:M23", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dash.conditional_formatting.add("M9:M23", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))
ws_dash.conditional_formatting.add("O9:O23", CellIsRule(operator="equal", formula=['"SUPERADO"'], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dash.conditional_formatting.add("O9:O23", CellIsRule(operator="equal", formula=['"PENDIENTE EXTRAORD."'], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 6: SEGUIMIENTO DUAL Y EXTRAORDINARIA
# =============================================================
ws_dual = wb.create_sheet(title="Seguimiento y Extraordinaria")
ws_dual.views.sheetView[0].showGridLines = True

ws_dual.merge_cells("A1:J1")
ws_dual["A1"] = "SEGUIMIENTO DE TRANSFERENCIA DUAL Y CONVOCATORIA EXTRAORDINARIA (1º DAW / DAM)"
ws_dual["A1"].font = FONT_TITLE
ws_dual["A1"].fill = FILL_NAVY
ws_dual["A1"].alignment = ALIGN_CENTER
ws_dual.row_dimensions[1].height = 36

ws_dual.merge_cells("A2:J2")
ws_dual["A2"] = "Vinculación ASG con la Empresa Colaboradora Dual y Registro de Recuperación en Convocatoria Extraordinaria de Junio"
ws_dual["A2"].font = FONT_SUBTITLE
ws_dual["A2"].fill = FILL_SUBHEADER
ws_dual["A2"].alignment = ALIGN_CENTER
ws_dual.row_dimensions[2].height = 20

headers_dual = [
    ("Nº", 5),
    ("Apellidos, Nombre", 25),
    ("Nota Ordinaria\n(Mayo)", 15),
    ("Empresa TIC Asignada", 22),
    ("Tutor/a Laboral", 20),
    ("Compromiso ASG Dual\n(Informe / Caso)", 18),
    ("Valoración Dual\n(Apto / Pendiente)", 18),
    ("RAs Pendientes\n(Extraordinaria)", 18),
    ("Nota Convocatoria\nExtraordinaria (Junio)", 20),
    ("Calificación Definitiva\nCurso Académico", 20)
]

ws_dual.row_dimensions[4].height = 38
for col_idx, (h_text, width) in enumerate(headers_dual, start=1):
    col_let = get_column_letter(col_idx)
    ws_dual.column_dimensions[col_let].width = width
    cell = ws_dual.cell(row=4, column=col_idx, value=h_text)
    cell.font = FONT_HEADER
    cell.alignment = ALIGN_CENTER
    cell.border = HEADER_BORDER
    if col_idx <= 2:
        cell.fill = FILL_NAVY
    elif col_idx <= 7:
        cell.fill = FILL_EMERALD_HEADER
    else:
        cell.fill = FILL_PURPLE_HEADER

for r_idx, (apell, nom) in enumerate(STUDENTS, start=5):
    ws_dual.row_dimensions[r_idx].height = 20
    is_zebra = (r_idx % 2 == 0)
    row_fill = FILL_ZEBRA if is_zebra else PatternFill(fill_type=None)
    dash_row = r_idx + 4  # Maps row 5 to row 9 in Dashboard
    
    # Nº & Nombre
    c1 = ws_dual.cell(row=r_idx, column=1, value=r_idx-4)
    c1.alignment = ALIGN_CENTER
    c1.border = CELL_BORDER
    c1.fill = row_fill
    c1.font = FONT_BODY
    
    c2 = ws_dual.cell(row=r_idx, column=2, value=f"{apell}, {nom}")
    c2.alignment = ALIGN_LEFT
    c2.border = CELL_BORDER
    c2.fill = row_fill
    c2.font = FONT_BODY_BOLD
    
    # Nota Ordinaria (Pulled from Dashboard Col M)
    c3 = ws_dual.cell(row=r_idx, column=3)
    c3.value = f"='Panel de Control'!M{dash_row}"
    c3.alignment = ALIGN_CENTER
    c3.border = CELL_BORDER
    c3.fill = FILL_TOTAL
    c3.font = FONT_BODY_BOLD
    c3.number_format = "0.00"
    
    # Empresa
    c4 = ws_dual.cell(row=r_idx, column=4, value="GreenCloud Solutions S.L." if r_idx % 2 == 0 else "EcoSoftware Andalucía")
    c4.alignment = ALIGN_LEFT
    c4.border = CELL_BORDER
    c4.fill = row_fill
    c4.font = FONT_BODY
    
    # Tutor
    c5 = ws_dual.cell(row=r_idx, column=5, value="Ing. Cristina Morales" if r_idx % 2 == 0 else "D. Jorge Cazorla")
    c5.alignment = ALIGN_LEFT
    c5.border = CELL_BORDER
    c5.fill = row_fill
    c5.font = FONT_BODY
    
    # Compromiso ASG
    c6 = ws_dual.cell(row=r_idx, column=6, value="Auditoría RAEE / PUE")
    c6.alignment = ALIGN_CENTER
    c6.border = CELL_BORDER
    c6.fill = row_fill
    c6.font = FONT_BODY
    
    # Valoración
    c7 = ws_dual.cell(row=r_idx, column=7)
    c7.value = f'=IF(C{r_idx}>=5, "APTO", "PENDIENTE")'
    c7.alignment = ALIGN_CENTER
    c7.border = CELL_BORDER
    c7.fill = row_fill
    c7.font = FONT_BODY_BOLD
    
    # RAs Pendientes
    c8 = ws_dual.cell(row=r_idx, column=8, value=f'=IF(C{r_idx}<5, "RA4, RA6", "Ninguno")')
    c8.alignment = ALIGN_CENTER
    c8.border = CELL_BORDER
    c8.fill = row_fill
    c8.font = FONT_BODY
    
    # Nota Extraordinaria
    c9 = ws_dual.cell(row=r_idx, column=9, value="")
    c9.alignment = ALIGN_CENTER
    c9.border = CELL_BORDER
    c9.fill = row_fill
    c9.font = FONT_BODY
    c9.number_format = "0.00"
    
    # Calificación Definitiva
    c10 = ws_dual.cell(row=r_idx, column=10)
    c10.value = f'=IF(ISBLANK(I{r_idx}), C{r_idx}, MAX(C{r_idx}, I{r_idx}))'
    c10.alignment = ALIGN_CENTER
    c10.border = CELL_BORDER
    c10.fill = FILL_GREEN_LIGHT
    c10.font = FONT_BODY_BOLD
    c10.number_format = "0.00"

ws_dual.conditional_formatting.add("J5:J19", CellIsRule(operator="greaterThanOrEqual", formula=["5.0"], stopIfTrue=True, fill=green_fill, font=green_font))
ws_dual.conditional_formatting.add("J5:J19", CellIsRule(operator="lessThan", formula=["5.0"], stopIfTrue=True, fill=red_fill, font=red_font))


# =============================================================
# SHEET 7: GUÍA DE FUNCIONAMIENTO INTERACTIVA
# =============================================================
ws_guide = wb.create_sheet(title="Guía de Funcionamiento")
ws_guide.views.sheetView[0].showGridLines = True

ws_guide.merge_cells("A1:G1")
ws_guide["A1"] = "GUÍA DE USO Y ARQUITECTURA DEL SISTEMA DE EVALUACIÓN — SOSTENIBILIDAD (1º DAW / DAM)"
ws_guide["A1"].font = FONT_TITLE
ws_guide["A1"].fill = FILL_NAVY
ws_guide["A1"].alignment = ALIGN_CENTER
ws_guide.row_dimensions[1].height = 36

guide_sections = [
    ("1. Filosofía y Funcionamiento Dinámico",
     "Esta hoja de cálculo implementa un motor de evaluación competencial bidireccional completamente automatizado para Sostenibilidad:\n"
     "• La 'Matriz Criterios' contiene los 34 Criterios de Evaluación oficiales agrupados en los 6 Resultados de Aprendizaje.\n"
     "• En cualquier momento del curso puedes marcar o desmarcar con una 'X' qué criterios evalúa cada tarea o examen.\n"
     "• En la FILA 41 se calcula automáticamente la SUMA EXACTA DE LOS PESOS de los criterios marcados con 'X' para esa tarea.\n"
     "• En la FILA 42 se calcula el % DE PONDERACIÓN EN EL TRIMESTRE, normalizado a 100% (para que cada boletín de notas trimestral sume 100%).\n"
     "• El motor recalcula en tiempo real las notas individuales de cada criterio, el avance de cada RA y las notas de T1, T2, T3 y final."),
    
    ("2. Flujo de Trabajo para el Docente",
     "PASO 1: Configurar la Matriz Criterios\n"
     "Revisa las columnas H a S (tareas T01 a T12 repartidas en los 3 trimestres). Coloca una 'X' en la fila del criterio que evalúe dicha tarea.\n"
     "La fila 40 te indica cuántos criterios evalúa cada tarea.\n"
     "La fila 41 calcula dinámicamente la suma directa de los pesos de dichos criterios sobre el total del módulo.\n"
     "La fila 42 rebalancea automáticamente los porcentajes dentro de cada trimestre sumando exactamente el 100%.\n\n"
     "PASO 2: Introducir Calificaciones en 'Registro Notas'\n"
     "Introduce las notas (0.00 a 10.00) obtenidas por los alumnos en cada tarea (columnas D a O).\n"
     "Las notas de 1º, 2º y 3er Trimestre se calculan automáticamente en las columnas P, Q y R a partir de los pesos derivados de los criterios.\n\n"
     "PASO 3: Supervisar el 'Panel de Control'\n"
     "Observa las tarjetas de KPIs (Alumnos, Aprobados, Suspensos, Nota Media, Tasa de Éxito) y la tabla consolidada\n"
     "con la calificación oficial y el estado de superación del módulo."),
    
    ("3. Robustez Matemática (Sin Ceros Prematuros)",
     "La fórmula implementada en cada criterio utiliza la función ISNUMBER combinada con SUMPRODUCT:\n"
     "Solo se promedian aquellas tareas que tienen una 'X' Y QUE ADEMÁS TIENEN NOTA INTRODUCIDA.\n"
     "Esto evita que un alumno aparezca con una nota suspensa en un criterio a principio de curso simplemente\n"
     "porque las tareas de los trimestres posteriores todavía no se han impartido o calificado."),
    
    ("4. Marco Normativo Integrado",
     "• Ley Orgánica 3/2022 y Real Decreto 659/2023 (Artículo 100 y Anexo VIII: currículo básico de Sostenibilidad 1708).\n"
     "• Real Decreto 500/2024 (Incorporación de Sostenibilidad a los títulos de FP).\n"
     "• Decreto 104/2024 (Ordenación de FP en Andalucía, derogando el Decreto 436/2008).\n"
     "• Orden de 18 de septiembre de 2025 (Evaluación y acreditación del alumnado de FP en Andalucía).\n"
     "• Normativa ASG sectorial: Directiva CSRD (UE 2022/2464), Directiva RAEE (2012/19/UE), Ley 7/2022 de residuos y Ley 3/2023 de Economía Circular de Andalucía (LECA).")
]

ws_guide.column_dimensions["A"].width = 6
ws_guide.column_dimensions["B"].width = 85
for c in ["C", "D", "E", "F", "G"]:
    ws_guide.column_dimensions[c].width = 12

curr_row = 3
for title, text in guide_sections:
    ws_guide.row_dimensions[curr_row].height = 26
    ws_guide.merge_cells(f"B{curr_row}:G{curr_row}")
    cell_sec = ws_guide[f"B{curr_row}"]
    cell_sec.value = title
    cell_sec.font = Font(name="Segoe UI", size=11, bold=True, color="065F46")
    cell_sec.fill = FILL_EMERALD_LIGHT
    cell_sec.alignment = ALIGN_LEFT
    cell_sec.border = HEADER_BORDER
    curr_row += 1
    
    num_lines = text.count("\n") + 1
    ws_guide.row_dimensions[curr_row].height = max(50, num_lines * 18)
    ws_guide.merge_cells(f"B{curr_row}:G{curr_row}")
    cell_body = ws_guide[f"B{curr_row}"]
    cell_body.value = text
    cell_body.font = FONT_BODY
    cell_body.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    cell_body.fill = FILL_ZEBRA
    cell_body.border = CELL_BORDER
    curr_row += 2


# -------------------------------------------------------------
# Save Workbook
# -------------------------------------------------------------
output_dir = r"e:\00. Clases\Apuntes\Sostenibilidad\Programación"
os.makedirs(output_dir, exist_ok=True)

excel_path = os.path.join(output_dir, "Hoja_Evaluacion_Avanzada_Sostenibilidad_1DAW_DAM_2025_2026.xlsx")
excel_path_v2 = os.path.join(output_dir, "Hoja_Evaluacion_Avanzada_Sostenibilidad_1DAW_DAM_2025_2026_v2.xlsx")

try:
    wb.save(excel_path)
    print(f"Hoja de evaluación avanzada para Sostenibilidad guardada con éxito en:\n{excel_path}")
except PermissionError:
    wb.save(excel_path_v2)
    print(f"AVISO: El archivo principal está abierto en Excel. Se ha guardado en:\n{excel_path_v2}")
