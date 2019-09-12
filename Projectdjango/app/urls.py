from django.urls import path
from app.views import index_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',index_view),
]