import pandas as pd
from openpyxl import Workbook
from win32com.client import Dispatch
from openpyxl.utils.dataframe import dataframe_to_rows
import os

mydata = {
    "Name":["Vikas","Goat","Freak"],
    "Class":["10th","12th","3rd year BE"],
    "Scores":[98, 88, 55],
}

MydataFrame = pd.DataFrame(mydata)
workbook = Workbook()
sheet = workbook.create_sheet(title="Students")

for row in dataframe_to_rows(MydataFrame,index=False,header=True):
    sheet.append(row)


save_path = r'Data\1.2_Excel_Pandas.xlsx'
workbook.save(save_path)