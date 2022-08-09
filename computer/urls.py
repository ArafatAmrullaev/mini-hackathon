from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ComputerViewSet
from rating.views import add_rating

router = DefaultRouter()
router.register('computers', ComputerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/add_rating/<int:p_id>/', add_rating),
]