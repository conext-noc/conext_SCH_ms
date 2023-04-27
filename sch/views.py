from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse
from dotenv import load_dotenv
import os

load_dotenv()
from sch.scripts.BC import clientFinder, clientPwrFinder


class CHECK(generics.GenericAPIView):
  def get(self, req):
    status_code = 200
    response_text = "ms_running"
    return HttpResponse(response_text, status=status_code)


class SCH(generics.GenericAPIView):
  def get(self, req):
    if req.META['HTTP_CONEXT_KEY'] == os.environ["CONEXT_KEY"]:
      status_code = 200
      contract = req.query_params.get('contract')
      olt = req.query_params.get('olt')
      data = {"contract":contract, "olt":olt}
      res = clientFinder(data)
      response_data = {"message": "OK", "data": res}
      return Response(response_data, status=status_code)
    else:
      return HttpResponse("Bad Request to server", status=400)
    
class PWR(generics.GenericAPIView):
  def get(self, req):
    if req.META['HTTP_CONEXT_KEY'] == os.environ["CONEXT_KEY"]:
      status_code = 200
      contract = req.query_params.get('contract')
      olt = req.query_params.get('olt')
      data = {"contract":contract, "olt":olt}
      res = clientPwrFinder(data)
      response_data = {"message": "OK", "data": res}
      return Response(response_data, status=status_code)
    else:
      return HttpResponse("Bad Request to server", status=400)
    
