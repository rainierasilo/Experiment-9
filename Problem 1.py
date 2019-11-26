import pandas as pd

a = {'Student': ['Ice Bear', 'Panda' ,'Grizzly'],
     'Math': [80,95,79]}
b = {'Student': ['Ice Bear', 'Panda' ,'Grizzly'],
     'Electronics': [85,81,83]}
c = {'Student': ['Ice Bear', 'Panda' ,'Grizzly'],
     'GEAS': [90,79,93]}
d = {'Student': ['Ice Bear', 'Panda' ,'Grizzly'],
     'ESAT': [93,89,88]}

math = pd.DataFrame(a, columns=['Student', 'Math'])
electronics = pd.DataFrame(b, columns=['Student', 'Electronics'])
geas = pd.DataFrame(c, columns=['Student', 'GEAS'])
esat = pd.DataFrame(d, columns=['Student', 'ESAT'])

e = pd.merge(math, electronics, how = 'outer', on = 'Student')
f =  pd.merge(geas, esat, how = 'outer', on = 'Student')

final = pd.merge (e,f, how = 'outer', on = 'Student')

print(final)



