from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'my_site/home.html')


def view_3d(request):
    pass


def view_print_detail(request):
    pass

