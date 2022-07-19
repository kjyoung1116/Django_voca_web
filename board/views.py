from django.shortcuts import render

import pandas as pd
from .models import learn_review_custom


# ----------------------------------------------------------------------------------------------------------------------
def index(request):
    return render(request, "../templates/index.html")
# ----------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
def learn_review(request):

    return render(request, "../templates/learn_review.html")
# ----------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
def K_SAT(request, param):
    K_SAT_len = []
    data = pd.read_excel('voca.xlsx')
    data_filtered = data.loc[data['장르']=='K_SAT']
    len_voca = len(data_filtered)

    if len_voca % 10 > 0:
        len_voca = len_voca // 10 + 1
    else:
        len_voca = len_voca // 10

    for i in range((int(param)-1)*10+1,int(param)*10+1):
        if i <= len_voca: 
            K_SAT_len.append(str(i))

    page = int(param)
    previous_page = int(param)-1
    next_page = int(param)+1
    len_page = len_voca //10 +1
    range_len_page = range(1,len_page+1)
    return render(request, "../templates/K_SAT.html", {'K_SAT_len' : K_SAT_len, 'page':page, 'previous_page':previous_page,'next_page':next_page,'len_page':len_page,'range_len_page':range_len_page})

def K_SATdetail(request, param):
    data = pd.read_excel('voca.xlsx')
    data_filtered = data.loc[data['장르']=='K_SAT']
    data_filtered2 = data_filtered[(int(param)-1)*10:int(param)*10]
    voca = data_filtered2['단어']
    meaning = data_filtered2['의미']
    sentence = data_filtered2['예문']
    significance = data_filtered2['중요도']
    difficulty = data_filtered2['난이도']
    number = range((int(param)-1)*10+1,int(param)*10+10)
    synonym = data_filtered2['유의어']

    voca_data = []

    for i in zip(voca,meaning,sentence, significance, difficulty, number,synonym):
        voca_data.append(i)

    len_page = len(data_filtered)//10 +1
    param = int(param)

    next_page = int(param)+1
    prev_page = int(param)-1
    next_page_ment = '다음 10단어 (%d~%d)' %(int(param)*10+1, (int(param)+1)*10)
    prev_page_ment = '이전 10단어 (%d~%d)' %((int(param)-2)*10+1, (int(param)-1)*10)
    list_page_ment = '단어목록으로 가기'
    if int(param) % 10 > 0:
        list_page = int((int(param) - int(param) % 10)/10 +1)
    else:
        list_page = int(int(param) /10)

    return render(request, "../templates/K_SATdetail.html", {'list_page_ment': list_page_ment,'list_page':list_page, 'len_page':len_page,'param':param,'voca_data':voca_data, 'next_page':next_page, 'next_page_ment':next_page_ment,'prev_page':prev_page, 'prev_page_ment':prev_page_ment})
# ----------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
def alphabet(request, param):
    alphabet_len = []
    data = pd.read_excel('voca.xlsx')
    data_filtered = data.sort_values(by = '단어')
    len_voca = len(data_filtered)

    if len_voca % 10 > 0:
        len_voca = len_voca // 10 + 1
    else:
        len_voca = len_voca // 10

    for i in range((int(param)-1)*10+1,int(param)*10+1):
        if i <= len_voca: 
            alphabet_len.append(str(i))

    page = int(param)
    previous_page = int(param)-1
    next_page = int(param)+1
    len_page = len_voca //10 +1
    range_len_page = range(1,len_page+1)
    return render(request, "../templates/alphabet.html", {'alphabet_len' : alphabet_len, 'page':page, 'previous_page':previous_page,'next_page':next_page,'len_page':len_page,'range_len_page':range_len_page})

def alphabet_detail(request, param):
    data = pd.read_excel('voca.xlsx')
    data_filtered = data.sort_values(by = '단어')
    data_filtered2 = data_filtered[(int(param)-1)*10:int(param)*10]
    voca = data_filtered2['단어']
    meaning = data_filtered2['의미']
    sentence = data_filtered2['예문']
    significance = data_filtered2['중요도']
    difficulty = data_filtered2['난이도']
    number = range((int(param)-1)*10+1,int(param)*10+10)
    synonym = data_filtered2['유의어']

    voca_data = []

    for i in zip(voca,meaning,sentence, significance, difficulty, number,synonym):
        voca_data.append(i)

    len_page = len(data_filtered)//10 +1
    param = int(param)
    
    next_page = int(param)+1
    prev_page = int(param)-1
    next_page_ment = '다음 10단어 (%d~%d)' %(int(param)*10+1, (int(param)+1)*10)
    prev_page_ment = '이전 10단어 (%d~%d)' %((int(param)-2)*10+1, (int(param)-1)*10)
    list_page_ment = '단어목록으로 가기'
    if int(param) % 10 > 0:
        list_page = int((int(param) - int(param) % 10)/10 +1)
    else:
        list_page = int(int(param) /10)

    return render(request, "../templates/alphabet_detail.html", {'list_page_ment': list_page_ment,'list_page':list_page, 'len_page':len_page,'param':param,'voca_data':voca_data, 'next_page':next_page, 'next_page_ment':next_page_ment,'prev_page':prev_page, 'prev_page_ment':prev_page_ment})
# ----------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------------
def confusing(request):
    confusing_len = []
    data = pd.read_excel('voca.xlsx')
    
    len_voca = len(data)

    if len_voca % 10 > 0:
        len_voca = len_voca // 10 + 1
    else:
        len_voca = len_voca // 10

    for i in range(1,len_voca+1):
        confusing_len.append(str(i))
    return render(request, "../templates/confusing.html", {'confusing_len' : confusing_len})

def confusing_detail(request, param):
    data = pd.read_excel('voca.xlsx')[(int(param)-1)*10:int(param)*10]
    
    voca = data['단어']
    meaning = data['의미']
    sentence = data['예문']
    significance = data['중요도']
    difficulty = data['난이도']
    number = range((int(param)-1)*10+1,int(param)*10+10)
    synonym = ['유의어']

    voca_data = []
    for i in zip(voca,meaning,sentence, significance, difficulty, number, synonym):
        voca_data.append(i)
    
    if len(data) - (10*(int(param)+1)) > -10: # ex) 총 단어 1001개, param 101까지
        next_page = int(param)+1
        page_ment = '다음 10단어 (%d ~ %d)' %(int(param)*10+1, (int(param)+1)*10)
    else:
        next_page = 'list'
        page_ment = '단어목록으로 가기'

    
    return render(request, "../templates/alphabet_detail.html", {'voca_data':voca_data, 'next_page':next_page, 'page_ment':page_ment})
# ----------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------------
def elementary(request):
    elementary_len = []
    data = pd.read_excel('voca.xlsx')
    data_filtered = data.loc[data['장르']=='elementary']
    len_voca = len(data_filtered)

    if len_voca % 10 > 0:
        len_voca = len_voca // 10 + 1
    else:
        len_voca = len_voca // 10

    for i in range(1,len_voca+1):
        elementary_len.append(str(i))
    return render(request, "../templates/elementary.html", {'elementary_len' : elementary_len})

def elementary_detail(request, param):
    data = pd.read_excel('voca.xlsx')
    data_filtered = data.loc[data['장르']=='elementary'][(int(param)-1)*10:int(param)*10]
    voca = data_filtered['단어']
    meaning = data_filtered['의미']
    sentence = data_filtered['예문']
    significance = data_filtered['중요도']
    difficulty = data_filtered['난이도']
    number = range((int(param)-1)*10+1,int(param)*10+10)
    synonym = data_filtered['유의어']

    voca_data = []
    for i in zip(voca,meaning,sentence, significance, difficulty, number, synonym):
        voca_data.append(i)
    
    if len(data) - (10*(int(param)+1)) > -10: # ex) 총 단어 1001개, param 101까지
        next_page = int(param)+1
        page_ment = '다음 10단어 (%d ~ %d)' %(int(param)*10+1, (int(param)+1)*10)
    else:
        next_page = 'list'
        page_ment = '단어목록으로 가기'

    
    return render(request, "../templates/alphabet_detail.html", {'voca_data':voca_data, 'next_page':next_page, 'page_ment':page_ment})
# ----------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------------
def significance(request):
    significance_len = []
    data = pd.read_excel('voca.xlsx')
    
    len_voca = len(data)

    if len_voca % 10 > 0:
        len_voca = len_voca // 10 + 1
    else:
        len_voca = len_voca // 10

    for i in range(1,len_voca+1):
        significance_len.append(str(i))
    return render(request, "../templates/significance.html", {'significance_len' : significance_len})

def significance_detail(request, param):
    data = pd.read_excel('voca.xlsx')[(int(param)-1)*10:int(param)*10]
    
    voca = data['단어']
    meaning = data['의미']
    sentence = data['예문']
    significance = data['중요도']
    difficulty = data['난이도']
    number = range((int(param)-1)*10+1,int(param)*10+10)
    synonym = data['유의어']

    voca_data = []
    for i in zip(voca,meaning,sentence, significance, difficulty, number, synonym):
        voca_data.append(i)
    
    if len(data) - (10*(int(param)+1)) > -10: # ex) 총 단어 1001개, param 101까지
        next_page = int(param)+1
        page_ment = '다음 10단어 (%d ~ %d)' %(int(param)*10+1, (int(param)+1)*10)
    else:
        next_page = 'list'
        page_ment = '단어목록으로 가기'

    
    return render(request, "../templates/alphabet_detail.html", {'voca_data':voca_data, 'next_page':next_page, 'page_ment':page_ment})
# ----------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------------
def GRE(request, param):
    GRE_len = []
    data = pd.read_excel('voca.xlsx')
    data_filtered = data.loc[data['장르']=='GRE']
    len_voca = len(data_filtered)

    if len_voca % 10 > 0:
        len_voca = len_voca // 10 + 1
    else:
        len_voca = len_voca // 10

    for i in range((int(param)-1)*10+1,int(param)*10+1):
        if i <= len_voca: 
            GRE_len.append(str(i))

    page = int(param)
    previous_page = int(param)-1
    next_page = int(param)+1
    len_page = len_voca //10 +1
    range_len_page = range(1,len_page+1)
    return render(request, "../templates/GRE.html", {'GRE_len' : GRE_len, 'page':page, 'previous_page':previous_page,'next_page':next_page,'len_page':len_page,'range_len_page':range_len_page})

def GRE_detail(request, param):
    data = pd.read_excel('voca.xlsx')
    data_filtered = data.loc[data['장르']=='GRE']
    data_filtered2 = data_filtered[(int(param)-1)*10:int(param)*10]
    voca = data_filtered2['단어']
    meaning = data_filtered2['의미']
    sentence = data_filtered2['예문']
    significance = data_filtered2['중요도']
    difficulty = data_filtered2['난이도']
    number = range((int(param)-1)*10+1,int(param)*10+10)
    synonym = data_filtered2['유의어']

    voca_data = []

    for i in zip(voca,meaning,sentence, significance, difficulty, number,synonym):
        voca_data.append(i)

    len_page = len(data_filtered)//10 +1
    param = int(param)
    
    next_page = int(param)+1
    prev_page = int(param)-1
    next_page_ment = '다음 10단어 (%d~%d)' %(int(param)*10+1, (int(param)+1)*10)
    prev_page_ment = '이전 10단어 (%d~%d)' %((int(param)-2)*10+1, (int(param)-1)*10)
    list_page_ment = '단어목록으로 가기'
    if int(param) % 10 > 0:
        list_page = int((int(param) - int(param) % 10)/10 +1)
    else:
        list_page = int(int(param) /10)

    return render(request, "../templates/GRE_detail.html", {'list_page_ment': list_page_ment,'list_page':list_page, 'len_page':len_page,'param':param,'voca_data':voca_data, 'next_page':next_page, 'next_page_ment':next_page_ment,'prev_page':prev_page, 'prev_page_ment':prev_page_ment})
# ----------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------




# ----------------------------------------------------------------------------------------------------------------------
def practice(request):
    practice_len = []
    data = pd.read_csv('voca.csv', encoding = 'UTF-8')
    
    len_voca = len(data)

    if len_voca % 10 > 0:
        len_voca = len_voca // 10 + 1
    else:
        len_voca = len_voca // 10

    for i in range(1,len_voca+1):
        practice_len.append(str(i))
    return render(request, "../templates/practice.html", {'practice_len' : practice_len})



def practice_detail(request, param):
    data = pd.read_csv('voca.csv', encoding = 'UTF-8')[(int(param)-1)*10:int(param)*10]
    
    voca = data['단어']   
    meaning = data['의미']
    sentence = data['예문']
    significance = data['중요도']
    difficulty = data['난이도']
    number = data['번호']
    genre = data['장르']
    voca_data = []
    for i in zip(voca,meaning,sentence, significance, difficulty, number):
        voca_data.append(i)
    
    return render(request, "../templates/practice_detail.html", {'voca_data':voca_data})
# ----------------------------------------------------------------------------------------------------------------------













