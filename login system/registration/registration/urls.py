from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('',views.HomePage,name='home'),
    path('home2',views.HomePage2,name='home2'),
    path('logout/',views.LogoutPage,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='passwordreset.html'), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='passwordresetdone.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwordresetform.html'), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'), name="password_reset_complete"),

    
]