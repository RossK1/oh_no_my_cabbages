from django.urls import include, path

urlpatterns = [
    path('viewer/', include('viewer.urls')),
]