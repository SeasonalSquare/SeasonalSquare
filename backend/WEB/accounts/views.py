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

# from .forms import CustomUserCreationForm
# from .models import Post


# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication,))
# def posts(request):
#     posts = Post.objects.filter(
#         published_at__isnull=False).order_by('-published_at')
#     post_list = serializers.serialize('json', posts)
#     return HttpResponse(post_list, content_type="text/json-comment-filtered")


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def set_allergy(request):
    print(request.data)
    user = request.user
    allergy_list = request.data['allergy_list']
    for a_type in allergy_list:
        allergy_model = get_object_or_404(Allergy, a_type=a_type)
        user.allergy.add(allergy_model)
    vegan_list = request.data['vegan_list']
    for v_type in vegan_list:
        vegi_model = get_object_or_404(Vegetarian, v_type=v_type)
        user.vegetarian.add(vegi_model)
    return Response(True)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def cart(request):
    user = request.user
    shoppinglist = request.data['shoppinglist']
    user.shoppingcart.delete()
    for shop in shoppinglist:
        user.shoppingcart.add(shop)
    return Response
