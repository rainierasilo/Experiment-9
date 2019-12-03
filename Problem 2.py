import pandas as pd

x = {'Box': ['Box1', 'Box1', 'Box1', 'Box2', 'Box2', 'Box2'], 
     'Dimension': ['Length','Width','Height','Length','Width','Height'], 
     'Value': [6,4,2,5,3,4]}

messy = pd.DataFrame(x, columns = ['Box','Dimension', 'Value'])

tidy = messy.pivot_table(index = ['Box'], columns = 'Dimension', values = 'Value').reset_index()

volume = [48, 60]

tidy['Volume'] = volume