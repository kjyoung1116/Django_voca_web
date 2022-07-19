import pandas as pd

data = pd.read_excel('voca.xlsx')
data_filtered = data.loc[data['장르']=='K_SAT']

print(len(data_filtered))

print(1033 //10 +1)
