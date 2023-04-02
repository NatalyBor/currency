# from time import time
from django.utils import timezone
from .models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # start = time()
        response = self.get_response(request)
        # end = time()
        # print(f'total: {end - start}')
        return response


class RequestResponseLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = timezone.now()

        response = self.get_response(request)

        end_time = timezone.now()
        time_difference = (end_time - start_time).microseconds // 1000

        log = RequestResponseLog(
            path=request.path,
            request_method=request.method,
            time=time_difference,
        )
        log.save()

        return response
