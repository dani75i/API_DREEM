import datetime
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from faker import Faker
fake = Faker()

l = []
list_key_available = ["nickname", "mac", "installed_firmware", "hardware"]

##################################
### OPERATION FOR ONE HEADBAND ###
##################################

@api_view(['GET', 'POST'])
def headband(request):

    if request.method == "GET":
        result = {
            "headbands":l
        }
        return Response(result, status=200)

    if request.method == "POST":
        result_headband = {
            "id": fake.uuid4(),
            "nickname": fake.user_name(),
            "mac": fake.ipv4(),
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "last_connection": datetime.datetime.now(),
            "installed_firmware": "BIOS",
            "hardware": random.choice(["Type 1", "Type 2"])
        }
        l.append(result_headband)

        result = {
            "result": "headband created",
            "headband": result_headband
        }
    return Response(result, status=201)

@api_view(['GET'])
def headband_id(request, id):

    if request.method == "GET":
        for i in range(len(l)):
            if l[i]["id"] == id:
                l[i]["last_connection"] = datetime.datetime.now()
                return Response(l[i], status=200)

        error = {
            "error": "not found",
            "error_description": "id {} doesn't exist".format(id)
        }
        return Response(error, status=404)

@api_view(['PUT'])
def add_content_for_one_headband(request, id, key, value):

    if request.method == "PUT":
        for i in range(len(l)):
            if l[i]["id"] == id:
                l[i][key] = value
                l[i]["headband_nickname"] = fake.user_name()
                l[i]["date_modification"] = datetime.datetime.now()

                result = {
                    "result": l[i]
                }
                return Response(result, status=200)

        error = {
            "reason": "not found",
            "detail": "id {} doesn't exist".format(id)
        }
        return Response(error, status=404)

@api_view(['DELETE'])
def delete_content_for_one_headband(request, id, key):
    if request.method == "DELETE":
        for i in range(len(l)):
            if l[i]["id"] == id:
                del l[i][key]
                result = {
                    "result": l[i]
                }
                return Response(result, status=200)

        error = {
            "reason": "not found",
            "detail": "id {} doesn't exist".format(id)
        }
        return Response(error, status=404)



###################################
### OPERATION FOR ALL HEADBANDS ###
###################################

@api_view(['DELETE'])
def delete_content_for_all_headbands(request, key):

    if request.method == "DELETE":
        if key in list_key_available:
            for i in range(len(l)):
                del l[i][key]
                l[i]["modified_at"] = datetime.datetime.now(),
                l[i]["last_connection"] = datetime.datetime.now(),
            list_key_available.remove(key)
            return Response(l, status=200)
        else:
            error = {
                "error": "not found",
                "error_description": "key {} doesn't exist".format(key)
                    }
            return Response(error, status=400)

@api_view(['PUT'])
def add_content_for_all_headbands(request, key, value):

    if request.method == "PUT":
        list_key_available.append(key)
        for i in range(len(l)):
            l[i][key] = value
            l[i]["modified_at"] = datetime.datetime.now(),
            l[i]["last_connection"] = datetime.datetime.now(),
        return Response(l, status=200)


