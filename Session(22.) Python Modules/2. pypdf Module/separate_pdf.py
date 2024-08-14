# pypdf module se PdfReader aur PdfWriter import karo
from pypdf import PdfReader, PdfWriter

# PdfReader object banao jo PDF ko read karega
pdf_reader = PdfReader("newest.pdf")

# PdfWriter object banao jo ek nayi PDF file banayega
pdf_writer = PdfWriter()

# Har page ko alag alag save karne ke liye loop chalao
for page_num in range(len(pdf_reader.pages)):

    # PdfReader se current page ko lo aur PdfWriter mein add karo
    pdf_writer.add_page(pdf_reader.pages[page_num])

    # Output PDF file ka naam define karo, jismein current page save hoga
    output_pdf_path = f"output_page_{page_num + 1}.pdf"

    # Nayi PDF file ko write mode ('wb') mein open karo
    with open(output_pdf_path, 'wb') as output_file:
        # PdfWriter se current page ko nayi PDF file mein likho
        pdf_writer.write(output_file)

# Process complete hone ka message print karo
print("PDF split successfully!")