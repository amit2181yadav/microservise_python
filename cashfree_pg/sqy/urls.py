from django.urls import path
from .views import orderdetails

urlpatterns = [
    path('orderApi/', orderdetails,name='orderdetails' ),
    # path('request/<id>/', handlerequest,name='handlerequest' ),
    # path('response', handleresponse,name='handleresponse' ),
]