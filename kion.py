# Create a DataFrame for tests
import pandas as pd
import numpy as np

# prepare dictionary

figures ={'City' : ['Sapporo', 'Sendai', 'Niigata', 'Tokyo', 'Nagoya', 'Osaka', 'Fukuoka', 'Naha'],
             'Saturday': [30, 26, 29, 32, 33, 32, 31, 28], 
               'Sunday': [33, 31, 31, 32, 34, 32, 32, 27]}

# convert to DataFrame
kion = pd.DataFrame(figures)

# set 'City' as Index
kion = kion.set_index('City')

# Add a column
kion_diff = kion
kion_diff['Diff'] = kion['Saturday'] - kion['Sunday']

# Rename
df = kion