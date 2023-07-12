import os
from dotenv import load_dotenv
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from sch.scripts.BC import client_finder, optical_finder

load_dotenv()


class CHECK(generics.GenericAPIView):
    def get(self, req):
        print(req)
        status_code = 200
        response_text = "ms_running"
        return HttpResponse(response_text, status=status_code)


class SCH(generics.GenericAPIView):
    def get(self, req):
        if req.META["HTTP_CONEXT_KEY"] == os.environ["CONEXT_KEY"]:
            contract = req.query_params.get("contract")
            olt = req.query_params.get("olt")
            data = {"contract": contract, "olt": olt}
            res = client_finder(data)
            response_data = {"message": "OK", "data": res}
            if res is None:
                response_data = {
                    "message": "The required OLT & ONT does not exists",
                    "data": res,
                }
            return Response(response_data, status=200)
        return HttpResponse("Bad Request to server", status=500)


class PWR(generics.GenericAPIView):
    def get(self, req):
        if req.META["HTTP_CONEXT_KEY"] == os.environ["CONEXT_KEY"]:
            contract = req.query_params.get("contract")
            olt = req.query_params.get("olt")
            data = {"contract": contract, "olt": olt}
            res = optical_finder(data)
            response_data = {"message": "OK", "data": res}
            if res is None:
                response_data = {
                    "message": "The required OLT & ONT does not exists",
                    "data": res,
                }
            return Response(response_data, status=200)
        return HttpResponse("Bad Request to server", status=500)


class SCHDashboard(generics.GenericAPIView):
    def post(self, req):
        if req.data["API_KEY"] == os.environ["API_KEY"]:
            contract = req.query_params.get("contract")
            data = {"contract": contract}
            res = client_finder(data)
            response_data = {"message": "OK", "data": res}
            if res is None:
                response_data = {
                    "message": "The required OLT & ONT does not exists",
                    "data": res,
                }
            return Response(response_data, status=200)
        return HttpResponse("Bad Request to server", status=500)
