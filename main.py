from fpdf import FPDF
import pandas as pd
import glob

excel_files = glob.glob("files/*.xlsx")
print(excel_files)

pdf = FPDF(orientation="P", unit="mm", format="A4" )
for file in excel_files:
    df = pd.read_excel(file)

    for index, row in df.iterrows():
        print(df)

