from django.urls import path
from .views import detail ,form ,edit ,lists,delete,student

app_name = 'course'

urlpatterns = [
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/edit/', edit, name='edit'),
    path('form/', form, name='form'),
    path("lists/" ,lists ,name="lists"),
        path('<int:user_id>/<int:category_id>/', student, name='student'),

    
]
