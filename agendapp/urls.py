from django.urls import path
from . import views

app_name = 'agendapp'
urlpatterns = [
    path('', views.IndexUserView.as_view(), name='index'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('<int:pk>/edit/', views.EditUserView.as_view(), name='edit'),
    path('delete/<int:pk>', views.DeleteUserView.as_view(), name='delete')
]
