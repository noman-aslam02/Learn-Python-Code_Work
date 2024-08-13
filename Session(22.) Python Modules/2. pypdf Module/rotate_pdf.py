# pypdf module se PdfReader aur PdfWriter ko import karo
from pypdf import PdfReader, PdfWriter

# Existing PDF file ko read karo
pdf_reader = PdfReader("newest.pdf")

# Nayi PDF file create karo
pdf_writer = PdfWriter()

# Pages ko read karo
pages = pdf_reader.pages

for page in pages:
    # Page ko 180 degrees rotate karo
    rotated_page = page.rotate(180)

    # Rotated page ko nayi PDF file mein add karo
    pdf_writer.add_page(rotated_page)

# Nayi rotated PDF file ko save karo
with open('rotated.pdf', 'wb') as rotated_file:
    pdf_writer.write(rotated_file)