"# Mvp-Project" 

1) first you should install required packages!

pip install -r requirements.txt

http://127.0.0.1:8000/api/register
You should send 'email','username','password' with POST request to register

http://127.0.0.1:8000/token/
Send GET request to get JwtToken



http://127.0.0.1:8000/api/create
In this url authentication is required!
You should send by POST method: {
                    "driver": "{driver's id},
                    "client": {client's id}
                   }
And It creates order, then returns the order's 'id'.


http://127.0.0.1:8000/api/update_status
In this url authentication is required! 
You should send by PUT method: {
                    "id": "{order's id},
                    "status": "created"/"cancelled"/"accepted"/"finished"
                   }

http://127.0.0.1:8000/api/orders/client/{client_id} << {client_id} is client's id
In this url authentication is required!
This url returns all of the orders of client!

and you can clarify the result by following example
http://127.0.0.1:8000/api/orders/client/{client_id}?from=5/01/2022&to=12/01/2022