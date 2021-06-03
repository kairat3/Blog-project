from django.urls import path, include, re_path

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, permissions
from blog.views import CustomLogoutView, ProductImagesViewSet
from blog_api.views import UserRegistrationView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    info=openapi.Info(
        title='Blog Project',
        default_version='v1',
        description='this is test blog project',
        terms_of_service='http://www.google.com/policies/terms/',
        contact=openapi.Contact(email='test@gmail.com',),
        license=openapi.License(name='BSD Licence')
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

router = routers.SimpleRouter()
router.register('post_images', ProductImagesViewSet)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('blog_api.urls')),
    path('api/v1/users/register/', UserRegistrationView.as_view()),
    path('api/v1/rest-auth/logout/', CustomLogoutView.as_view()),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)