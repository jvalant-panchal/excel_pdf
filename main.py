from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

excel_files = glob.glob("files/*.xlsx")

for file in excel_files:
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    filename = Path(file).stem
    invoice_no, date = filename.split("-")

    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_no}", ln=1)

    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=0, h=16, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(file, sheet_name="Sheet 1")

    # Add table header
    pdf.set_font(family="Times", size=12, style="B")
    columns = list(df.columns)
    columns = [item.replace("_", "").title() for item in columns]
    pdf.set_text_color(90, 90, 90)
    pdf.cell(w=30, h=8, txt=columns[0], align="C", border=1,)
    pdf.cell(w=60, h=8, txt=columns[1], align="C", border=1)
    pdf.cell(w=40, h=8, txt=columns[2], align="C", border=1)
    pdf.cell(w=30, h=8, txt=columns[3], align="C", border=1)
    pdf.cell(w=30, h=8, txt=columns[4], align="C", border=1, ln=1)

# Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(90, 90, 90)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), align="C", border=1)
        pdf.cell(w=60, h=8, txt=str(row["product_name"]), align="C", border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), align="C", border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), align="C", border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), align="C", border=1, ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(w=30, h=8, txt="", align="C", border=1)
    pdf.cell(w=60, h=8, txt="", align="C", border=1)
    pdf.cell(w=40, h=8, txt="", align="C", border=1)
    pdf.cell(w=30, h=8, txt="", align="C", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), align="C", border=1, ln=1)

    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=30, h=14, txt=f"Total Price:{total_sum}", ln=1)
    pdf.cell(w=30, h=14, txt=f"pythonhow", )
    pdf.image("pythonhow.png", w=14)

    pdf.output(f"PDFs/{filename}.pdf")

