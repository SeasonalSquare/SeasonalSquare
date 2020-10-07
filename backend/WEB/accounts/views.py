# rest_framework
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
# auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST

# django model
from django.shortcuts import render, get_object_or_404
from .models import Allergy, Vegetarian
from .serializers import UserSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def allergy_vegan(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        data = {
            'allergy': None,
            'vegetarian': None,
        }
        temp = []
        for a_pk in serializer.data['allergy']:
            allergy_model = get_object_or_404(Allergy, pk=a_pk)
            temp.append(allergy_model.a_type)
        data['allergy'] = temp
        v_pk = serializer.data['vegetarian']
        if v_pk:
            vegi_model = get_object_or_404(Vegetarian, pk=v_pk)
            data['vegetarian'] = vegi_model.v_type
        return Response(data)
    else:
        allergy_list = request.data['allergy_list']
        user.allergy.set([])
        for a_type in allergy_list:
            allergy_model = get_object_or_404(Allergy, a_type=a_type)
            user.allergy.add(allergy_model)
        v_type = request.data['vegetarian']
        user.vegetarian = None
        if v_type:
            vegi_model = get_object_or_404(Vegetarian, v_type=v_type)
            user.vegetarian = vegi_model
        user.save()
        return Response(True)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def cart(request):
    user = request.user
    if request.method == 'GET':
        shoppinglist = user.get_shop_data()
        return Response(shoppinglist)
    elif request.method == 'POST':
        shoppinglist = request.data['shoppinglist']
        user.set_shop_data(shoppinglist)
        user.save()
        return Response(True)
    elif request.method == 'PUT':
        shoppinglist = user.get_shop_data()
        shoppinglist += request.data['shoppinglist']
        user.set_shop_data(shoppinglist)
        user.save()
        return Response(True)
    else:
        user.shoppingcart = None
        user.save()
        return Response(True)