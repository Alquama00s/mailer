from django.urls import path
from . import views



urlpatterns=[
  path('status',views.status),
  path('requestcode',views.request_code),
  path('checkcode',views.check_code),

]