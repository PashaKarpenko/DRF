"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from stores import views
from stores.urls import router as my_store_router
from stores.urls import store_router as store_router
from stores.urls import admin_router as admin_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path('calculator/', views.CalculatorApiView.as_view()),
    path('today/', views.today),
    path('my_name/', views.my_name),
    path('stores/', include(store_router.urls)),
    path('my_stores/', include(my_store_router.urls)),
    path('admin_stores/', include(admin_router.urls))
]
