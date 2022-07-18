from django.urls import path, include
from rest_framework import routers
from .views import MyStoreViewSet, StoresViewSet, AdminStoreViewSet


router = routers.SimpleRouter()
router.register('', MyStoreViewSet, basename='my_store')
store_router = routers.SimpleRouter()
store_router.register('', StoresViewSet, basename='store')
admin_router = routers.SimpleRouter()
admin_router.register('', AdminStoreViewSet, basename='admin')
