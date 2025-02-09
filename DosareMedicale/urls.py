from django.urls import path
from . import views
from DosareMedicale.views import PetRecordCreateView, FormSuccessView, PetRecordListView, PetRecordEditView

urlpatterns = [
    path('dosare-medicale/', PetRecordCreateView.as_view(), name='dosare_medicale'),
    path('form-success/<int:pk>/', FormSuccessView.as_view(), name='form_success'),
    path('dosare-salvate/', PetRecordListView.as_view(), name='pet_record_list'),
    path('delete/<int:pk>/', views.delete_pet_record, name='delete'),
    path('modifica/<int:pk>', PetRecordEditView.as_view(), name='modifica'),
]