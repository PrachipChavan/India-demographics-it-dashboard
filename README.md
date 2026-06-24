# India-demographics-it-dashboard using Streamlit
Interactive data visualization explorer for India's demographics, languages, and technology landscape built with Streamlit and Plotly.

🇮🇳 **India Insights** is an interactive, modern, and colorful Streamlit web application designed to visualize and analyze India's demographics, spoken languages, and growing IT industry footprint.

This project is built to demonstrate data analysis (EDA), custom interactive charting, and stateful user authentication inside a sleek glassmorphic dark-theme UI.

---

## 🚀 Key Features

* **🔐 Stateful Authentication**: Access-controlled dashboard featuring a custom-styled Login page and a Logout button.
* **🔍 Search & Filter Panels**: Dynamic sidebar filters to search regions (States/UTs) by name, type, population size, primary/secondary languages, or IT company density.
* **📊 Visual Data Analytics**:
  * **Interactive Pie Charts**: Visual distribution of primary spoken languages and IT companies concentration across India.
  * **Demographics Bar Charts**: Horizontally-sorted population representation per state or union territory.
  * **Salary vs. IT Density Scatter Plot**: Deep dive into average IT packages (LPA) against company counts, sized by population.
* **📈 Exploratory Data Analysis (EDA)**:
  * Heatmaps showcasing feature correlations.
  * Comprehensive statistical tables (`mean`, `median`, `std dev`, `min/max`).
* **📥 Data Exporter**: Seamless button to download the filtered or full dataset directly as a CSV file.
* **🎨 Modern Aesthetic**: Loaded with custom CSS variables, custom typography, gradient highlights, and hover-triggered micro-animations.

---

## 📁 Repository Structure

```text
india_dashboard/
├── .streamlit/
│   └── config.toml          # Custom theme configuration (natively forces white text)
├── assets/
│   ├── styles.css           # Glassmorphic UI designs & text color overrides
│   └── dashboard_banner.png # Generated header vector graphics 
├── app.py                   # Core dashboard logic, tabs, and charts
├── auth.py                  # Credentials validation & login form layout
├── generate_data.py         # Mock dataset creator (generates the CSV file)
├── india_demographics.csv   # The source dataset (States, Pop, Languages, IT data)
└── README.md                # Project documentation

## 🔑 Demo Access Credentials

Once the dashboard launches in your browser, log in with the following default credentials:

* **Username:** `admin`
* **Password:** `india@2026`

---

## 🛠️ Technologies Used

* **Language**: Python 3
* **App Framework**: Streamlit
* **Data Processing**: Pandas
* **Data Visualization**: Plotly Express, Plotly Graph Objects
* **Styling**: Custom CSS and HTML5
