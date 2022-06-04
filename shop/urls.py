from django.urls import path
from .views import shop_list, shop_detail

app_name = 'shop'

urlpatterns = [
    path('', shop_list, name='shop_list'),
    path('<slug:category_slug>/', shop_list, name='shop_list_by_category'),
    path('<int:id>/<slug:slug>', shop_detail, name='shop_detail')
]
