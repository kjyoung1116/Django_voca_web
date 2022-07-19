from django.shortcuts import render
import csv
import pandas as pd

# Create your views here.

def search(request):
    data = pd.read_excel('voca.xlsx')
    
    voca_data = []
    
    if 'q' in request.GET:
        query = request.GET.get('q')
        data = pd.read_excel('voca.xlsx')
        df = pd.DataFrame(data)
        data = data[df['유의어'].str.contains(query,na=False) | df['단어'].str.contains(query,na=False) | df['의미'].str.contains(query,na=False)]

        voca = data['단어']
        meaning = data['의미']
        sentence = data['예문']
        significance = data['중요도']
        difficulty = data['난이도']
        number = data['번호']
        synonym = data['유의어']
    
        for i in zip(voca,meaning,sentence, significance, difficulty, number,synonym):
            voca_data.append(i)

        if len(voca_data) > 0:
            return render(request, '../templates/search.html', {'voca_data': voca_data, 'query': query})
        else:
            no_data = '검색 결과가 없습니다.'
            return render(request, '../templates/search.html', {'no_data':no_data, 'query': query})

