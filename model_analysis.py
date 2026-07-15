import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os


def model_evaluation():

    model = joblib.load("model/air_quality_model.pkl")


    result = {}


    # Check if model has feature importance

    if hasattr(model, "feature_importances_"):


        features = [
            "PM2.5",
            "PM10",
            "NO",
            "NO2",
            "NOx",
            "CO",
            "SO2",
            "O3"
        ]


        importance = model.feature_importances_


        feature_data = pd.DataFrame({

            "Feature": features,

            "Importance": importance

        })


        # Create static folder

        if not os.path.exists("static"):

            os.makedirs("static")



        # Feature importance graph


        plt.figure(figsize=(8,5))


        plt.bar(
            feature_data["Feature"],
            feature_data["Importance"]
        )


        plt.title("Feature Importance")

        plt.xlabel("Pollutants")

        plt.ylabel("Importance")

        plt.xticks(rotation=45)

        plt.tight_layout()


        plt.savefig(
            "static/feature_importance.png"
        )


        plt.close()



        print("Feature importance graph created")



        result["feature_graph"] = True


    else:

        print("Model does not support feature importance")

        result["feature_graph"] = False




    return result
