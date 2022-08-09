from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, action
from rest_framework import filters
from .models import Rating
from computer.models import Computer

@api_view(['POST'])
def add_rating(request, c_id):
    user = request.user
    computer = get_object_or_404(Computer, id=c_id)
    value = request.POST.get('value')

    if not user.is_authenticated:
        raise ValueError('authentication credentials are not provided')

    if not value:
        raise ValueError('value is required')
    
    if Rating.objects.filter(user=user, computer=computer).exists():
        rating = Rating.objects.get(user=user, computer=computer)
        rating.value = value
        rating.save()

    else:
        Rating.objects.create(user=user, computer=computer, value=value)

    return Response('rating created', 201)

@api_view(['DELETE'])
def delete_rating(request, c_id):
    user = request.user
    computer = get_object_or_404(Computer, id=c_id)
    # delete_rating = request.DELETE.get('value')

    if not user.is_authenticated:
        raise ValueError('authentication credentials are not provided')
    
    if Rating.objects.filter(user=user, computer=computer).exists():
        rating = Rating.objects.get(user=user, computer=computer)
        # rating.value = value
        rating.delete()

    else:
        raise ValueError('rating does not exists')

    return Response('rating deleted', 201)