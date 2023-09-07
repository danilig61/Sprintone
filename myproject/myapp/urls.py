from .views import PassListCreateView
from django.urls import path

urlpatterns = [
    path('api/pass/', PassListCreateView.as_view(), name='pass-list-create'),
    path('api/pass/submitData', PassListCreateView.as_view(), name='pass-submit-data'),
]