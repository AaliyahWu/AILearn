from django.shortcuts import render

# 首頁畫面
def index(request):
    return render(request, 'index.html')

