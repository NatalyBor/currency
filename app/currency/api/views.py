# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import kwargs as kwargs
# from certifi.__main__ import args
# from rest_framework import generics
# from django.core.mail import send_mail
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework import viewsets
from rest_framework.decorators import action

from currency.models import Rate, Source

from currency.api.serializers import RateSerializer, SourceSerializer
from rest_framework.permissions import AllowAny

# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# from rest_framework_xml.renderers import XMLRenderer
# from rest_framework_yaml.renderers import YAMLRenderer

from currency.api.serializers import ContactUsSerializer
from currency.filters import RateFilter, SourceFilter, ContactUsFilter
from currency.models import ContactUs
from currency.paginators import RatePagination, SourcePagination, ContactUsPagination
from currency.throttlers import AnonCurrencyThrottle


# @api_view(['GET'])
# def hello_world(request):
# 	data = {'hello': 'world'}
# 	return Response()

# class RateApiView(generics.ListCreateAPIView):
# 	queryset = Rate.objects.all().select_related('source')
# 	serializer_class = RateSerializer # perform json.dumps, json.loads
#
#
# class RateDetailApiView(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Rate.objects.all()
# 	serializer_class = RateSerializer
#

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    # renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = RatePagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = RateFilter
    ordering_fields = ('id', 'created', 'buy', 'sale')
    throttle_classes = (AnonCurrencyThrottle,)

    @action(detail=True, methods='POST', )
    def buy(self, request, *args, **kwargs):
        rate = self.get_object()
        # print(rate)  # send buy request
        sz = self.get_serializer(instance=rate)
        return Response(sz.data)


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    # renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = SourcePagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )

    filterset_class = SourceFilter
    ordering_fields = ('id', 'name', 'source_url')
    throttle_classes = (AnonCurrencyThrottle,)


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    pagination_class = ContactUsPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )

    filterset_class = ContactUsFilter
    ordering_fields = ('name', 'subject')
    throttle_classes = (AnonCurrencyThrottle,)
