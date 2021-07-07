from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='subscribe-index'),
    # path('about/', views.about, name='jobsite-about'),
    # path('signin/', views.signin, name='jobsite-signin'),
    # path('signup/', views.signup, name='jobsite-signup'),
    # path('job/<int:pk>/', JobDetailView.as_view(), name='career-detail'),
]
