from django.urls import path
from . import views
from DosareMedicale.views import PetRecordCreateView, FormSuccessView, PetRecordListView, PetRecordDeleteView, PetRecordEditView

urlpatterns = [
    path('dosare-medicale/', PetRecordCreateView.as_view(), name='dosare_medicale'),
    path('form-success/<int:pk>/', FormSuccessView.as_view(), name='form_success'),
    path('dosare-salvate/', PetRecordListView.as_view(), name='pet_record_list'),
    path('delete/<int:pk>/', PetRecordDeleteView.as_view(), name='delete'),
    path('modifica/<int:pk>', PetRecordEditView.as_view(), name='modifica'),
]