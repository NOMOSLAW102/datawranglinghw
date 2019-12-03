import pandas as pd
x = pd.DataFrame({'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]})
tidyx=x.pivot_table(index=['Box'],columns='Dimension',values='Value')
tidyx['Volume'] = tidyx.Length*tidyx.Height*tidyx.Width
print(tidyx)