from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('register/', RegisterUserForm.as_view(), name='register'),
    path('login/', LoginUserForm.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('', shop_list, name='shop_list'),
    path('<slug:category_slug>/', shop_list, name='shop_list_by_category'),
    path('<int:id>/<slug:slug>', shop_detail, name='shop_detail'),
]
