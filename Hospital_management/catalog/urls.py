"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from .import views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'main/$',views.main_home,name="main_home"),
    url(r'test/$',views.tests,name="test"),
   
    url(r'home/$',views.home,name="home"),
    url(r'aboutus/$',views.aboutus,name="aboutus"),
    url(r'team/$',views.team,name="team"),
    url(r'service$',views.service,name="service"),
    url(r'contactus/$',views.contactus,name="contact"),
    url(r'team/$',views.team,name="team"),
    url(r'^takeapoint/$',views.takeapoint,name='takeapoint'),
    url(r'^viewapoint/$',views.viewapoint,name='viewapoint'),
    url(r'^viewapoint/(\w+)',views.patientdetail, name='patientdetail'),
    url(r'^cancelapoint/$',views.cancelapoint,name='cancelapoint'),
    url(r'^givemedicine/$',views.givemed,name='givemedicine'),
    url(r'^history/$',views.history,name='history'),
    url(r'^myappoint/$',views.myappoint,name='myappoint'),
    url(r'^history/(?P<date>[A-Za-z]?%20[0-9]{2}?%20[0-9]{4})/$', views.tests, name='index'),

    url(r'^ajax/slots/$', views.load_slots, name='ajax_load_slots'),
    url(r'^ajax/finalslots/$', views.load_finalslots, name='ajax_load_finalslots'),
    url(r'login/$', auth_views.login, {'template_name': 'login.html'},name='login'),
    url(r'register/$',views.register, name='register'),
    # xurl(r'register2/$',views.register2,name='register2'),
    url(r'logout/$',auth_views.logout,{'next_page': '/main'},name='logout'),
    #url(r'logout/$',auth_views.LogoutView.as_view(template_name='logout.html')),
    url(r'password_change/$',auth_views.PasswordChangeView.as_view(template_name='registration\password_change.html',success_url='/password_change_done')),
    url(r'password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration\password_change_done.html')),
    url(r'password_reset/$',auth_views.PasswordResetView.as_view(template_name='registration\password_reset_form.html',email_template_name='password_reset_email.html',subject_template_name='registration\password_reset_subject.txt',success_url='/password_reset_done/',from_email='support@yoursite.ma')),
    url(r'password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='registration\password_reset_done.html')),
    url(r'password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='registration\password_reset_confirm.html',success_url='/password_reset_complete/')),
    url(r'password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration\password_reset_complete.html'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

