import streamlit as st
import requests
import pandas as pd
import time
from datetime import datetime
import plotly.express as px
import folium
from streamlit_folium import st_folium
from io import BytesIO
from fpdf import FPDF
import base64

# Page config
st.set_page_config(page_title="🌤️ Weather Dashboard", layout="wide")

# Theme toggle
dark_mode = st.toggle("🌙 Dark Mode", value=False)
if dark_mode:
    st.markdown("<style>body { background-color: #1e1e1e; color: white; }</style>", unsafe_allow_html=True)

# Title
st.title("🌤️ Advanced Weather Dashboard")

# API key
API_KEY = st.secrets["OPENWEATHER_API_KEY"]
  # Replace with your OpenWeather key

# Input
city_input = st.text_input("Enter cities (comma-separated):", "Bangalore, Mysore, Mangalore")
cities = [c.strip() for c in city_input.split(",") if c.strip()]

@st.cache_data(ttl=600)
def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return {"error": f"Error {res.status_code}: {res.text}"}
        return res.json()
    except Exception as e:
        return {"error": str(e)}

@st.cache_data(ttl=600)
def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return {"error": f"Error {res.status_code}: {res.text}"}
        return res.json()
    except Exception as e:
        return {"error": str(e)}

weather_data = []
map_locations = []

for city in cities:
    with st.spinner(f"Fetching weather for {city}..."):
        current = get_current_weather(city)
        forecast = get_forecast(city)
        time.sleep(1)

    if "error" in current:
        st.error(f"{city}: {current['error']}")
        continue

    try:
        data = {
            "City": current["name"],
            "Country": current["sys"]["country"],
            "Temperature (°C)": current["main"]["temp"],
            "Humidity (%)": current["main"]["humidity"],
            "Wind Speed (m/s)": current["wind"]["speed"],
            "Cloudiness (%)": current["clouds"]["all"],
            "Weather": current["weather"][0]["description"].title(),
            "Datetime": datetime.utcfromtimestamp(current["dt"]).strftime('%Y-%m-%d %H:%M:%S'),
            "Lat": current["coord"]["lat"],
            "Lon": current["coord"]["lon"]
        }
        weather_data.append(data)
        map_locations.append((data["City"], data["Lat"], data["Lon"]))

        with st.expander(f"📍 {data['City']}, {data['Country']}"):
            st.metric("Temperature (°C)", data["Temperature (°C)"])
            st.metric("Humidity (%)", data["Humidity (%)"])
            st.metric("Wind Speed (m/s)", data["Wind Speed (m/s)"])
            st.metric("Cloudiness (%)", data["Cloudiness (%)"])
            st.write("**Weather:**", data["Weather"])
            st.caption(f"Updated at: {data['Datetime']} UTC")

            if "list" in forecast:
                df_forecast = pd.DataFrame(forecast["list"])
                df_forecast["dt_txt"] = pd.to_datetime(df_forecast["dt_txt"])
                df_forecast["Temp"] = df_forecast["main"].apply(lambda x: x["temp"])
                df_forecast["Wind"] = df_forecast["wind"].apply(lambda x: x["speed"])
                df_forecast["Humidity"] = df_forecast["main"].apply(lambda x: x["humidity"])

                st.write("### 📈 Forecast (5-Day)")
                fig = px.line(df_forecast, x="dt_txt", y="Temp", title="Temperature Forecast")
                st.plotly_chart(fig, use_container_width=True)
                fig2 = px.line(df_forecast, x="dt_txt", y="Wind", title="Wind Speed Forecast")
                st.plotly_chart(fig2, use_container_width=True)
    except Exception as e:
        st.warning(f"Error parsing weather for {city}: {e}")

if weather_data:
    df = pd.DataFrame(weather_data)

    st.subheader("📊 Weather Summary Charts")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(px.bar(df, x="City", y="Temperature (°C)", color="Temperature (°C)", title="Temperature"))
    with col2:
        st.plotly_chart(px.bar(df, x="City", y="Humidity (%)", color="Humidity (%)", title="Humidity"))

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(px.bar(df, x="City", y="Wind Speed (m/s)", color="Wind Speed (m/s)", title="Wind Speed"))
    with col4:
        st.plotly_chart(px.bar(df, x="City", y="Cloudiness (%)", color="Cloudiness (%)", title="Cloudiness"))

    st.subheader("🗺️ City Map")
    m = folium.Map(location=[weather_data[0]["Lat"], weather_data[0]["Lon"]], zoom_start=5)
    for city, lat, lon in map_locations:
        folium.Marker(location=[lat, lon], popup=city).add_to(m)
    st_folium(m, width=700, height=450)

    st.subheader("📄 Full Weather Data")
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download CSV", csv, "weather_data.csv", "text/csv")

    excel_buf = BytesIO()
    df.to_excel(excel_buf, index=False, sheet_name="Weather")
    st.download_button("⬇️ Download Excel", excel_buf.getvalue(), "weather_data.xlsx", "application/vnd.ms-excel")

    # PDF export
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Weather Report", ln=True, align="C")
    for i, row in df.iterrows():
        pdf.cell(200, 10, txt=str(row.to_dict()), ln=True)
    pdf_buf = BytesIO()
    pdf.output(pdf_buf)
    st.download_button("⬇️ Download PDF", data=pdf_buf.getvalue(), file_name="weather_report.pdf", mime="application/pdf")

else:
    st.info("Enter valid city names to view data.")
