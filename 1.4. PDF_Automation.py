#1. Read the PDF File and print the contents and Page Number Count
#2. Create a PDF File

#pip install PyPDF2
#pip install fpdf

import PyPDF2
from fpdf import FPDF

#1. Start
# #Read the PDF as Binary File using rb
# file = open('Data\Inputs\Digital_Resume.pdf','rb')

# Create a PDF reader object
# reader=PyPDF2.PdfReader(file)

# to get PDF Page Count
# #print(len(reader.pages))

# activePage= reader.pages[0]
# print(activePage.extract_text())

#1. End

#2. Start

# Create an instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set the font and size  
pdf.set_font('helvetica', size=14)

# Add a cell with the text
pdf.cell(200, 20, text="Vikas is here!!", align="C")
pdf.cell(text="This is the main body of this pdf")


# Output the PDF to a file
output_path = r'Data\1.4_PDF_Automation.pdf'  # Use raw string for path
pdf.output(output_path)