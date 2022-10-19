# Load in imports
import numpy as np
import pandas as pd

# Create Cities and Towns for Dataset
cities = ['Galway', 'Dublin', 'Limerick',
          'Cork', 'Derry']

towns = ['Roscommon', 'Longford', 'Castlebar',
         'Sligo', 'Carrick-on-Shannon']

# Assign variables
n = len(cities)
m = len(towns)

# Create the Artificial Dataset with Headers
city_data = {'Temperature': np.random.normal(24, 3, n),
             'Humidity': np.random.normal(78, 2.5, n),
             'Wind': np.random.normal(15, 4, n)
             }

town_data = {'Temperature': np.random.normal(24, 3, m),
             'Humidity': np.random.normal(78, 2.5, m),
             'Wind': np.random.normal(15, 4, m)
             }

# Assign Dataframes to a Variable
df = pd.DataFrame(data=city_data, index=cities)
df2 = pd.DataFrame(data=town_data, index=towns)
print(df, "\n", "\n", df2) # Formatting for Printing
