# Test script

"""
Use this to do the development
"""

"""1. load data"""
#use pandas to import  csv file
import pandas as pd
inc_df = pd.read_csv('Data/incident_data.csv')
inc_df = inc_df.drop(columns='Unnamed: 0')

inc_df.columns # Columns
inc_df.index # Rows
inc_df.loc[0,:] # first entry 


inc_df.loc[:, 'COD_SONDA'] # column 
inc_df.iloc[:, 0]

inc_df.loc[0, 'COD_SONDA'] 


"""2. build incident objects"""
from SRC.incident import Incident

['COD_SONDA', 'NK_INC','DAT_PRIMEIRA_OBS', 'NUM_LATITUDE', 'NUM_LONGITUDE']


test1 = Incident(*inc_df.loc[0, ['COD_SONDA', 'NK_INC',
                                'DAT_PRIMEIRA_OBS', 'NUM_LATITUDE', 'NUM_LONGITUDE']].values)

float(inc_df.loc[:, 'NUM_LATITUDE'].values[0].replace(',', '.'))

def convert_loc_string(pos):
    if isinstance(pos,str):
        return float(pos.replace(',', '.'))
    else:
        return pos

lat = []
lon = []
for i in inc_df.index:
    lat.append(convert_loc_string(inc_df.loc[i, 'NUM_LATITUDE']))
    lon.append(convert_loc_string(inc_df.loc[i, 'NUM_LONGITUDE']))

inc_df['NUM_LATITUDE'] = lat
inc_df['NUM_LONGITUDE'] = lon

"""3. plot data"""
