from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'form/index.html')

def submit(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    request.session['counter'] += 1
    return redirect('/result')

def result(request):
    return render(request, 'form/result.html')
