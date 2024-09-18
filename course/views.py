from django.shortcuts import render,get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from .models import Course,Category
from .forms import NewICourseForm ,EditItemForm ,StudentForm
from django.contrib.auth.models import User 

# Create your views here.
login_required
def form(request):
    if request.method == 'POST':
        form = NewICourseForm(request.POST, request.FILES)

        if form.is_valid():
            couse = form.save(commit=False)
            couse.created_by = request.user
            couse.save()

            return redirect('course_list')
    else:
        form = NewICourseForm()

    return render(request, 'course/form.html', {
        'form': form,
        'title': 'New Course',
    })




def detail (request,pk):
    category =get_object_or_404(Category ,pk=pk)
    courses = Course.objects.filter(category=category)
    
    return render(request ,"course/detail.html",{
        "category":category,
        "courses":courses
    })
    
    
    
@login_required
def edit(request, pk):
    course = get_object_or_404(Course, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=course)

        if form.is_valid():
            form.save()

            return redirect('course:lists')
    else:
        form = EditItemForm(instance=course)

    return render(request, 'course/form.html', {
        'form': form,
        'title': 'Edit course',
    })
    
    

@login_required
def delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()

    return redirect('dashboard:index')


@login_required
def lists(request):
    courses = Course.objects.all()  # Fetch all courses
    return render(request, 'course/lists.html', {'courses': courses})




def student(request, user_id, category_id):
    # Fetch the user and course using their IDs
    user = get_object_or_404(User, id=user_id)
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('core:index')  # Redirect to a success page after form submission
    else:
        form = StudentForm(initial={
            'full_name': user.username,  # Pre-populate the full name field with user info
            'course_name': category.name  # Pre-populate the course name field with course info
        })

    context = {
        'form': form,
        'user': user,
        'category': category
    }
    
    return render(request, 'course/student.html', context)