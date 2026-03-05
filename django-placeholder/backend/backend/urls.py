from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "Backend Live", "message": "SMS Backend API is running"})

urlpatterns = [
    path('', home, name='home'),
    # path('admin/', admin.site.urls),
    path('api/v1/',include('api.urls')),
    path('auth/',include('security.urls')),
    # path('api-auth/',include('rest_framework.urls',namespace='rest_framework')), # it will show login on admin panel on top-right corner of api, in which user doesnot need to be staff or admin
]
