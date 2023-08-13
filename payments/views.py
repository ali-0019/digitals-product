from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

import uuid

import requests

from datetime import datetime

from .serializers import GatewaySerializer
from subscriptions.models import Package, Subscription
from payments.models import Gateway, Payment

# Create your views here.

class GatewayView(APIView):
    def GET(self, request):
        gateway = gateway.objects.filter(is_enable= True)
        serializer = GatewaySerializer(gateway, many = True)
        return Response(serializer.data)
    

class PaymentView(APIView):
    permission_class = [IsAuthenticated]
    
    def GET(self, request):
        gateway_id = request.query_params.get('gateway')
        package_id = request.query_params.get('package')
        
        
        try :
            package = Package.objects.get(pk = package_id, is_enable = True)
            gateway = Gateway.objects.get(pk = gateway_id, is_enable = True)
            
        except (Package.DoesNotExist, Gateway.DoesNotExist):
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        payment = payment.objects.create(
            user = request.user,
            package = package,
            gateway = gateway,
            price = package.price,
            Phone_number = request.user.PHone_number,
            token = str(uuid.uuid4())
        )
        
        #return redirect()
        return Response({'token': payment.token, 'callback_url': 'kttps://my-site.com/payment/'})
    
    
    def POST(self, request):
        token = request.data.get('token')
        st = request.data.get('status')
        
        try: 
            payment = Payment.objects.get(token = token)
        except Payment.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        if st != 10:
            payment.status = Payment.STATUS_CANCELED
            payment.save()
            return Response({'detail' : 'Payment verification failed'}, status= status.HTTP_400_BAD_REQUEST)
        
        r = requests.post('bank_verify_url', data = {})
        if r.status_code // 100 != 2 :
            payment.status = payment.STATUS_ERROR
            payment.save()
            
            return Response({'detail' : 'Payment verification failed'}, status= status.HTTP_400_BAD_REQUEST)
        
        payment.status = payment.STATUS_PAID
        payment.save()
        
        Subscription.objects.create(
            user = payment.user,
            package = payment.package,
            expire_time = datetime.now() + datetime.timedelta(days = payment.package.duration.days)
        )
        
        return Response({'detail': 'payment successfully'})