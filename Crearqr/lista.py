from fpdf import FPDF

# Datos de la lista
alumnos = [
    ("CRUZ JUAREZ", "ALAN"),
    ("LIRA CHAVARRIA", "ALAN ELIAS"),
    ("SOTO VALERIO", "ALISSON"),
    ("GARCIA GALINDO", "BRENDA JOANA"),
    ("RODRIGUEZ REYES", "CESAR GAEL"),
    ("GONZALEZ GARCIA", "EVELYN ALEJANDRA"),
    ("ZAPATA GARCIA", "EVELYN JAMILET"),
    ("RAMIREZ EUSEBIO", "GABRIEL"),
    ("CRUZ GIL", "GONZALO URIEL"),
    ("ABURTO BONILLA", "JACQUELINE"),
    ("HERNANDEZ HERNANDEZ", "JACQUELINE"),
    ("VARO PARADA", "JATZIRI"),
    ("GARCIA JIMENEZ", "JESUS ARTURO"),
    ("GARCIA JIMENEZ", "JOSE LUIS"),
    ("VELAZQUEZ FUENTES", "JOSTIN DANIEL"),
    ("GALINDO MALDONADO", "KAMAEL OMEATL"),
    ("MEDINA SALOME", "KARINA LIZBETH"),
    ("GUALITO HERNANDEZ", "KARLA JOVANA"),
    ("CHABLE DE LEON", "LEONARDO DANIEL"),
    ("CIPRIANO MONDRAGON", "LUIS ALFONSO"),
    ("BENITEZ AGUILAR", "LUZ JACQUELINE"),
    ("JORDAN AVILES", "MARCO ANTONIO"),
    ("HERNANDEZ RONQUILLO", "RICARDO"),
    ("JUAREZ MUNOZ", "RICARDO GABRIEL"),
    ("MARTINEZ MONDRAGON", "RODRIGO"),
    ("FLORENTINO LOPEZ", "UZZIEL")
]

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Título
pdf.cell(0, 10, "Lista de Alumnos", ln=True, align='C')
pdf.ln(5)

# Encabezados
pdf.set_font("Arial", 'B', 12)
pdf.cell(70, 10, "Apellido(s)", border=1, align='C')
pdf.cell(70, 10, "Nombre(s)", border=1, align='C')
pdf.ln()

# Cuerpo de la tabla
pdf.set_font("Arial", size=12)
for apellido, nombre in alumnos:
    pdf.cell(70, 10, apellido, border=1)
    pdf.cell(70, 10, nombre, border=1)
    pdf.ln()

pdf.output("lista_alumnos.pdf")
print("PDF generado: lista_alumnos.pdf")