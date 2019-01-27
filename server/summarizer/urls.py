from django.contrib import admin
from django.urls import path, re_path
from summarizer.views import check, execute

urlpatterns = [
    path('check/<slug:ytube_id>/', check),
    path('execute/<slug:ytube_id>/<int:percent>/', execute),
]
