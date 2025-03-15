import streamlit as st
import requests

# OpenWeatherMap API Key
API_KEY = "4565bdea59e6778f22b6db165ac65149"  # Replace with your API key

def get_weather(city, country):
    if not city or not country:
        st.error("Please enter both country and city.")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            st.error(data.get("message", "Error retrieving weather data"))
            return
        
        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        
        st.success(f"**Weather:** {weather_desc}\n\n**Temperature:** {temp}°C")
    
    except Exception as e:
        st.error(f"Could not retrieve weather data: {e}")

# Streamlit UI
st.title("Weather App")

# Country and City text input fields
selected_country = st.text_input("Enter Country:").strip()
selected_city = st.text_input("Enter City:").strip()

if st.button("Get Weather"):
    get_weather(selected_city, selected_country)
