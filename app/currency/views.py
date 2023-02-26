from django.shortcuts import render
from django.http import HttpResponse

from currency.models import Rate, ContactUs


def list_rates(request):
    rates = Rate.objects.all()

    context = {
        'rates' : rates

    }

    return render(request, 'rates_list.html', context)

    # result = []
    # for rate in qs:
    #     result.append(f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency}, source: {rate.source}, created: {rate.created}<br>')
    # return HttpResponse(str(result))


# def contact_form(request):
#     qs = ContactUs.objects.all()
#     result = []
#     for client in qs:
#         result.append(f'id: {client.id}, email_from: {client.email_from}, subject: {client.subject}, message: {client.message} <br>')
#     return HttpResponse(str(result))

def contact_form(request):
    contactus = ContactUs.objects.all()
    context = {
        'contactus': contactus
    }

    return render(request, 'contact_us.html', context)
