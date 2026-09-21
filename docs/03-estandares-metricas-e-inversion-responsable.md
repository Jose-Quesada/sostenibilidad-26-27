# 03 · Estándares, métricas e inversión socialmente responsable

**Resultados de aprendizaje que cubre:** RA1 (criterios e, f)

> **Objetivo didáctico:** identificar los principales estándares de métricas para la evaluación
> del desempeño en sostenibilidad y su papel en la rendición de cuentas; describir la inversión
> socialmente responsable y el papel de analistas, inversores, agencias e índices.

---

## 1. Panorama de estándares y marcos de reporte ASG

Criterio RA1.e: *"identificar los principales estándares de métricas para la evaluación del
desempeño en sostenibilidad y su papel en la rendición de cuentas que marca la legislación
vigente y las futuras regulaciones en desarrollo."*

### 1.1 Normas ISO (Organización Internacional de Normalización)

| Norma | Ámbito | Uso en sector TIC |
|-------|--------|-------------------|
| **ISO 26000** | Orientaciones sobre responsabilidad social. | Marco general de comportamiento responsable. |
| **ISO 14001** | Sistemas de gestión ambiental. | Certificación de la gestión ambiental de instalaciones/procesos. |
| **ISO 50001** | Sistemas de gestión de energía. | Eficiencia energética en data centers y oficinas. |
| **ISO 14064-1** | Cuantificación e informe de GEI (organización). | Inventario de huella de carbono (Alcances 1, 2, 3). |
| **ISO 14067** | Huella de carbono de productos. | LCA / huella por producto o servicio TIC. |
| **ISO 31000** | Gestión de riesgos. | Riesgos ASG (ver §4 del archivo 02). |
| **ISO 14001/50001 + 14064** combinadas | Base técnica de la mayoría de inventarios. | Estándar de facto para reportes climáticos. |

> **Punto clave:** ISO 14064-1 es la norma técnica sobre la que se construyen los inventarios
> de GEI; el protocolo **GHG Protocol** (WRI/WBCSD) es su complemento más usado en empresas.

### 1.2 GRI (Global Reporting Initiative)

- El marco de reporte de sostenibilidad **más utilizado a nivel global**.
- Estructura: **estándares universales** (general, aspectos temáticos) + **temas específicos**
  (emisiones, agua, residuos, diversidad, datos, etc.).
- Principio rector: **materialidad temática** (qué afecta a la empresa y qué la afecta).
- El alumnado usará la lógica GRI para estructurar el informe de sostenibilidad del T3.

### 1.3 SASB → ISSB (IFRS S1 y S2)

- **SASB** (Sustainability Accounting Standards Board): estándares sectoriales de materialidad
  financiera (cómo los temas ASG afectan al valor económico).
- En 2022 SASB se integra en el **ISSB** (International Sustainability Standards Board, bajo IFRS
  Foundation), que publica:
  - **IFRS S1:** información general sobre sostenibilidad.
  - **IFRS S2:** divulgación de información climática (alineada con TCFD).
- Son la base de la futura contabilidad ESG internacional y se alinean con la CSRD europea.

### 1.4 CDP (Carbon Disclosure Project)

- Plataforma global de divulgación ambiental a inversores.
- Cuestionarios por tema: **Clima, Agua, Bosques**.
- Las empresas TIC responden al cuestionario climático; las calificaciones (A–D) influyen en la
  percepción de inversores y clientes.

### 1.5 Otros marcos

- **AA1000:** estándar de aseguramiento y materialidad de la responsabilidad social.
- **TCFD** (Task Force on Climate-related Financial Disclosures): divulgación financiera climática
  (gobernanza, estrategia, gestión de riesgos, indicadores). Adoptado por ISSB/IFRS S2.
- **UNGP / OIT:** principios rectores de derechos humanos y empresas.

### 1.6 Cuadro comparativo rápido

| Marco | Enfoque | ¿Qué mide? | Uso típico |
|-------|---------|------------|------------|
| ISO 14064 / GHG Protocol | Técnico-medible | Emisiones GEI (tCO₂e) | Inventario de huella |
| GRI | Reporte integral | Aspectos materiales E/S/G | Informe de sostenibilidad |
| IFRS S1/S2 (ISSB) | Materialidad financiera | Riesgos/oportunidades ASG que afectan al valor | Divulgación a inversores |
| CDP | Divulgación a capital | Clima, agua, bosques | Calificación por inversores |
| TCFD | Climático-financiero | 4 pilares (gobernanza, estrategia, riesgo, KPIs) | Reporte climático |

---

## 2. Métricas y KPIs típicos del sector TIC

Criterio RA1.e / RA6.d: *"determinar las métricas de evaluación del desempeño de acuerdo con
los estándares de sostenibilidad más ampliamente utilizados."*

### 2.1 Indicadores ambientales (E)

| KPI | Unidad | Referencia/estándar |
|-----|--------|---------------------|
| Emisiones GEI Alcance 1 | tCO₂e | ISO 14064-1 / GHG Protocol |
| Emisiones GEI Alcance 2 (mercado y ubicación) | tCO₂e | GHG Protocol |
| Emisiones GEI Alcance 3 | tCO₂e | GHG Protocol |
| Consumo eléctrico total | MWh | ISO 50001 |
| % energía renovable | % | CDP / GRI 305 |
| **PUE** (Power Usage Effectiveness) | ratio | Green Grid (eficiencia de data centers) |
| **WUE** (Water Usage Effectiveness) | L/kWh | Green Grid (huella hídrica) |
| Residuos electrónicos generados | kg o % | GRI 306 / RAEE |
| % materiales reciclados/reutilizados | % | GRI 301 / ecodiseño UE |
| Huella hídrica total | m³ | ISO 14046 (huella hídrica) |

> **PUE** es el indicador estrella del sector: `PUE = energía total del data center / energía
> de los sistemas IT`. Un PUE de 1,0 es ideal (toda la energía va a IT); hoy los mejores están
> en torno a 1,1. Es perfecto para prácticas cuantitativas.

### 2.2 Indicadores sociales (S)

| KPI | Unidad | Referencia |
|-----|--------|------------|
| % mujeres en plantilla / puestos técnicos | % | GRI 405 (igualdad) |
| Rotación de personal | % | GRI 401 |
| Horas de formación por empleado | h | GRI 404 |
| Incidentes de seguridad/privacidad | nº | RGPD / NIS2 |
| Satisfacción laboral | índice | encuesta interna |
| Diversidad e inclusión (D&I) | % / índice | GRI 405 |

### 2.3 Indicadores de gobernanza (G)

| KPI | Unidad | Referencia |
|-----|--------|------------|
| Existencia de comité de sostenibilidad | sí/no | IFRS S1 |
| % retribución vinculada a KPIs ESG | % | GRI 207 |
| Informes ASG asegurados (externos) | % / año | AA1000 / CSRD |
| Cumplimiento de código ético | % / nº incidencias | GRI 205 |
| Nº proveedores auditados en sostenibilidad | % | GRI 308 |

---

## 3. Inversión socialmente responsable (RA1.f)

Criterio RA1.f: *"describir la inversión socialmente responsable y el papel de los analistas,
inversores, agencias e índices de sostenibilidad en el fomento de la sostenibilidad."*

### 3.1 Concepto

La **inversión socialmente responsable (ISR)** integra criterios ASG en las decisiones de
inversión, más allá del retorno financiero puramente corto. Formas:

- **Screening negativo:** excluir sectores/empresas problemáticas (armas, tabaco, carbón).
- **Screening positivo (best-in-class):** seleccionar líderes ESG por sector.
- **Inversión de impacto:** buscar un impacto social/ambiental medible y explícito.
- **ESG integration:** incorporar sistemáticamente los factores ASG al análisis financiero.
- **Activismo accionarial (engagement/shareholder activism):** presionar a las empresas para
  mejorar su desempeño ESG.

### 3.2 Actores del ecosistema ISR

| Actor | Papel en el fomento de la sostenibilidad |
|-------|------------------------------------------|
| **Inversores institucionales** (fondos de pensiones, seguros, family offices) | Condicionan financiación a mejoras ESG; grandes dueños de empresas TIC. |
| **Analistas ESG / analistas financieros** | Evalúan y califican el desempeño ASG; incorporan riesgos ASG a valoraciones. |
| **Agencias de rating ESG** (MSCI, S&P Global, CDP, Sustainalytics, ISS) | Otorgan calificaciones (AAA–CCC) que mueven flujos de capital. |
| **Índices de sostenibilidad** (DJSI, FTSE4Good, EcoVadis, MSCI ESG Leaders) | Recopilan empresas líderes; los fondos los usan como referencia de inversión. |
| **Reguladores** (CSRD, SFDR, Taxonomía UE) | Obligan a reportar y a etiquetar productos financieros "verdes". |

### 3.3 Principales índices y agencias (fichas breves)

- **DJSI (Dow Jones Sustainability Indices):** los índices de sostenibilidad más antiguos y
  reconocidos; incluyen a empresas líderes por tamaño y sector.
- **MSCI ESG Ratings:** calificación AAA (líder) a CCC (alto riesgo); muy usada por fondos.
- **S&P Global CSA / Corporate Sustainability Assessment:** evaluación que alimenta el DJSI.
- **EcoVadis:** medalla (platino/oro/plata/bronce) por desempeño RSE; popular en cadenas de suministro (muy usado para calificar proveedores TIC).
- **CDP:** calificación climática/hídrica A–D; referencia para riesgo climático.
- **FTSE4Good:** índice de empresas con prácticas ASG sólidas (Londres).

### 3.4 Efecto sobre las empresas TIC

- Una mala calificación ESG puede encarecer el capital y perder clientes corporativos.
- Una buena calificación abre acceso a **bonos verdes** y a fondos de inversión responsable.
- El alumnado debe entender que la sostenibilidad es hoy un **factor financiero**, no solo ético.

> **Regulación financiera vinculada:** el **SFDR** (Sustainable Finance Disclosure Regulation)
> obliga a los gestores financieros a revelar su integración de riesgos ASG; y la **Taxonomía UE**
> define qué actividades son "ambientalmente sostenibles" para canalizar inversión verde real
> y evitar el *greenwashing*.

---

## 4. Regulación que marca la rendición de cuentas (contexto RA1.e)

| Norma | Qué obliga | Plazo/estado |
|-------|-----------|--------------|
| **CSRD** (Reg. UE 2022/2464) | Reporte de doble materialidad con estándares ESRS, con aseguramiento externo. | Aplica progresivamente desde el ejercicio 2024–2028 según tamaño. |
| **ESRS** (Estándares Europeos de Reporte de Sostenibilidad) | 10 temas transversales + sectoriales; métricas detalladas. | Aprobados por la ESMA/Commission (2023). |
| **Taxonomía UE** | Clasificar actividades "verdes"; evitar greenwashing. | En vigor, sectores progresivos. |
| **SFDR** | Divulgación de sostenibilidad en productos financieros. | En vigor desde 2021–2023. |
| **Reglamento de debida diligencia (CSDDD)** | Debida diligencia en derechos humanos y medio ambiente en cadenas de valor. | En tramitación/implantación progresiva. |

> **Conclusión para el alumnado:** la "rendición de cuentas" ya no es voluntaria: CSRD +
> aseguramiento externo + Taxonomía obligan a las grandes empresas (incluidas muchas TIC) a
> medir, reportar y garantizar sus datos ASG. Esto da rigor y exigibilidad a todo el módulo.

---

## 5. Síntesis (ficha resumen)

```
ESTÁNDARES DE MÉTRICAS:
  ISO 14064/GHG Protocol → inventario GEI (tCO₂e).
  ISO 50001 → energía; PUE/WUE → data centers.
  GRI → informe de sostenibilidad (materialidad temática).
  IFRS S1/S2 (ISSB) + TCFD → materialidad financiera / climático-financiero.
  CDP → calificación a inversores (clima, agua, bosques).

KPIs TIC típicos: tCO₂e por alcance, % renovables, PUE, WUE, kg RAEE, % reciclado,
  % mujeres técnicas, nº incidentes de privacidad, % proveedores auditados.

INVERSIÓN RESPONSABLE (ISR): screening, best-in-class, impacto, integración ESG, activismo.
ACTORES: inversores institucionales, analistas, agencias (MSCI, S&P, CDP, EcoVadis),
  índices (DJSI, FTSE4Good), reguladores (CSRD, SFDR, Taxonomía).

Efecto: la calificación ESG mueve capital; la sostenibilidad es hoy un FACTOR FINANCIERO.
```

---

## 6. Cuestionario de autoevaluación (RA1e–f)

1. Diferencia ISO 14064-1, GRI e IFRS S2: ¿qué mide cada uno y a quién va dirigido?
2. ¿Qué es el PUE y por qué es un KPI clave en data centers? Calcula el PUE si la energía total es 1.200 MWh y la de IT es 1.000 MWh.
3. Enumera tres KPIs ambientales, tres sociales y tres de gobernanza para una empresa cloud.
4. ¿Qué diferencia hay entre screening negativo e inversión de impacto?
5. Explica cómo una mala calificación MSCI puede afectar a una empresa TIC.
6. ¿Qué obliga la CSRD y qué son los ESRS? ¿Afecta a las grandes empresas del sector?

> Soluciones orientativas en [`10-glosario-recursos-bibliografia.md`](10-glosario-recursos-bibliografia.md).
