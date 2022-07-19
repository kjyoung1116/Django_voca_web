import csv
import pandas as pd


data = pd.read_csv('voca.csv', encoding = 'UTF-8')

data_filtered= data.loc[data['장르'] == 'GRE']

voca = data_filtered['단어']
meaning = data_filtered['의미']
sentence = data_filtered['예문']
significance = data_filtered['중요도']
difficulty = data_filtered['난이도']
number = data_filtered['번호']
genre = data_filtered['장르']
        
voca_data = []
for i in zip(voca,meaning,sentence, significance, difficulty, number):
    voca_data.append(i)

print(voca_data)