from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

excel_files = glob.glob("files/*.xlsx")
print(excel_files)


for file in excel_files:
    df = pd.read_excel(file)
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    for index, row in df.iterrows():
        pdf.add_page()

        filename = Path(file).stem
        invoice_no, date = filename.split("-")

        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_no}", ln=1)

        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=0, h=16, txt=f"Date: {date}", ln=1)

        pdf.output(f"PDFs/{filename}.pdf")

