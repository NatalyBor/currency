from django.urls import path
# from currency.views import contact_form
from currency.views import (
    RateListView,
    RateCreateView,
    RateDetailView,
    RateUpdateView,
    RateDeleteView,
    ContactListView,
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    ContactUsCreateView,
)

app_name = 'currency'

urlpatterns = [
    path('rate/list', RateListView.as_view(), name='rate-list'),
    path('contactus', ContactListView.as_view(), name='contact-form'),

    path('rate/create', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('source/list', SourceListView.as_view(), name='source-list'),
    path('source/create', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('contact-us/create/', ContactUsCreateView.as_view(), name='contact-us-create'),
]
