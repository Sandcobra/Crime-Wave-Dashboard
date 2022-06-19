import pandas as pd
import requests
import datetime




r = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/4/query?outFields=*&where=1%3D1&f=geojson')
data = r.json()
new_data = data['features']


# CREATE DATAFRAME FROM MPD API
df = pd.DataFrame.from_dict(new_data, orient='columns')
df_output = pd.DataFrame()

for row in df.values:
    t = row[3]['REPORT_DAT']
    date = int(str(t)[:10])
    dt = datetime.datetime.fromtimestamp(date).strftime('%m-%d-%Y %H:%M:%S')
    # month = datetime.datetime.fromtimestamp(date).strftime('%m')
    offense = row[3]['OFFENSE']
    address = row[3]['BLOCK']
    ward = row[3]['WARD']
    cluster = row[3]['NEIGHBORHOOD_CLUSTER'] 
    latitude = row[3]['LATITUDE'] 
    longitude = row[3]['LONGITUDE'] 
    df1 =  pd.DataFrame({'date': [dt], 'offense': [offense], 'address': [address], 'ward': [ward], 'cluster': [cluster], 'latitude': [latitude], 'longitude': [longitude]})
    df_output = df1.append(df_output, ignore_index=True)
# print(df_output.sort_values(by='date', ascending=False))

# CREATE DATA FOR CRIME MAP BY WARD
ward1_all = df_output[df_output['ward'] == '1']
ward1_map = pd.DataFrame(ward1_all, columns=['latitude', 'longitude'])
ward2_all = df_output[df_output['ward'] == '2']
ward2_map = pd.DataFrame(ward2_all, columns=['latitude', 'longitude'])
ward3_all = df_output[df_output['ward'] == '3']
ward3_map = pd.DataFrame(ward3_all, columns=['latitude', 'longitude'])
ward4_all = df_output[df_output['ward'] == '4']
ward4_map = pd.DataFrame(ward4_all, columns=['latitude', 'longitude'])
ward5_all = df_output[df_output['ward'] == '5']
ward5_map = pd.DataFrame(ward5_all, columns=['latitude', 'longitude'])
ward6_all = df_output[df_output['ward'] == '6']
ward6_map = pd.DataFrame(ward6_all, columns=['latitude', 'longitude'])
ward7_all = df_output[df_output['ward'] == '7']
ward7_map = pd.DataFrame(ward7_all, columns=['latitude', 'longitude'])
ward8_all = df_output[df_output['ward'] == '8']
ward8_map = pd.DataFrame(ward8_all, columns=['latitude', 'longitude'])

clusters = (df_output.groupby(['offense','cluster']).size().unstack(fill_value=0)) # GROUPBY NEIGHBORHOOD CLUSTERS/WARD
wards = (df_output.groupby(['offense','ward']).size().unstack(fill_value=0)) # GROUPBY NEIGHBORHOOD CLUSTERS/WARD
wards_all = (df_output.groupby(['ward', 'offense'])) # GROUPBY NEIGHBORHOOD CLUSTERS/WARD
ward88 = df_output[['date', 'ward', 'offense']]

map_data = pd.DataFrame(df_output, columns=['latitude', 'longitude'])

# All Homicides by ward
ward1_homicide = wards['1']['HOMICIDE']
ward2_homicide = wards['2']['HOMICIDE']
ward3_homicide = wards['3']['HOMICIDE']
ward4_homicide = wards['4']['HOMICIDE']
ward5_homicide = wards['5']['HOMICIDE']
ward6_homicide = wards['6']['HOMICIDE']
ward7_homicide = wards['7']['HOMICIDE']
ward8_homicide = wards['8']['HOMICIDE']

# All Assaults w/Deadly Weapon by ward
ward1_adw = wards['1']['ASSAULT W/DANGEROUS WEAPON']
ward2_adw = wards['2']['ASSAULT W/DANGEROUS WEAPON']
ward3_adw = wards['3']['ASSAULT W/DANGEROUS WEAPON']
ward4_adw = wards['4']['ASSAULT W/DANGEROUS WEAPON']
ward5_adw = wards['5']['ASSAULT W/DANGEROUS WEAPON']
ward6_adw = wards['6']['ASSAULT W/DANGEROUS WEAPON']
ward7_adw = wards['7']['ASSAULT W/DANGEROUS WEAPON']
ward8_adw = wards['8']['ASSAULT W/DANGEROUS WEAPON']

# All Robberies by ward
ward1_rob = wards['1']['ROBBERY']
ward2_rob = wards['2']['ROBBERY']
ward3_rob = wards['3']['ROBBERY']
ward4_rob = wards['4']['ROBBERY']
ward5_rob = wards['5']['ROBBERY']
ward6_rob = wards['6']['ROBBERY']
ward7_rob = wards['7']['ROBBERY']
ward8_rob = wards['8']['ROBBERY']


