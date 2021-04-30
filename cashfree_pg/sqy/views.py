from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.http import JsonResponse
from django.http import Http404
from .models import Order 
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt 
import hashlib
import hmac
import base64

@api_view(['POST'])
def orderdetails(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            orderId = obj.orderId
            print(orderId)    
            return Response({"ordeId":orderId})
        return Response(serializer.errors)

# secretKey = "<ENTER_YOUR_SECRETKEY_HERE>
# secretKey = "5cb2d3893a2c392d8b7b045c23ea9087de2f3ca2"
# def handlerequest(request,id):
#     if (request.method=='GET'):
#         mode = "TEST" # <-------Change to TEST for test server, PROD for production
#         print(id)
#         order = Order.objects.get(id = id)
#         orderId = order.id  
#         orderAmount = order.orderAmount  
#         orderCurrency = order.orderCurrency
#         orderNote = order.orderNote
#         customerName = order.customerName 
#         customerPhone = order.customerPhone  
#         customerEmail = order.customerEmail  
#         appId = '6604138e3302a413d0d6ab04114066'
#         returnUrl = 'http://127.0.0.1:8000/sqy/response'
#         notifyUrl = 'http://127.0.0.1:8000/sqy/response'

        
#         postData = {
#             "appId" : appId,
#             "orderId" : orderId,
#             "orderAmount" : orderAmount,
#             "orderCurrency" : orderCurrency,
#             "orderNote" : orderNote,
#             "customerName" : customerName,
#             "customerPhone" : customerPhone,
#             "customerEmail" : customerEmail, 
#             "returnUrl" : returnUrl,
#             "notifyUrl" : notifyUrl
#         }
#         sortedKeys = sorted(postData)
#         print(sortedKeys)
#         signatureData = ""
#         for key in sortedKeys:
#             signatureData += key+str(postData[key])
#         message = signatureData.encode('utf-8')
#         #get secret key from your config
#         secretKey = "5cb2d3893a2c392d8b7b045c23ea9087de2f3ca2"
#         secret = secretKey.encode('utf-8')
#         signature = base64.b64encode(hmac.new(secret,message,digestmod=hashlib.sha256).digest()).decode("utf-8")
#         # signature = base64.b64encode(hmac.new(secret, message,digestmod=hashlib.sha256).digest())
#         if mode == 'PROD': 
#             url = "https://www.cashfree.com/checkout/post/submit"
#         else: 
#             url = "https://test.cashfree.com/billpay/checkout/post/submit"
#         d = {'postData':postData,'signature':signature,'url':url}
#         return render(request,'request.html', context = d)
#     return render(request, 'request.html')
