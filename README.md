# weather_dashboard
# 🌤️ Streamlit Weather Dashboard

COMPANY : CODTECH IT SOLUTIONS

NAME : LIKHITHA N

INTERN ID : CT06DL625

DOMAIN : PYTHON PROGRAMMING

DURATION : 6 WEEKS

MENTOR : NEELA SANTOSH


# 🌤️ Advanced Weather Dashboard – Streamlit Application

## 📘 Project Description

The **Advanced Weather Dashboard** is a comprehensive, interactive, and visually engaging weather data monitoring application developed using **Python** and 
<br>
**Streamlit**. It enables users to fetch real-time and forecasted weather data for multiple cities simultaneously, visualize this data through dynamic charts and maps, and download comprehensive reports in CSV, Excel, and PDF formats. The application is ideal for users who want a one-stop solution for monitoring and analyzing weather conditions across different regions quickly and efficiently.

The project integrates several APIs, data processing libraries, and visualization tools to deliver a professional-grade dashboard experience. With support for data export and visual summary, it serves both analytical and reporting needs. Its lightweight and responsive design makes it deployable on local systems or remote servers using platforms like Streamlit Cloud, Heroku, or AWS.

---

## 🎯 Objectives of the Project

* Fetch real-time weather and 5-day forecasts using the OpenWeatherMap API.
* Allow users to input multiple cities and compare weather data between them.
* Visualize data trends such as temperature, wind speed, and humidity using Plotly charts.
* Display geographical locations using interactive maps powered by Folium.
* Provide export options in multiple formats: CSV, Excel, and PDF.
* Deliver a professional, theme-toggle enabled UI for accessibility and aesthetics.

---

## 🧰 Tools & Technologies Used

### 🔹 Languages and Core Technologies:

* **Python 3.x** – Primary programming language for logic and functionality.
* **Streamlit** – For building an interactive web application interface.

### 🔹 APIs and Services:

* **OpenWeatherMap API** – Used to fetch current weather and 5-day forecast data.

  * Endpoint: `http://api.openweathermap.org/data/2.5/weather`
  * Forecast endpoint: `http://api.openweathermap.org/data/2.5/forecast`

### 🔹 Python Libraries:

* **requests** – For making HTTP requests to the weather API.
* **pandas** – For managing, cleaning, and processing weather data in tabular format.
* **plotly.express** – For creating dynamic, interactive plots for weather parameters.
* **folium** – For embedding interactive maps displaying city locations.
* **streamlit-folium** – For integrating Folium maps into the Streamlit frontend.
* **datetime / time** – For timestamp formatting and caching logic.
* **fpdf** – To generate downloadable PDF reports containing weather summaries.
* **base64 & BytesIO** – To handle file conversions and downloads within the Streamlit UI.

### 🔹 Development Platform / IDE:

* **Visual Studio Code (VS Code)** – Used for writing and debugging code. It supports Python linting, Git integration, and auto-formatting.
* OS: **Windows 10**

---

## 🧱 Application Features

### 🔹 1. Multi-City Input

* Accepts comma-separated city names.
* Sanitizes and processes user input to ensure valid API requests.

### 🔹 2. Real-Time Weather Display

* Shows current temperature, humidity, wind speed, and weather condition.
* Weather descriptions are formatted in title case for readability.
* Automatically updates every 10 minutes using Streamlit's `@st.cache_data(ttl=600)`.

### 🔹 3. Forecast Visualization

* Retrieves 5-day weather forecast in 3-hour intervals.
* Converts JSON forecast into a pandas DataFrame.
* Line charts are generated for:

  * Temperature trends
  * Wind speed trends
  * Humidity variation

### 🔹 4. Summary Charts

* Bar graphs show city-wise comparison for:

  * Temperature
  * Humidity
  * Wind Speed
  * Cloudiness

### 🔹 5. Interactive Map

* Uses Folium to plot the latitude and longitude of each city.
* Includes zoom and pan controls.
* Each marker is labeled with the city name.

### 🔹 6. Export Options

* Users can download the processed weather data in:

  * **CSV** format for Excel or spreadsheet applications.
  * **Excel (XLSX)** format with proper tabular layout.
  * **PDF** format containing each city’s data as text for offline sharing.

### 🔹 7. Dark Mode Toggle

* Theme switcher that allows toggling between light and dark modes using Streamlit’s `st.toggle()` feature.
* Applies custom CSS for dark background and white text for better readability at night.

---

## 📌 How to Run the Project

### 🛠️ Setup Instructions

1. **Clone or download the repository**:

   ```bash
   git clone <your_repo_link>
   cd weather_dashboard
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key** using Streamlit’s `secrets.toml`:

   * Create `.streamlit/secrets.toml` with:

     ```toml
     OPENWEATHER_API_KEY = "your_actual_api_key"
     ```

4. **Run the app**:

   ```bash
   streamlit run app.py
   ```

5. Open in your browser at `http://localhost:8501`.

---

## 🧩 Project Folder Structure

```
weather_dashboard/
├── app.py                  # Main Streamlit app
├── requirements.txt        # All required libraries
├── .streamlit/
│   └── secrets.toml        # API key for OpenWeatherMap
```

---

## 🏢 Applications and Real-World Use Cases

This dashboard has broad real-world utility across industries:

* **Meteorological Research**: Compare city-wide forecasts to identify trends or anomalies.
* **Travel & Tourism**: Help travel planners and tourists check weather across destinations.
* **Logistics & Transport**: Inform route planning and delivery operations.
* **Educational Projects**: Demonstrate real-time API use, data visualization, and reporting.
* **Corporate Use**: Generate location-specific weather reports for field teams or international branches.

---

## 🚀 Future Enhancements

* Add precipitation and UV index charts.
* Cache city coordinates to reduce API calls.
* Add date-range-based historical weather visualization using One Call API.
* Integrate with alert systems for weather warnings.

---

## ✅ Conclusion

The **Advanced Weather Dashboard** project is a full-featured, cross-functional application that demonstrates how various modern Python libraries can be combined to create a real-world, production-ready dashboard. With features like real-time data fetching, rich visualizations, map integration, and export tools, it offers a valuable resource for anyone needing timely and accessible weather insights.

![Image](https://github.com/user-attachments/assets/7d2b2db1-af0b-4ef5-98a0-4cc89427fd60)

![Image](https://github.com/user-attachments/assets/4abe1f88-b889-4e34-b62c-c33f12658044)

![Image](https://github.com/user-attachments/assets/9bee728c-449a-4998-9008-bc1e6fb52173)

![Image](https://github.com/user-attachments/assets/781c7335-fa2f-4660-87cf-ca7d4af81222)

![Image](https://github.com/user-attachments/assets/742ad2d7-e703-43a0-ab0b-eaac1654e16e)

![Image](https://github.com/user-attachments/assets/6bfbb39f-7196-44bc-b309-2564205c98c3)

![Image](https://github.com/user-attachments/assets/4f9faff1-6451-4425-80d3-975d3a61ec52)

![Image](https://github.com/user-attachments/assets/4c0d673a-5e33-4584-8653-482a391e86e4)


![Image](https://github.com/user-attachments/assets/9c91f841-070c-45fc-8f70-af4304e33b14)

![Image](https://github.com/user-attachments/assets/6d96c879-0cb7-4428-8889-489d2e4b354b)

![Image](https://github.com/user-attachments/assets/dc591776-46a3-4d84-b2c3-1050aee50d4f)




