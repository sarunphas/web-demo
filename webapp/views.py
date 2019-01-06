from django.shortcuts import render

def index(request):
    return render(request, 'webapp/home.html')
def contact(request):
    context = {
        'content': ['My email','bell@gmail.com']
    }
    return render(request, 'webapp/contact.html', context)

def about(request):
    return render(request, 'webapp/about.html')
def knowledges(request):
    return render(request, 'webapp/knowledges.html')
def programs(request):
    return render(request, 'webapp/programs.html')
def publications(request):
    return render(request, 'webapp/publications.html')
def data(request):
    context = {
    'NDII': ['My email','bell@gmail.com']
    }
    return render(request, 'webapp/data.html')

