"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuario.views import signup_view, home, login_view
from atividade.views import excluir_atividade
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.contrib.staticfiles.views import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('', home, name='home'),
    path('atividade/', include('atividade.urls', namespace='atividade')),
    path('empresa/', include('empresa.urls', namespace='empresa')),
    path('excluir/<int:area_id>/', excluir_atividade, name='excluir_atividade'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

