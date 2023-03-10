# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
# from django.http import HttpResponseRedirect
# from django.http import HttpResponse, HttpResponseRedirect, Http404

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm


class RateListView(ListView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all()


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactListView(ListView):
    template_name = 'contact_us.html'
    queryset = ContactUs.objects.all()


class SourceListView(ListView):
    template_name = 'source_list.html'
    queryset = Source.objects.all()


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()


# def list_rates(request):
#     rates = Rate.objects.all()
#
#     context = {
#         'rates': rates
#     }
#
#     return render(request, 'rates_list.html', context)

# result = []
# for rate in qs:
#     result.append(f'id: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, currency: {rate.currency}, source: {rate.source}, created: {rate.created}<br>')
# return HttpResponse(str(result))

# get details

# def rates_details(request, pk):
#     rate = get_object_or_404(Rate, pk=pk)
#
#     context = {
#         'rate': rate
#     }
#
#     return render(request, 'rates_details.html', context)

# def rates_create(request):
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list')
#     elif request.method == 'GET':
#         form = RateForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'rates_create.html', context)

# def rates_update(request, pk):
#     rate = get_object_or_404(Rate, pk=pk)
#     if request.method == 'POST':
#         form = RateForm(request.POST, instance=rate)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/rate/list')
#     elif request.method == 'GET':
#         # try:
#         #     rate = Rate.objects.get(id=pk)
#         # except Rate.DoesNotExist:
#         #     raise Http404('Rate does not exist')
#         form = RateForm(instance=rate)
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'rates_update.html', context)

# def rates_delete(request, pk):
#     rate = get_object_or_404(Rate, pk=pk)
#
#     if request.method == 'POST':
#         rate.delete()
#         return HttpResponseRedirect('/rate/list')
#     elif request.method == 'GET':
#         context = {
#            'rate': rate
#         }
#
#     return render(request, 'rates_delete.html', context)

# def contact_form(request):
#     qs = ContactUs.objects.all()
#     result = []
#     for client in qs:
#         result.append(f'id: {client.id}, email_from: {client.email_from}, subject: {client.subject}, message: {client.message} <br>')
#     return HttpResponse(str(result))

# def contact_form(request):
#     contactus = ContactUs.objects.all()
#     context = {
#         'contactus': contactus
#     }
#
#     return render(request, 'contact_us.html', context)

# source
# def source_list(request):
#     sources = Source.objects.all()
#
#     context = {
#         'sources': sources
#     }
#
#     return render(request, 'source_list.html', context)
#
#
# def source_create(request):
#     if request.method == 'POST':
#         form = SourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/list')
#     elif request.method == 'GET':
#         form = SourceForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'source_create.html', context)
#
#
# def source_update(request, pk):
#     source = get_object_or_404(Source, pk=pk)
#     if request.method == 'POST':
#         form = SourceForm(request.POST, instance=source)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/source/list')
#     elif request.method == 'GET':
#         form = SourceForm(instance=source)
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'source_update.html', context)
