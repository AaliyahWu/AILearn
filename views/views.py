from django.shortcuts import render

# 首頁畫面
def index(request):
    return render(request, 'index.html')

# 首頁畫面
def login(request):
    return render(request, 'login.html')

# 首頁畫面
def logout(request):
    return render(request, 'indexx.html')

# 首頁畫面
def register(request):
    return render(request, 'register.html')

# 首頁畫面
def forget(request):
    return render(request, 'forget.html')

