import numpy as np
import pandas as pd

data = {'name' :['tama', 'pochi', 'taro', 'jiro', 'mike'] ,
    'type' : ['cat', 'dog', 'dog', 'cat', 'cat'], 
    'gender' : ['f', 'm', 'm', 'm', 'f'],
    'age' : [2, 3, 5, 4, 10],
    'location' : ['Tokyo', 'Osaka', 'Sapporo', 'Tokyo', 'Tokyo'],
    'Ins_follow': [4000, 850, 51500, 84800, 1200],
    'Tw_follow': [1200, 400, 26900, 48300, 450],
    'Is_pro' : [False, False, True, True, False] }

dfp0 = pd.DataFrame(data)

dfp = dfp0.set_index('name')

print(dfp)
