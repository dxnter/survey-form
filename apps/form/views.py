from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "Hello, I am your first request!"
    print response
    return render(request, 'form/index.html')

def submit(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'form/result.html')