
from django.urls import path,include
from . models import Post
from .serializers import PostSerializer
from todo import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import PostListApi

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="Test API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('posts/', views.PostListApi.as_view()),
    path('post/delete/<int:pk>/',views.PostDeleteApi.as_view()),
    path('post/update/<int:pk>/',views.PostUpdateApi.as_view()),
    path('post/create/',views.PostCreateApi.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
