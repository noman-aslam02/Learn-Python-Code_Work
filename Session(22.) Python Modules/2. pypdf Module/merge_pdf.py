from pypdf import PdfMerger
import os

# PdfMerger class ka instance banaya gaya hai
merge = PdfMerger()

# PDF files ko merge ke liye append kiya gaya hai
merge.append("monk_ang.pdf")
merge.append("monk_hap.pdf")

pdf_file = "monkeys.pdf"

# Check kiya gaya hai ke 'monkeys.pdf' file pehle se exist karti hai ya nahi
if os.path.exists(pdf_file):
    print(f"File '{pdf_file}' pehle se exist karti hai")
else:
    # PDFs ko merge karke 'monkeys.pdf' file mein likha gaya hai
    with open(pdf_file, "wb") as monk_file:
        merge.write(monk_file)
        print("PDFs successfully merge ho gaye hain")

# 'monkeys.pdf' file ko default PDF viewer mein open karne ke liye (Windows)
try:
    os.startfile(pdf_file)
except Exception as e:
    print(f"PDF file ko open karte waqt error aaya hai: {e}")
