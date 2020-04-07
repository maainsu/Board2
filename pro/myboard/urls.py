from django.urls import path
from myboard import views

urlpatterns = [
    path('boardList/', views.showList),
    path('boardContent/', views.showContent),
    path('write/', views.writeContent),
    path('writeOk/', views.writeContentOk),
    path('modify/', views.modifyContent),
    path('modifyOk/', views.modifyContentOk),
    path('delete/', views.deleteContent),
]