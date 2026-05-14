# ocr_pdf.py
import pytesseract
from PIL import Image
# Abrir la imagen
img = Image.open("/home/farfaneduardo/Documentos/Proyectos/farfan-eduardo-pdi-1c-2026/Diciembre2025.jpeg")
# Extraer texto y guardar como PDF
pdf_data = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')
# Guardar el PDF
with open("Diciembre2025_texto.pdf", "wb") as f:
    f.write(pdf_data)
print("PDF con texto extraído creado: Diciembre2025_texto.pdf")