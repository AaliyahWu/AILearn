from django.shortcuts import render

# about畫面
def about(request):
    return render(request, 'about.html')

# about畫面
def course(request):
    return render(request, 'course.html')

# about畫面
def instructor(request):
    return render(request, 'instructor.html')

# about畫面
def blog(request):
    return render(request, 'blog.html')

# about畫面
def contact(request):
    return render(request, 'contact.html')

# about畫面
def blog_single(request):
    return render(request, 'blog-single.html')

# about畫面
def instructor_details(request):
    return render(request, 'instructor-details.html')

def theme(request):
    return render(request, 'theme.html')

def pic(request):
    return render(request, 'pic.html')

def pic4(request):
    return render(request, 'pic4.html')

def reading(request):
    return render(request, 'reading.html')

def reading9(request):
    return render(request, 'reading9.html')

def reading10(request):
    return render(request, 'reading10.html')

def reading11(request):
    return render(request, 'reading11.html')

def gtp_reading(request):
    return render(request, 'gtp_reading.html')

def gtp_reading9(request):
    return render(request, 'gtp_reading9.html')

def gtp_reading10(request):
    return render(request, 'gtp_reading10.html')

def gtp_reading11(request):
    return render(request, 'gtp_reading11.html')

def score(request):
    return render(request, 'score.html')

def vocabulary(request):
    return render(request, 'vocabulary.html')
def record(request):
    return render(request, 'record.html')
def record_single(request):
    return render(request, 'record_single.html')
