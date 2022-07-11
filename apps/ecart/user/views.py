from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.utils import timezone
from datetime import datetime
from .models import CustomerInformations, Orders
from django.utils import timezone
import json


@api_view(['POST'])
def user(request):
	try:
		user = User(request)
		if request.data['method'] == 'createUser':
			msg = user.createUser()
	
		return Response({'Response_status':True,"Response_data":msg}, status=HTTP_200_OK)
	except Exception as e:
		print(e)
		return Response({'Response_status':False,"Response_data":{"user_id":None,"status":"Failure","error_msg": "Invalid data or data missing"}}, status=HTTP_400_BAD_REQUEST)

class User:
	def __init__(self,request):
		if type(request) is dict:
			self.request = {}
			self.request['request'] = request
		else:
			self.request = request.data
		self.getDataFromRequest = lambda key : self.request['request'][key] if key in self.request['request'] else None

	def createUser(self):
				
		user_details = {
			"user_name" : self.getDataFromRequest('user_name'),
			"password" : self.getDataFromRequest('password'),
			"email_id" : self.getDataFromRequest('email_id'),
			"status" : self.getDataFromRequest('status'),
			"created_date" : timezone.now()
		}
		user_detials_data=CustomerInformations(**user_details)		
		user_detials_data.save()
		user_id = user_detials_data.customer_id		
		return {"user_id":user_id,"status":"Success"}

