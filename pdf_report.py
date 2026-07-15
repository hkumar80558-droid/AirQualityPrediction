from fpdf import FPDF
from datetime import datetime


def generate_pdf(
        aqi,
        category,
        advice,
        pm25,
        pm10,
        no,
        no2,
        nox,
        co,
        so2,
        o3,
        weather
):

    filename = "AQI_Report.pdf"


    pdf = FPDF()

    pdf.add_page()


    pdf.set_font("Arial", "B", 18)

    pdf.cell(
        0,
        10,
        "Air Quality Prediction Report",
        ln=True,
        align="C"
    )


    pdf.ln(10)


    pdf.set_font("Arial", size=12)


    pdf.cell(
        0,
        10,
        f"Generated Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        ln=True
    )


    pdf.ln(5)


    pdf.set_font("Arial", "B", 14)
    pdf.cell(
        0,
        10,
        "AQI Prediction",
        ln=True
    )


    pdf.set_font("Arial", size=12)


    pdf.cell(
        0,
        10,
        f"Predicted AQI: {aqi}",
        ln=True
    )


    pdf.cell(
        0,
        10,
        f"Category: {category}",
        ln=True
    )


    pdf.multi_cell(
        0,
        10,
        f"Health Advice: {advice}"
    )


    pdf.ln(5)


    pdf.set_font("Arial", "B", 14)

    pdf.cell(
        0,
        10,
        "Pollution Values",
        ln=True
    )


    pdf.set_font("Arial", size=12)


    pollutants = [
        ("PM2.5", pm25),
        ("PM10", pm10),
        ("NO", no),
        ("NO2", no2),
        ("NOx", nox),
        ("CO", co),
        ("SO2", so2),
        ("O3", o3)
    ]


    for name, value in pollutants:

        pdf.cell(
            0,
            8,
            f"{name}: {value}",
            ln=True
        )


    pdf.ln(5)


    if weather:


        pdf.set_font("Arial", "B", 14)

        pdf.cell(
            0,
            10,
            "Weather Information",
            ln=True
        )


        pdf.set_font("Arial", size=12)


        pdf.cell(
            0,
            8,
            f"City: {weather['city']}",
            ln=True
        )


        pdf.cell(
            0,
            8,
            f"Temperature: {weather['temperature']} C",
            ln=True
        )


        pdf.cell(
            0,
            8,
            f"Humidity: {weather['humidity']} %",
            ln=True
        )


        pdf.cell(
            0,
            8,
            f"Wind Speed: {weather['wind']} m/s",
            ln=True
        )


        pdf.cell(
            0,
            8,
            f"Condition: {weather['description']}",
            ln=True
        )


    pdf.output(filename)


    return filename