from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from library.views import home
from users.views import login_view, api_login

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('library.urls')),
    path('api/login/', api_login, name="api_login"),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
