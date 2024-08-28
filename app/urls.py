from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    # Page
    path('', views.home, name='home'),

    # Resource
    path('resource', views.resource_list, name='resource_list'),
    path('resource/create', views.create_resource, name='create_resource'),
    path('resource/url/<path:public_url>/path/<path:path>/download', views.download_resource_item,
         name='download_resource_item'),
    path('resource/<path:public_url>/meta-data', views.resource_meta_data, name='resource_meta_data'),
    path('resource/<path:public_url>/meta-data/update', views.update_resource_meta_data,
         name='update_resource_meta_data'),
    path('resource/<path:public_url>/delete', views.delete_resource, name='delete_resource'),
    path('resource/<path:public_url>', views.resource_detail, name='resource_detail'),
]
