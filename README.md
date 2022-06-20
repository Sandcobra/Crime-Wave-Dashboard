![Crime_Wave_Banner](https://user-images.githubusercontent.com/20058009/174626710-23055f36-ece9-4686-a808-8de222bb98d0.png)

![https://img.shields.io/badge/python-streamlit-blue](https://img.shields.io/badge/python-streamlit-blue)
[![GitHub license](https://img.shields.io/github/license/Sandcobra/Crime-Wave-Dashboard)](https://github.com/Sandcobra/Crime-Wave-Dashboard/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Sandcobra/Crime-Wave-Dashboard)](https://github.com/Sandcobra/Crime-Wave-Dashboard/issues)

Display crime data for various cities

This app uses python streamlit library to display crime data for cities like Washington DC. The crime data are broken down into neighborhoods to help users better understand how dangerous a area is with points on a map that visualize the crime data.

## Run Locally
```bash
Run git clone https://github.com/Sandcobra/Crime-Wave-Dashboard.git
Run pip install -r requirements.txt
Run streamlit run dashboard.py
```

- Streamlit has a simple setup to get a dashboard up and running quickly
- Create a sidebar with select boxes for easy clean navigation
- Add page titles and a header without inserting any HTML

![crimewave_code](https://user-images.githubusercontent.com/20058009/174624366-f796e886-bf4a-4cbb-ab4c-5d80118e935a.png)
![sidebar](https://user-images.githubusercontent.com/20058009/174631863-d8878ff0-be8e-48d1-a8c5-2b8c5056a39b.JPG)

## Visualize the Data
- The Dashboard displays Homicides, Assault w/Deadly Weapon and Robbery crimes
- Users can view the violent crimes happening near them
- Users can view the increase or decrease in violent crime trends


![crime _stats](https://user-images.githubusercontent.com/20058009/174632652-57f9299e-2771-41f6-a63e-ca4d995e1686.JPG)


- Change neighborhoods using the selector 
- Users can zoom in on the map to see exactly where crimes are occuring
- Users can scroll through the raw data in the crime table to see all crimes

![crime_map](https://user-images.githubusercontent.com/20058009/174633508-d60fbcbb-8ce3-4940-9cf6-922d22bc06da.JPG)
