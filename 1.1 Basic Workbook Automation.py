#1. Use Active Sheet
#2. CREATE NEW SHEET AND USE IT
#3. Write values to cells
#4. Fetch and Print the cellvalues
#5, Rewrite a cell value
#6. Open an workbook application


from openpyxl import Workbook
from win32com.client import Dispatch
import os

# 1. Create a new workbook and use the active sheet
workbook = Workbook()
sheet = workbook.active  # Gets the active sheet
#sheet = workbook.create_sheet(title="NewSheet") # Creates a new sheet
# 2. Write values to cells
sheet["A1"] = "Helloo"
sheet["B1"] = "Vikas"

# 3. Save the workbook
savePath = r'Data\1.1_Basic_Workbook_Activities.xlsx'
savePath = os.path.abspath(savePath)
workbook.save(savePath)

# 4. Fetch and print the cell values
cellvalues = sheet["A1"].value + " " + sheet["B1"].value 
print("Original Cell Values:", cellvalues)

# 5. Rewrite a cell value
#sheet["A1"] = "Hello, Vikas!"

# Save the changes to the workbook
workbook.save(savePath)

# 6. Start Excel and open the workbook
xl = Dispatch('Excel.Application')
xl.Visible = True

# Open the workbook in Excel
wb = xl.Workbooks.Open(savePath)
