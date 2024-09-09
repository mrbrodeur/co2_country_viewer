import streamlit as st
import pandas as pd

df = pd.read_csv('co2_data.csv')
for_chart = pd.DataFrame()
"Show the CO2 emissions for a country"

options = st.multiselect(
    'Select a Country',
     df["Country or Area"].unique())

print(options)

for country in options:
    to_add = df.loc[df["Country or Area"] == country, ["Year", "Value"]]
    to_add = to_add.rename(columns={"Value": country}).set_index("Year")
    if len(for_chart) == 0:
        for_chart = to_add
    else:
        for_chart[country] = to_add[country]

print(for_chart)

st.line_chart(for_chart, x_label="Year", y_label="CO2 emissions")

