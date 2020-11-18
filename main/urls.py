from django.urls import path

from .views import (HomeView, APIListView, APIDetialView,
                    AddSuggestionView,mark_as_read_view,
                    ContactView)

app_name = 'main'
urlpatterns = [
    path('', HomeView.as_view(),name="home" ),
    path('apis/', APIListView.as_view(),name="list" ),
    path('apis/<slug:slug>/guide/', APIDetialView.as_view(),name="detail" ),
    path('apis/<slug:slug>/suggestion/add/',
          AddSuggestionView.as_view(),name="suggestion-add" ),
    path('suggestion/<pk>/read/',
          mark_as_read_view,name="suggestion-read" ),
    path('contact/', ContactView.as_view(),name="contact" ),
]
