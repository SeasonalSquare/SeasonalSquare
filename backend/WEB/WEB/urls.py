from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

# drf_yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="제철의 광장 API",
      default_version='v0.8',
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', include('recipe_api.urls')),
    path('accounts/', include('accounts.urls')),
    # 직접 만든 적은 없지만 rest_auth라는 앱이 생긴다.
    # 로그인 & 로그아웃
    path('rest-auth/', include('rest_auth.urls')),
    # 회원가입
    path('rest-auth/signup/', include('rest_auth.registration.urls')),
    # drf_yasg
    path('swagger/json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    # url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('rest-auth/signup/', include('rest_auth.registration.urls'))
]
