Create_user request :
Post man url : http://localhost:8000/user 

request : 

{
  "method": "createUser",
  "request": {
    "user_name": "arun",
    "password": "password123",
    "email_id": "admin",
    "status": "Y"
  }
}

................................................................


Add product to cart:

{
  "method": "addProduct",
  "request": {
    "category": "1",
    "customer_id": "1",
    "product_name": "iphone"
  }
}

.......................................

Place card order :

{
  "method": "placeCartOrder",
  "request": {
    "customer_id": "1"
  }
}

