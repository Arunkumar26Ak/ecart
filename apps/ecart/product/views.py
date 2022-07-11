from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)
from django.utils import timezone
from .models import Products
from ..user.models import Orders
from django.utils import timezone
import json


@api_view(['POST'])
def product(request):
	try:
		product = Product(request)
		if request.data['method'] == 'addProduct':
			msg = product.addProduct()
		if request.data['method'] == 'placeCartOrder':
			msg = product.placeCartOrder()
		return Response({'Response_status':True,"Response_data":msg}, status=HTTP_200_OK)
	except Exception as e:
		print(e)
		return Response({'Response_status':False,"Response_data":{"product_id":None,"status":"Failure","error_msg": "Invalid data or data missing"}}, status=HTTP_400_BAD_REQUEST)

class Product:
	def __init__(self,request):
		if type(request) is dict:
			self.request = {}
			self.request['request'] = request
		else:
			self.request = request.data
		self.getDataFromRequest = lambda key : self.request['request'][key] if key in self.request['request'] else None

	def addProduct(self):

		product_details = {
			"category_id" : self.getDataFromRequest('category'),
			"customer_id": self.getDataFromRequest('customer_id'),
			"product_name" : self.getDataFromRequest('product_name'),
			"created_at" : timezone.now()
		}
		product_details_data=Products(**product_details)		
		product_details_data.save()
		product_id = product_details_data.product_id		
		return {"product_id":product_id,"status":"Product added to Cart"}
	
	def placeCartOrder(self):
		
		cart_details = Products.objects.filter(customer_id = self.getDataFromRequest('customer_id')).values("product_id")

		for i in cart_details:
			order_details = {
				"product_id" : i['product_id'],
				"customer_id" : self.getDataFromRequest('customer_id'),
				"status" : "PLACED",
				"created_at" : timezone.now()
			}
			product_details_data=Orders(**order_details)		
			product_details_data.save()
			product_id = product_details_data.product_id	
			
		return {"status":"Cart order placed."}
	

	
	

