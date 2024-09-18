from django.urls import path
from .views import index,freeContent ,contact ,register,training
from django.contrib.auth import views as auth_veiw
from .forms import LoginForm
app_name ="core"

urlpatterns = [
    path('',index , name="index"),
    path('training/',training,name="training")
    ,
    path('freeContent/',freeContent,name="freeContent"),
    path('register/',register,name="register"),
    path('login/',auth_veiw.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name="login"),
    path('logout/', auth_veiw.LogoutView.as_view(template_name='core/logout.html'), name='logout'),

    path("contact/",contact ,name="contact"),
    
]

