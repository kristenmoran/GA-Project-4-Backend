"""zoodoc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
=======
=======
>>>>>>> 4bbd0be2d2db4b4d1ca72ad44ddea8aecd540258
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls'))
<<<<<<< HEAD
>>>>>>> 1e5bb15153522aec51664c9fff011da3ebea3805
=======
>>>>>>> 4bbd0be2d2db4b4d1ca72ad44ddea8aecd540258
]
