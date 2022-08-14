from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import base64



class Index(View):
    def get(self, request):
        context = {"a":1}
        template = "viewer/main_page.html"
        return render(request, template, context)

class NextMedia(APIView):
    def get(self, request):
        with open("C:/Users/KukardRS/Downloads/MicrosoftTeams-image.png", "rb") as imageFile:
            image_byte_string = base64.b64encode(imageFile.read())
        return Response({"status_code": 200, "image": image_byte_string, "video": None})