from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import base64
from os import listdir
from os.path import isfile, join, splitext
import random
import mimetypes
import cv2


class Index(View):
    def get(self, request):
        context = {"a":1}
        template = "viewer/main_page.html"
        return render(request, template, context)

class NextMedia(APIView):
    def get(self, request):
        media_folder = "C:/Temp/django_media/"
        files_in_folder = [f for f in listdir(media_folder) if isfile(join(media_folder, f))]
        filename = random.choice(files_in_folder)
        filepath = join(media_folder, filename)
        _, extension = splitext(filename)
        image_byte_string = None
        video_byte_string = None
        mime_type = mimetypes.guess_type(filename)[0]
        with open(filepath, "rb") as imageFile:
            file_data = base64.b64encode(imageFile.read())
            if extension in (".jpg", ".png"):
                image_byte_string = file_data
            elif extension in (".mp4"):
                print("video file")
                video_byte_string = file_data
        return Response({"status_code": 200, "image": image_byte_string, "video": video_byte_string, "mime_type":mime_type, "delay":5000})