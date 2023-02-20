from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.decorators import api_view
from . import redis_client,email_sender
import threading
from validate_email_address import validate_email
from constants import email_validations
@api_view([
  "get"
])
def status(request, *args, **kwargs):
    return JsonResponse({"status": "running",
                         "activeThreads": threading.active_count(),
                         "active_request":redis_client.requestQueueLength(),
                         "failed_requests":email_sender.discard_count,
                         "concurrent_connections":email_sender.current_concurrency,
                         "max_concurrency":email_sender.getMaxConcurrency()
                         })





@api_view([
  "post"
])
def request_code(request:Request):
  email=request.data["email"]
  isValid=validate_email(email)
  if(isValid==True):
    domain=str(email).split("@")[1]
    if(domain in email_validations.allowed_domain):
      ts=redis_client.publishRequest(email)
      return JsonResponse({"status": ts is not None,
                            "timestamp": ts
                            })
    else:
      return JsonResponse({"status": False,
                           "message":"domain invalid" 
                            },status=400)
  else:
    return JsonResponse({"status": False,
                          "message":"email is invalid" 
                          },status=400)
  



@api_view([
  "post"
])
def check_code(request:Request):
  email=request.data["email"]
  code=request.data["code"]
  res=redis_client.checkCode(email,code)
  return JsonResponse({"status": res=="OK",
  "message":res  
  })
