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
def pic1(request):
    return render(request, 'pic1.html')

def reading(request):
    return render(request, 'reading.html')

def reading1(request):
    return render(request, 'reading1.html')

def reading2(request):
    return render(request, 'reading2.html')
def reading3(request):
    return render(request, 'reading3.html')
def reading4(request):
    return render(request, 'reading4.html')
def reading5(request):
    return render(request, 'reading5.html')
def gtp_reading(request):
    return render(request, 'gtp_reading.html')
def gtp_reading1(request):
    return render(request, 'gtp_reading1.html')
def gtp_reading2(request):
    return render(request, 'gtp_reading2.html')
def gtp_reading3(request):
    return render(request, 'gtp_reading3.html')
def gtp_reading4(request):
    return render(request, 'gtp_reading4.html')
def gtp_reading5(request):
    return render(request, 'gtp_reading5.html')
def score(request):
    return render(request, 'score.html')
def score1(request):
    return render(request, 'score1.html')
def score2(request):
    return render(request, 'score2.html')
def score3(request):
    return render(request, 'score3.html')
def score4(request):
    return render(request, 'score4.html')
def score5(request):
    return render(request, 'score5.html')

def vocabulary(request):
    return render(request, 'vocabulary.html')
def record(request):
    return render(request, 'record.html')
def record_single(request):
    return render(request, 'record_single.html')
