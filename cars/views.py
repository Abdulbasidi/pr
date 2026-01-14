from django.shortcuts import render , redirect

# Create your views here.

def main_page(request):
    return render(request, 'components/base.html')




def contacts(request):
    return render(request=request, template_name='cars/contact.html',)


def about(request):
    return render(request=request, template_name='cars/about.html',)

def works(request):
    return render(request=request, template_name='cars/works.html',)


def services(request):
    return render(request=request, template_name='cars/services.html',)

def offers(request):
    return render(request=request, template_name='cars/offers.html',)