from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
# 회원가입

def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'signup_error_id.html')

        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],
                                            first_name=request.POST.get('first_name', 'default'), # 생년월일을 받기 위해 user 기본 모델의 퍼스트네임 사용
                                            last_name=request.POST.get('last_name', 'default'),)  # 성별을 받기 위해 user 기본 모델의 라스트네임 사용

            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/board')
        else:
            return render(request, 'signup_error_pw.html')
            
    return render(request, '../templates/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/')
        else:
            return render(request, 'login_error.html')
    else:
        return render(request, 'login.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('index')

# home
def home(request):
    return render(request, '../templates/index.html')





