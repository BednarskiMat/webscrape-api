from django.urls import path
from shows import views

urlpatterns = [
    path('update', views.run_scrape),
    path("",views.ListShowAPIView.as_view(),name="show_list"),
    
]