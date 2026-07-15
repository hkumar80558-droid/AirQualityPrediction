try:
    import requests
except ImportError:
    raise ImportError("requests module is required. Install it using: pip install requests")

API_KEY = "f52890588db51670ebb43370ad287b4c"


def get_weather(city="Delhi"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:

        response = requests.get(url, timeout=10)

        data = response.json()

        if response.status_code == 200:

            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": data["weather"][0]["description"].title()
            }

            return weather

        else:

            return None

    except Exception as e:

        print(e)
        return None