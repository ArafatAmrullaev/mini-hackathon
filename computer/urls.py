from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ComputerViewSet
from rating.views import add_rating, delete_rating

router = DefaultRouter()
router.register('computers', ComputerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('computers/add_rating/<int:c_id>/', add_rating),
    path('computers/delete_rating/<int:c_id>/', delete_rating),
]