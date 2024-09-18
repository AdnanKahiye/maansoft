from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from course.models import Category, Course
from .forms import SignupForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    courses =Course.objects.all()
    return render(request, "core/index.html", {
        "categories": categories,
        "courses":courses
        
    })
    
@login_required
def freeContent(request):
    return render(request, "core/freeContent.html")

def contact(request):
    return render(request, "core/contact.html")




def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save phone number or other fields to the profile if needed here
           # login(request, user)  # Log in the user after registration
            return redirect('/login/')  # Redirect to a home page or other view
    else:
        form = SignupForm()
    
    return render(request, 'core/register.html', {'form': form})


def training(request):
    return render(request ,"core/training.html")
