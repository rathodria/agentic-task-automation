data={"Goa":"Sunny, 30°C","Delhi":"Clear, 22°C"}
def get_weather(city): return data.get(city, "Weather unavailable")
