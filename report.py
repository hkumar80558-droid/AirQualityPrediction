from fpdf import FPDF
from datetime import datetime


def create_pdf(aqi, category, advice):

    filename = "AQI_Report.pdf"

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=16)

    pdf.cell(
        200,
        10,
        "Air Quality Prediction Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font("Arial", size=12)


    pdf.cell(
        200,
        10,
        f"Date: {datetime.now()}",
        ln=True
    )


    pdf.cell(
        200,
        10,
        f"Predicted AQI: {aqi}",
        ln=True
    )


    pdf.cell(
        200,
        10,
        f"Air Quality Category: {category}",
        ln=True
    )


    pdf.ln(10)


    pdf.multi_cell(
        0,
        10,
        f"Health Advice: {advice}"
    )


    pdf.output(filename)


    return filename