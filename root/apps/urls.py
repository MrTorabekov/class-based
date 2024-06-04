from django.urls import path
from .views import UserList, UsersDelete,UserUpdate

urlpatterns = [
    path('', UserList.as_view(), name="home"),
    path('delete/<int:pk>', UsersDelete.as_view(), name='delete'),
    path('detail/<int:pk>', UserUpdate.as_view(), name='detail'),
]