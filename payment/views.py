from django.shortcuts import render

from payment.models import BillingProfile
from .serializers import BillingProfileSerializer, StripeTokenSerializer
# Create your views here.
from rest_framework import generics
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


class BillingProfileAPIView(generics.GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset            =   BillingProfile.objects.all()
    serializer_class    =   BillingProfileSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class StripPaymentAPIView(generics.GenericAPIView):
    pass
	# queryset                =       OrderItem.objects.all()
#     serializer_class        =       StripeTokenSerializer
#     permission_classes      =       []
#     # authentication_classes  =       [TokenAuthentication,JSONWebTokenAuthentication,SessionAuthentication]


#     def get(self,request):
#     	order_id          =   self.request.GET.get("order_id")
# 	print("order id",order_id)
#     	order		      =	Order.objects.get(order_id=order_id)
#     	user              =   order.User
#     	amount			  =	int(decimal.Decimal(order.total)*decimal.Decimal(100))
#     	token             = self.request.GET.get("token")
#     	charge            = stripe.Charge.create(
# 		  amount=amount,
# 		  currency="usd",
# 		  description=order_id,
# 		  source=token,)
#     	if charge.status=="succeeded":
#     		qs 					=	Cart.objects.filter(User=user,active=True)
#     		try:
#     			qs                  =   qs.first()
#     			qs.active			=	False
#     			qs.save()
#     		except:
#     			print(qs)
#     		qs1         		=   OrderItem.objects.filter(User=user,active=True)
#     		try:
#     			for x in qs1:
#     				x.active		=	False
#     				x.save()
#     		except:
#     			print(qs1)
#     		order.ordered=True
#     		order.save()
#     		send_email(user.email)
#     		BASE_URL ="https://exp.host/--/api/v2/push/send/"
#     		headers ={'Accept': 'application/json',
#     					'Accept-encoding': 'gzip, deflate',
#     					'Content-Type': 'application/json',}
#     		message = {
#     					"to": order.shop.user.notification.token,
#     					"sound": 'default',
#     					"title": 'Order Recieved',
#     					"body": 'Order Recievved',
#     					"data": { "someData": 'goes here' },
#     		}
#     		res = requests.post(BASE_URL,data=json.dumps(message),headers=headers)
#     		return redirect("https://management.ezswiftshops.com/billing/thankyou/")
#     	return redirect("https://management.ezswiftshops.com/billing/failed/")
# #ExponentPushToken[xSva47K3VIys9gkwnZiTc-]
