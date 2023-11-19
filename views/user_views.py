from django.shortcuts import render


def user(request):
    return render(request, 'user.html')

def uedit(request):
    return render(request, 'user-edit.html')