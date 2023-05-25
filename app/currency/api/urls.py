from django.urls import path
# from currency.api.views import RateApiView, RateDetailApiView

from rest_framework.routers import DefaultRouter

from currency.api.views import RateViewSet, SourceViewSet

from currency.api.views import ContactUsViewSet

# from currency.api.views import hello_world

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')
router.register(r'sources', SourceViewSet, basename='sources')
router.register(r'contactus', ContactUsViewSet, basename='sources')

urlpatterns = [
	# path('rates/', hello_world),
	# path('rates/', RateApiView.as_view(), name='rates'),
	# path('rates/<int:pk>/', RateDetailApiView.as_view(), name='rates-detail')
]

urlpatterns += router.urls