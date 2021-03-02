from django.urls import path
from . import views


urlpatterns = [
    path('',views.json_example_view),
    path('serializeddetailview/',views.SerilaizedDetailView.as_view(), name='serializedDetailView'),
    path('serializedlistview/',views.SerilaizedListView.as_view(), name='serializedListView'),
    
]