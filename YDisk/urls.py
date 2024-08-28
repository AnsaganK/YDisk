from django.contrib import admin
from django.contrib.auth import views as acc
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls', namespace='app')),
]

urlpatterns += [
    path('login', acc.LoginView.as_view(), name='login'),
    path('logout', acc.LogoutView.as_view(), name='logout'),
]
