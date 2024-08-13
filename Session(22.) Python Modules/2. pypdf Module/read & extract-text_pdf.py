from pypdf import PdfReader

# PDF file ko kholna
pdf_reader = PdfReader("Karachi.pdf")

# Dekhna ke PDF file mein kitni pages hain
num_pages = pdf_reader.get_num_pages()
print(f"Number of pages in the PDF: {num_pages}")

# PDF file se text nikalna

# Yeh loop saari pages ka text print karega
# Istamal karne ke liye neeche wali lines uncomment karein
# for page in pdf_reader.pages:
#     print(page.extract_text())

# Ya phir aap kisi specific page ka text bhi nikal sakte hain aur print kar sakte hain

# PDF file se saari pages hasil karna
pages = pdf_reader.pages

# Pehla page object print karna (debugging ke liye)
print(pages)

# Pehle page se text nikalna aur print karna
first_page_text = pages[0].extract_text()
print(f"Text from the first page:\n{first_page_text}")