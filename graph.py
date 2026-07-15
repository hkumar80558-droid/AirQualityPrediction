import pandas as pd
import matplotlib.pyplot as plt
import os


def create_graph():

    print("Graph function started")


    file = "prediction_history.csv"


    if not os.path.exists(file):

        print("CSV file not found")
        return



    data = pd.read_csv(file)


    print(data.columns)



    if not os.path.exists("static"):

        os.makedirs("static")





    # 1. AQI Graph

    plt.figure(figsize=(8,5))


    plt.plot(
        data["AQI"],
        marker="o"
    )


    plt.title("AQI Prediction History")

    plt.xlabel("Prediction Number")

    plt.ylabel("AQI")

    plt.grid(True)


    plt.savefig("static/aqi_graph.png")

    plt.close()






    # 2. PM2.5 and PM10 Graph


    plt.figure(figsize=(8,5))


    plt.plot(
        data["PM2.5"],
        marker="o",
        label="PM2.5"
    )


    plt.plot(
        data["PM10"],
        marker="o",
        label="PM10"
    )


    plt.title("PM2.5 and PM10 Analysis")

    plt.xlabel("Prediction Number")

    plt.ylabel("Pollution Level")

    plt.legend()

    plt.grid(True)


    plt.savefig("static/pm_graph.png")

    plt.close()






    # 3. Gas Pollutant Graph


    plt.figure(figsize=(8,5))


    plt.plot(
        data["CO"],
        label="CO"
    )


    plt.plot(
        data["NO2"],
        label="NO2"
    )


    plt.plot(
        data["SO2"],
        label="SO2"
    )


    plt.plot(
        data["O3"],
        label="O3"
    )


    plt.title("Gas Pollutant Analysis")

    plt.xlabel("Prediction Number")

    plt.ylabel("Pollution Level")

    plt.legend()

    plt.grid(True)



    plt.savefig("static/gas_graph.png")

    plt.close()







    # 4. AQI Category Distribution Chart


    if "Category" in data.columns:


        category_count = data["Category"].value_counts()



        plt.figure(figsize=(7,7))


        plt.pie(

            category_count,

            labels=category_count.index,

            autopct="%1.1f%%"

        )


        plt.title("AQI Category Distribution")


        plt.savefig(
            "static/category_graph.png"
        )


        plt.close()



    else:

        print("Category column not found")






    print("All graphs created successfully")