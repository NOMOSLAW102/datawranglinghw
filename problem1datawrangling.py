import pandas as pd
math = pd.DataFrame({'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]})
electronics = pd.DataFrame({'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]})
geas = pd.DataFrame({'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]});
esat = pd.DataFrame({'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]});
merge1 = pd.merge (math,electronics, on='Student')
merge2 = pd.merge (geas,esat, on='Student')
mergefinal = pd.merge (merge1,merge2, on='Student')
long=pd.melt(mergefinal,id_vars=['Student'],var_name='Subject', value_name='Grades')
print(long)