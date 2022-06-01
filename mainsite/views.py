from django.shortcuts import redirect, render
from .models import Contact, Teachers
from django.contrib import messages


# Create your views here.
def index(request):
    teachers = Teachers.objects.all()
    params = {'teacher': teachers}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        msg = request.POST.get('msg')

        contact = Contact(name=name, email=email, number=number, msg=msg)
        contact.save()

    return render(request, 'index.html', params)


def student(request):
    return render(request, "student.html")


def course(request):
    return render(request, "course.html")


def vfx(request):
    return render(request, "3d.html")

def arts(request):
    return render(request, "arts.html")

def basic(request):
    return render(request, "basic.html")

def graphics(request):
    return render(request, "graphics.html")

def editing(request):
    return render(request, "editing.html")

def finance(request):
    return render(request, "finance.html")


def works(request):
    return render(request, "works.html")


def userlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        if (name=="straight" and password=="12345"):
            return redirect('student')
        else:
            messages.warning(request, 'Invalid Credentials.')

    return render(request, "login.html")
