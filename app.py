# streamlit run app.py 
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.express as px


st.title("Urban Sustainability Clustering")
st.header("Predict Country Sustainability Clusters")


col1, col2 = st.columns(2)

with col1:
    green_space = st.number_input("Green Space %", value=30.0)
    air_quality = st.number_input("Air Quality Index", value=50.0)
    waste_recycled = st.number_input("Waste Recycled", value=40.0)
    renewable_energy = st.number_input("Renewable Enery", value=20.0)
    carbon_emision = st.number_input("Carbon Emision", value=30.0)
    

with col2:
    energy_efficiency = st.number_input("Energy Efficient", value=70.0)
    avg_commute = st.number_input("Average Commute Time", value=35.0)
    water_access = st.number_input("Water Access", value=80.0)
    population = st.number_input("Population", value=5.0)


country = st.selectbox("Select a country for the map",
                       ['Argentina','Australia','Brazil','Canada','China','Denmark','Egypt','Finland','France','Germany','India','Indonesia','Iran','Iraq','Italy','Kenya','Mexico','New Zealand','Nigeria','Pakistan','Peru','Philippines','Qatar','Russia','Saudi Arabia','South Africa','Spain','Sweden','Switzerland','Thailand','Turkey','United Arab Emirates','United Kingdom','United States','Vietnam'])

if st.button("Predict Cluster"):
    CLUSTER_INFO = {0:"Transitional Cties", 1:"Critical Intervention Zone", 2:"Sustaibility Leaders"}
    
    model = joblib.load("model_sustainability.joblib")
    scaler = joblib.load("scaler_sustainability.joblib")
    
    input_data = np.array([[green_space, air_quality, waste_recycled, renewable_energy, 
                            carbon_emision, energy_efficiency, avg_commute, water_access, population]])
    
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    
    if prediction == 0:
        st.warning(f"Prediction Result: {CLUSTER_INFO[prediction]}")
    elif prediction == 1:
        st.error(f"Prediction Result: {CLUSTER_INFO[prediction]}")
    else:
        st.success(f"Prediction Result: {CLUSTER_INFO[prediction]}")

    df = pd.DataFrame({"country": [country], "cluster_label": [CLUSTER_INFO[prediction]]})

    fig = px.choropleth(
        df,
        locationmode="country names",
        locations="country",
        color="cluster_label",
        hover_name="country",
        title="Sustainability clustering per cities",
        color_discrete_map={
            "Transitional Cties": "yellow",
            "Critical Intervention Zone": "red",
            "Sustaibility Leaders": "green"
        }
    )
    
    st.plotly_chart(fig, use_container_width=True)
