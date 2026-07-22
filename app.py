from flask import Flask, render_template, request, send_file, redirect, url_for
from predict import predict_aqi
from graph import create_graph
from model_analysis import model_evaluation
from weather import get_weather
from report import create_pdf
import csv
import os
import pandas as pd
from datetime import datetime

app = Flask(__name__)

latest_prediction = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        pm25 = float(request.form["pm25"])
        pm10 = float(request.form["pm10"])
        no = float(request.form["no"])
        no2 = float(request.form["no2"])
        nox = float(request.form["nox"])
        co = float(request.form["co"])
        so2 = float(request.form["so2"])
        o3 = float(request.form["o3"])
    except Exception as e:
        print("ERROR:", e)
        return render_template(
            "index.html",
            error=str(e)
        )
    

    values = [
        pm25,
        pm10,
        no,
        no2,
        nox,
        co,
        so2,
        o3
    ]

    if any(value < 0 for value in values):

        return render_template(
            "index.html",
            error= "Error: Pollution values cannot be negative."
        )

    if any(value > 1000 for value in values):

        return render_template(
            "index.html",
            error= "Error: Please enter valid numeric values."
        )

    # AI Prediction

    result = predict_aqi(
        pm25,
        pm10,
        no,
        no2,
        nox,
        co,
        so2,
        o3
    )

    result = round(float(result), 2)

    # AQI Category

    if result <= 50:

        category = "Good"
        advice = "Air quality is good. Enjoy outdoor activities."
        color = "good"

    elif result <= 100:

        category = "Satisfactory"
        advice = "Air quality is acceptable."
        color = "satisfactory"

    elif result <= 200:

        category = "Moderate"
        advice = "Sensitive people should reduce outdoor activities."
        color = "moderate"

    elif result <= 300:

        category = "Poor"
        advice = "Avoid long outdoor exposure. Wear a mask."
        color = "poor"

    elif result <= 400:

        category = "Very Poor"
        advice = "Avoid outdoor exercise."
        color = "verypoor"

    else:

        category = "Severe"
        advice = "Stay indoors and avoid outdoor activities."
        color = "severe"

    # Save Prediction History

    filename = "prediction_history.csv"

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Date Time",
                "PM2.5",
                "PM10",
                "NO",
                "NO2",
                "NOx",
                "CO",
                "SO2",
                "O3",
                "AQI",
                "Category"
            ])
        writer.writerow([
            datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            pm25,
            pm10,
            no,
            no2,
            nox,
            co,
            so2,
            o3,
            result,
            category
        ])


    print("CSV saved successfully")


    # Create graphs

    create_graph()


    # Model analysis graph

    model_evaluation()


    print("All graphs created successfully")


    # Weather API

    weather = get_weather("Delhi")
    # Save latest prediction for PDF report

    latest_prediction["aqi"] = result
    latest_prediction["category"] = category
    latest_prediction["advice"] = advice

    return render_template(
        "index.html",
        prediction=result,
        category=category,
        advice=advice,
        color=color,
        weather=weather
    )


# ==========================
# Dashboard Route
# ==========================

@app.route("/dashboard")
def dashboard():

    file = "prediction_history.csv"

    if os.path.exists(file):

        data = pd.read_csv(file)

        total = len(data)

        if len(data) > 0:

            average = round(data["AQI"].mean(), 2)
            highest = data["AQI"].max()

        else:

            average = 0
            highest = 0

    else:

        total = 0
        average = 0
        highest = 0

    return render_template(
        "dashboard.html",
        total=total,
        average=average,
        highest=highest
    )
    

   


# ==========================
# Download Prediction History
# ==========================

@app.route("/download")
def download():

    filename = "prediction_history.csv"

    if os.path.exists(filename):

        return send_file(
            filename,
            as_attachment=True,
            download_name="prediction_history.csv"
        )

    return "Prediction history not found."

# ==========================
# Download AQI PDF Report
# ==========================

@app.route("/report")
def report():

    if not latest_prediction:
        return "No prediction available. Please predict AQI first."

    filename = create_pdf(
        latest_prediction["aqi"],
        latest_prediction["category"],
        latest_prediction["advice"]
    )

    if not os.path.exists(filename):
        return "Could not generate the report file."

    return send_file(
        filename,
        as_attachment=True,
        download_name="AQI_Report.pdf"
    )


# ==========================
# Clear Prediction History
# ==========================

@app.route("/clear")
def clear_history():

    filename = "prediction_history.csv"

    # Delete prediction history
    if os.path.exists(filename):
        os.remove(filename)
    return redirect(url_for("dashboard"))
# ==========================
# Run Flask App
# ==========================

if __name__ == "__main__":

    app.run(debug=True)