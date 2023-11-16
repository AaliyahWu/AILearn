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