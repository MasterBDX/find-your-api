from django.urls import path

from .views import (HomeView, APIListView, APIDetialView,
                    AddSuggestionView,mark_as_read_view,
                    ContactView)

app_name = 'main'
urlpatterns = [
    path('', HomeView.as_view(),name="home" ),
    path('guide/', APIListView.as_view(),name="list" ),
    path('guide/<slug:slug>/api/', APIDetialView.as_view(),name="detail" ),
    path('guide/<slug:slug>/suggestion/add/',
          AddSuggestionView.as_view(),name="suggestion-add" ),
    path('suggestion/<pk>/read/',
          mark_as_read_view,name="suggestion-read" ),
    path('contact/', ContactView.as_view(),name="contact" ),
]
