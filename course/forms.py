from django import forms 
from .models import Course ,Student

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewICourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('category', 'name', 'instructor', 'description', 'duration','price','image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'instructor':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        ,
            
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            
              'duration':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
            ,
            
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'instructor','description','duration', 'price', 'image')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'instructor': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
             'duration': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
        
        
        
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('FulName', 'PhoneNumber','CourseName')
        widgets = {
            'FulName': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'PhoneNumber': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
             'CourseName': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }