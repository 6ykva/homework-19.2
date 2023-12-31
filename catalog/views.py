from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя{name}\n'
              f'Телефон {phone}\n'
              f'Сообщение {message}\n')
    
    return render(request, 'catalog/contacts.html')
