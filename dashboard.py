import streamlit as st
import pandas as pd
import numpy as np
from data import *

city = st.sidebar.selectbox(
     'Which City?',
     ('DC', 'New York', 'Miami'))

if city == 'DC':
    st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Featour.com%2Fwp-content%2Fuploads%2F2018%2F05%2Fwdc.jpg&f=1&nofb=1', width=400)
st.title("Crime Wave Dashboard")

st.sidebar.title("Options")

st.header(city)

crime1, crime2, crime3 = st.columns(3)


if city == 'DC':
    
    hood = st.sidebar.select_slider('Choose Hood',('Ward 1', 'Ward 2', 'Ward 3', 'Ward 4', 'Ward 5', 'Ward 6', 'Ward 7', 'Ward 8'))
    st.markdown(f"### {hood}")
    chart1, chart2 = st.columns(2)
    
    if hood == 'Ward 1':
        crime1.metric(label = "Homicide", value = f"{ward1_homicide}", delta = 1.5, delta_color='inverse')
        crime2.metric(label = "Assault w/Deadly Weapon", value = f"{ward1_adw}", delta = -2.5, delta_color='inverse')
        crime3.metric(label = "Robbery", value = f"{ward1_rob}", delta = 3.5, delta_color='inverse')
        ward1_list = {'Homicide': [ward1_homicide], 'ADW': [ward1_adw], 'Robbery': [ward1_rob]}
        chart1.map(ward1_map)
        chart2.dataframe(ward1_all.sort_values(by='date', ascending=False))
    if hood == 'Ward 2':
        crime1.metric(label = "Homicide", value = f"{ward2_homicide}", delta = 1.5, delta_color='inverse')
        crime2.metric(label = "Assault w/Deadly Weapon", value = f"{ward2_adw}", delta = -2.5, delta_color='inverse')
        crime3.metric(label = "Robbery", value = f"{ward2_rob}", delta = 3.5, delta_color='inverse')
        ward2_list = {'Homicide': [ward2_homicide], 'ADW': [ward2_adw], 'Robbery': [ward2_rob]}
        chart1.map(ward2_map)
        chart2.dataframe(ward2_all.sort_values(by='date', ascending=False))
    if hood == 'Ward 3':
        crime1.metric(label = "Homicide", value = f"{ward3_homicide}", delta = 1.5, delta_color='inverse')
        crime2.metric(label = "Assault w/Deadly Weapon", value = f"{ward3_adw}", delta = -2.5, delta_color='inverse')
        crime3.metric(label = "Robbery", value = f"{ward3_rob}", delta = 3.5, delta_color='inverse')
        ward3_list = {'Homicide': [ward3_homicide], 'ADW': [ward3_adw], 'Robbery': [ward3_rob]}
        chart1.map(ward3_map)
        chart2.dataframe(ward3_all.sort_values(by='date', ascending=False))
    if hood == 'Ward 4':
        crime1.metric(label = "Homicide", value = f"{ward4_homicide}", delta = 1.5, delta_color='inverse')
        crime2.metric(label = "Assault w/Deadly Weapon", value = f"{ward4_adw}", delta = -2.5, delta_color='inverse')
        crime3.metric(label = "Robbery", value = f"{ward4_rob}", delta = 3.5, delta_color='inverse')
        ward4_list = {'Homicide': [ward4_homicide], 'ADW': [ward4_adw], 'Robbery': [ward4_rob]}
        chart1.map(ward4_map)
        chart2.dataframe(ward4_all.sort_values(by='date', ascending=False))
    if hood == 'Ward 5':
        crime1.metric(label = "Homicide", value = f"{ward5_homicide}", delta = 1.5, delta_color='inverse')
        crime2.metric(label = "Assault w/Deadly Weapon", value = f"{ward5_adw}", delta = -2.5, delta_color='inverse')
        crime3.metric(label = "Robbery", value = f"{ward5_rob}", delta = 3.5, delta_color='inverse')
        ward5_list = {'Homicide': [ward5_homicide], 'ADW': [ward5_adw], 'Robbery': [ward5_rob]}
        chart1.map(ward5_map)
        chart2.dataframe(ward5_all.sort_values(by='date', ascending=False))
    if hood == 'Ward 6':
        crime1.metric(label = "Homicide", value = f"{ward6_homicide}", delta = 1.5, delta_color='inverse')
        crime2.metric(label = "Assault w/Deadly Weapon", value = f"{ward6_adw}", delta = -2.5, delta_color='inverse')
        crime3.metric(label = "Robbery", value = f"{ward6_rob}", delta = 3.5, delta_color='inverse')
        ward6_list = {'Homicide': [ward6_homicide], 'ADW': [ward6_adw], 'Robbery': [ward6_rob]}
        chart1.map(ward6_map)
        chart2.dataframe(ward6_all.sort_values(by='date', ascending=False))
    if hood == 'Ward 7':
        crime1.metric(label = "Homicide", value = f"{ward7_homicide}", delta = 1.5, delta_color='inverse')
        crime2.metric(label = "Assault w/Deadly Weapon", value = f"{ward7_adw}", delta = -2.5, delta_color='inverse')
        crime3.metric(label = "Robbery", value = f"{ward7_rob}", delta = 3.5, delta_color='inverse')
        ward7_list = {'Homicide': [ward7_homicide], 'ADW': [ward7_adw], 'Robbery': [ward7_rob]}
        chart1.map(ward7_map)
        chart2.dataframe(ward7_all.sort_values(by='date', ascending=False))
    if hood == 'Ward 8':
        crime1.metric(label = "Homicide", value = f"{ward8_homicide}", delta = 1.5, delta_color='inverse')
        crime2.metric(label = "Assault w/Deadly Weapon", value = f"{ward8_adw}", delta = -2.5, delta_color='inverse')
        crime3.metric(label = "Robbery", value = f"{ward8_rob}", delta = 3.5, delta_color='inverse')
        ward8_list = {'Homicide': [ward8_homicide], 'ADW': [ward8_adw], 'Robbery': [ward8_rob]}
        chart1.map(ward8_map)
        chart2.dataframe(ward8_all.sort_values(by='date', ascending=False))


if city == 'New York':
    st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhbkcpa.com%2Fwp-content%2Fuploads%2F2020%2F03%2Fnew-york-city-1536x1024.jpg&f=1&nofb=1')
    st.subheader('Coming Soon')

if city == 'Miami':
    st.image('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.natgeofe.com%2Fn%2F4e57f727-4dfd-4f7d-9c27-9edd6f73cfd0%2Fmiami-travel.jpg%3Fw%3D1200&f=1&nofb=1')
    st.subheader('Coming Soon')

    
        