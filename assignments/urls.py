from django.urls import path
from . import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Assignment API",
      default_version='v1',
      description="Create and view assignment and search by tags",
      terms_of_service="https://assignment/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

#initial path assignment/
urlpatterns = [
    path('create/', views.create_assignment),
    path('id=<pk>/', views.get_assignment),
    path('tag=<str:tag>/', views.search_assignments),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]