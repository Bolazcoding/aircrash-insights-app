## ✈️ Air Crashes Analysis Dashboard

This project focuses on analyzing a **global dataset of air crashes** to uncover historical trends, fatality patterns, survival rates, and geographical impact.
The work is divided into two parts: **data exploration** in Jupyter Notebook and an **interactive Streamlit dashboard** for live insights.

## 🔎 What This Project Does

- Cleans and prepares aviation accident data.
- Performs exploratory data analysis (EDA) on crashes across decades.
- Builds visual insights into crash frequency, fatalities, operators, and aircraft types.
- Provides an interactive dashboard where users can filter and explore the dataset themselves.

## 📊 The Dataset

- **Records:** ~5,000 crash events
- **Time Frame:** Multiple decades of accident history

**Attributes include:**

- **Date-related:** Year, Month, Quarter, Day
- **Aircraft details:** Manufacturer, Model
- **Operators and Locations**
- **Victim data:** Passengers aboard, Fatalities (air + ground)

This allows for time-series analysis, geographic insights, and safety performance comparisons.

## 📌 Core Insights

- Some decades saw dramatic spikes in aviation accidents.
- A few countries and operators account for a large share of crashes and fatalities.
- Fatality counts vary widely — some incidents had complete survival while others were fully catastrophic.
- Certain aircraft manufacturers and models appear more often, likely due to larger fleets.
- Survival is correlated with the number of passengers aboard, though outcomes differ by crash type.

## 📈 Dashboard Highlights

**The Streamlit app provides:**

- **Key Metrics at a glance:** total crashes, passengers aboard, fatalities, survival rate.
- **Trend charts:** crashes per year, fatalities per decade, seasonal breakdown.
- **Top 10 views:** most crash-prone operators, manufacturers, and countries.
- **Comparisons:** aboard vs fatalities, survival ratios.
- **Visuals used:** bar charts, line plots, scatter plots, treemaps, and interactive Altair charts.

## 🛠 Tools & Libraries

- **Python** (core language)
- **Pandas** — cleaning and analysis
- **Matplotlib / Seaborn** — static plotting
- **Altair** — interactive charts
- **Squarify** — treemaps
- **Streamlit** — dashboard framework
- **Jupyter Notebook** — exploratory analysis

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Bolazcoding/aircrash-insights-app.git
cd aircrash-insights-app
```

#### 2. Install dependencies

pip install -r requirements.txt

#### 3. Run the Streamlit app (For the best experience, please view this app in Dark Mode)

streamlit run app.py

---

## ✍️ Author

Developed by Mobolaji Adelabu

🔗 GitHub: https://github.com/Bolazcoding/

🔗 LinkedIn: https://www.linkedin.com/in/adelabu-mobolaji-68791b243/
