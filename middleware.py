import jwt
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()

secret_key = os.getenv("secret_key")

def create_token(details, expiry):
    expire = datetime.now() + timedelta(minutes=expiry)

    details.update({"exp":expire})

    encoded_jwt= jwt.encode(details, secret_key)
    return encoded_jwt

def verify_token(request: HTTPAuthorizationCredentials = Security(bearer)):
    # request.headers.get("Authorization")
    payload = request.header.get("Authorization")
    "Authorization": "Bearer jdkfhhfjdkdkkd"
    payload = "Bearer jdkfhhfjdkdkkd"

       
    # token = payload.split("")[1]
    token = request.credentials
    verify_token = jwt.decode(token, secret_key, algorithm=["HS256"])

    return {
        "email": verify_token.get("email")
        "userType": verify_token.get("userType")  
    }




