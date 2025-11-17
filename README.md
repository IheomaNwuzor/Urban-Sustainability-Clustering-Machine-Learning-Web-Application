# Urban-Sustainability-Clustering-Machine-Learning-Web-Application
![Image 7](https://github.com/user-attachments/assets/72002e3a-04d2-41da-8600-3463775fd64c)

### An interactive Streamlit app for clustering countries based on sustainability indicators using machine learning and visualizing results on a global map.

# 🔍 Overview
This project applies machine learning clustering to classify countries into sustainability categories based on environmental, economic, and social metrics. Users can interactively adjust multiple indicators, such as renewable energy use, green space, carbon emissions, and water access and instantly visualize clustering results on a geospatial map.

# 🧩 Key Features
•	Interactive Streamlit Interface
User-friendly UI with numeric sliders and country selection.
•	Machine Learning Clustering Model
Uses a pre-trained and scaled clustering model for real-time predictions.
•	Dynamic Choropleth Map
Plotly Express visualizes sustainability clusters on a global map.
•	Custom Alerts

# Color-coded prediction messages:
o	🟢 Sustainability Leaders
o	🟡 Transitional Cities
o	🔴 Critical Intervention Zones
•	Instant Inference
Inputs are scaled, processed, and clustered in real-time.

# 📸 Application Screenshot
🧠 Tech Stack
•	Python 3.8+
•	Streamlit
•	scikit-learn
•	Plotly Express
•	NumPy & Pandas
•	Joblib

# 📁 Project Structure
urban-sustainability-clustering/
│
├── app.py
├── model_sustainability.joblib
├── scaler_sustainability.joblib
├── requirements.txt
├── README.md
└── assets/
      └── screenshot.png

# 🧮 How It Works
1.	User inputs sustainability indicators such as:
o	Green space percentage
o	Air quality index
o	Carbon emission
o	Renewable energy usage
o	Waste recycled
o	Energy efficiency
o	Water access
o	Population
2.	Inputs are converted into a NumPy array.
3.	Values are standardized via a trained scaler.
4.	A saved ML model predicts and assigns a sustainability cluster.
5.	A colored choropleth map highlights the selected country under its predicted cluster category.

# 🗂️ Model Explanation
•	The clustering model groups countries into three sustainability categories:
o	Cluster 0 — Transitional Cities
o	Cluster 1 — Critical Intervention Zone
o	Cluster 2 — Sustainability Leaders
•	Features were standardized using StandardScaler before fitting the clustering model.
🔮 Future Improvements
•	Add city-level sustainability datasets
•	Integrate more indicators (public transport, GDP, health index)
•	Introduce deep learning for sustainability scoring
•	Add time-series prediction for forecasting improvements
•	Deploy to cloud services (Streamlit Cloud, AWS, GCP, Azure)

# 📜 License
MIT License (optional, depending on your preference)

