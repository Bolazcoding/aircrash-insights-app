import pandas as pd
import streamlit as st

def load_data():
   df = pd.read_excel("aircrashes_data_cleaned.xlsx")
   return df
try:
   df = load_data()


   st.title("Aircrashes Insights App")

   filters = {
   "Year": df["Year"].unique(),
   "Month": df["Month"].unique(),
   "Aircraft": df["Aircraft"].unique(),
   "Aircraft Manufacturer": df["Aircraft Manufacturer"].unique(),
   "Country/Region": df["Country/Region"].unique(),
   }

   selected_filters = {}

   # Creating filters in sidebar dynamically
   for key, options in filters.items():
   
      selected_filters[key] = st.sidebar.multiselect(key, sorted(options))

   # Filtered data
   filtered_df = df.copy()
   for key, selected_values in selected_filters.items():
      if selected_values:
         filtered_df = filtered_df[filtered_df[key].isin(selected_values)]

   # KPIs
   total_crashes = len(filtered_df)
   total_fatalities = filtered_df["Fatalities(air)"].sum()
   total_passengers = filtered_df["Aboard"].sum()
   avg_fatality_rate = round((total_fatalities / total_passengers) * 100, 2)

   #streamlit column components
   col1 , col2, col3, col4 = st.columns(4)

   with col1:
      st.metric("Total Crashes", total_crashes)

   with col2:
      st.metric("Total Fatalities", f"{total_fatalities:,}")

   with col3:
      st.metric("Total Passengers", f"{total_passengers:,}")
   
   with col4:
      st.metric("Average Fatality Rate", f"{avg_fatality_rate:,}")
   

   # display the Filtered Table 
   st.dataframe(filtered_df)

   st.write("### Analysis Findings")
   # RQ1
   st.write("#### 1. Number of Air crashes per year")
   # Full list for table
   temp1 = (
   filtered_df.groupby("Year").size().reset_index(name="Crash Count")
   .sort_values("Crash Count", ascending=False)
   )
   st.dataframe(temp1)
   # Top 10 for chart
   temp1c= temp1.head(10)


   # plotting a bar chart
   import altair as alt
   chart1 = alt.Chart(temp1c).mark_bar().encode(
      x=alt.X("Year:N",
         sort=alt.SortField(field="Crash Count", order="descending"),
         axis=alt.Axis(title="Year", labelAngle=45),
      ),
      y=alt.Y("Crash Count:Q", axis=alt.Axis(title="Number of Air Crashes")),
      color=alt.Color("Crash Count:Q", legend=None),
      tooltip=["Year:N", "Crash Count:Q"],
   ).properties( height=320)
   
   # displaying the chart
   st.altair_chart(chart1, use_container_width=True)

   # RQ2: Trend of air crashes over time
   st.write("#### 2. Trend of Air Crashes Over Time")
   temp2 = df.groupby("Year").size().reset_index(name="Crash Count")
   st.dataframe(temp2)
   chart2 = alt.Chart(temp2).mark_line(point=True).encode(
   x=alt.X("Year:N", axis=alt.Axis(title="Year", labelAngle=45)),
   y=alt.Y("Crash Count:Q", axis=alt.Axis(title="Number of Crashes")),
   tooltip=["Year:N", "Crash Count:Q"]
   ).properties(height=320)
   st.altair_chart(chart2, use_container_width=True)

   
   # RQ3: Countries with highest crashes
   st.write("#### 3. Top 10 Countries with Most Air Crashes")

   temp3 = df["Country/Region"].value_counts().reset_index()
   temp3.columns = ["Country/Region", "Crash Count"]
   st.dataframe(temp3)
   temp3c = temp3.head(10)
   chart3 = alt.Chart(temp3c).mark_bar().encode(
      x=alt.X("Crash Count:Q", axis=alt.Axis(title="Number of Crashes")),
      y=alt.Y("Country/Region:N", sort="-x", axis=alt.Axis(title="Country/Region")),
      color=alt.Color("Crash Count:Q", legend=None),
      tooltip=["Country/Region:N", "Crash Count:Q"]
   ).properties(height=320)

   st.altair_chart(chart3, use_container_width=True)


  # RQ4: Aircraft manufacturers with most crashes
   st.write("#### 4. Top 10 Aircraft Manufacturers with Most Crashes")

   temp4 = df["Aircraft Manufacturer"].value_counts().reset_index()
   temp4.columns = ["Manufacturer", "Crash Count"]
   st.dataframe(temp4)
   temp4c = temp4.head(10)
   chart4 = alt.Chart(temp4c).mark_bar().encode(
      x=alt.X("Crash Count:Q", axis=alt.Axis(title="Number of Crashes")),
      y=alt.Y("Manufacturer:N", sort="-x", axis=alt.Axis(title="Manufacturer")),
      color=alt.Color("Crash Count:Q", legend=None),
      tooltip=["Manufacturer:N", "Crash Count:Q"]
   ).properties(height=320)

   st.altair_chart(chart4, use_container_width=True)

   # RQ5: Average fatality rate by operator type
   st.write("#### 5. Average Fatality Rate by Operator Type")

   temp5 = df.groupby("Operator Type")["Fatality Rate(%)"].mean().reset_index().sort_values("Fatality Rate(%)", ascending=False)
   st.dataframe(temp5)
   chart5 = alt.Chart(temp5).mark_bar().encode(
      x=alt.X("Fatality Rate(%):Q", axis=alt.Axis(title="Average Fatality Rate (%)")),
      y=alt.Y("Operator Type:N", sort="-x", axis=alt.Axis(title="Operator Type")),
      color=alt.Color("Fatality Rate(%):Q", legend=None),
      tooltip=["Operator Type:N", "Fatality Rate(%):Q"]
   ).properties(height=320)

   st.altair_chart(chart5, use_container_width=True)


   # RQ6: Operators with most crashes
   st.write("#### 6. Top 10 Operators with Most Crashes")

   temp6 = df["Operator"].value_counts().reset_index()
   temp6.columns = ["Operator", "Crash Count"]
   st.dataframe(temp6)
   temp6c = temp6.head(10)
   chart6 = alt.Chart(temp6c).mark_bar().encode(
      x=alt.X("Crash Count:Q", axis=alt.Axis(title="Number of Crashes")),
      y=alt.Y("Operator:N", sort="-x", axis=alt.Axis(title="Operator")),
      color=alt.Color("Crash Count:Q", legend=None),
      tooltip=["Operator:N", "Crash Count:Q"]
   ).properties(height=320)

   st.altair_chart(chart6, use_container_width=True)

   # RQ7: Crashes by quarter
   st.write("#### 7. Number of Crashes by Quarter")

   temp7 = df.groupby("Quarter").size().reset_index(name="Crash Count").sort_values("Quarter")
   st.dataframe(temp7)
   chart7 = alt.Chart(temp7).mark_bar().encode(
      x=alt.X("Quarter:N", axis=alt.Axis(title="Quarter")),
      y=alt.Y("Crash Count:Q", axis=alt.Axis(title="Number of Crashes")),
      color=alt.Color("Crash Count:Q", legend=None),
      tooltip=["Quarter:N", "Crash Count:Q"]
   ).properties(height=320)

   st.altair_chart(chart7, use_container_width=True)

   # RQ8: Total aboard vs fatalities
   st.write("#### 8. Total Number of People Aboard vs Fatalities")

   temp8 = pd.DataFrame({
      "Category": ["Aboard", "Fatalities"],
      "Count": [df["Aboard"].sum(), df["Fatalities(air)"].sum()]
   })
   st.dataframe(temp8)
   chart8 = alt.Chart(temp8).mark_bar().encode(
      x=alt.X("Category:N", axis=alt.Axis(title="Category")),
      y=alt.Y("Count:Q", axis=alt.Axis(title="Count of People")),
      color=alt.Color("Category:N", legend=None),
      tooltip=["Category:N", "Count:Q"]
   ).properties(height=320)

   st.altair_chart(chart8, use_container_width=True)

   # RQ9: Fatalities by decade
   st.write("#### 9. Total Fatalities by Decade")

   df["Decade"] = (df["Year"] // 10) * 10
   temp9 = df.groupby("Decade")["Fatalities(air)"].sum().reset_index()
   st.dataframe(temp9)
   chart9 = alt.Chart(temp9).mark_bar().encode(
      x=alt.X("Decade:N", axis=alt.Axis(title="Decade")),
      y=alt.Y("Fatalities(air):Q", axis=alt.Axis(title="Total Fatalities")),
      color=alt.Color("Fatalities(air):Q", legend=None),
      tooltip=["Decade:N", "Fatalities(air):Q"]
   ).properties(height=320)

   st.altair_chart(chart9, use_container_width=True)

   # RQ10: Deadliest crashes
   st.write("#### 10. Top 10 Deadliest Crashes")

   deadliest = df[['Year', 'Country/Region', 'Aircraft', 'Operator', 'Fatalities(air)', 'Aboard']]\
      .sort_values(by="Fatalities(air)", ascending=False).head(10)
   st.dataframe(deadliest)
   chart10 = alt.Chart(deadliest).mark_bar().encode(
      x=alt.X("Fatalities(air):Q", axis=alt.Axis(title="Fatalities (Air)")),
      y=alt.Y("Operator:N", sort="-x", axis=alt.Axis(title="Operator")),
      color=alt.Color("Fatalities(air):Q", legend=None),
      tooltip=["Year:N", "Operator:N", "Fatalities(air):Q", "Aboard:Q"]
   ).properties(height=320)

   st.altair_chart(chart10, use_container_width=True)


except Exception as e:
    st.error("Error: check error details")

    with st.expander("Error Details"):
        st.code(str(e))
