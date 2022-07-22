
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app01 import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'group', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users', views.index),
    path('api/',include(router.urls)),
    path('api/', include(('app02.urls', 'app02'), namespace='app02')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
