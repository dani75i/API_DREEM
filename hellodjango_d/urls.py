
from django.contrib import admin
from django.urls import path

from appone import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="API Dreem")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('headband/', views.headband),
    path('headband/id/<str:id>', views.headband_id),
    path('headband/id/<str:id>/key/<str:key>', views.delete_content_for_one_headband),
    path('headband/id/<str:id>/key/<str:key>/value/<str:value>', views.add_content_for_one_headband),
    path('headbands/key/<str:key>', views.delete_content_for_all_headbands),
    path('headbands/key/<str:key>/value/<str:value>', views.add_content_for_all_headbands),

]
