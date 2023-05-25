# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import PasswordResetForm
# from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth.views import PasswordContextMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView
# from django.http import HttpResponse, HttpResponseRedirect, Http404
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm
from django_filters.views import FilterView

from currency.filters import RateFilter
from currency.filters import SourceFilter

from currency.filters import ContactUsFilter


class RateListView(FilterView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all().select_related('source')
    paginate_by = 10
    filterset_class = RateFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'

        )
        return context

    def dispatch(self, request, *args, **kwargs):
        # print('before in view')
        result = super().dispatch(request, *args, **kwargs)
        # print('after in view')
        return result


class RateDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'

    def test_func(self):
        return self.request.user.is_authenticated

    # def dispatch(self, request, *args, **kwargs):
    #     print('before')
    #     start = time()
    #     result = super().dispatch(request, *args, **kwargs)
    #     print('after')
    #     end = time()
    #     print(f'time: {end - start}')
    #     return result


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactListView(FilterView):
    template_name = 'contact_us.html'
    queryset = ContactUs.objects.all()
    paginate_by = 10
    filterset_class = ContactUsFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page'

        )
        return context


class ContactUsCreateView(CreateView):
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    model = ContactUs
    fields = (
        'created',
        'name',
        'email',
        'subject',
        'message',
    )

    # def _slow(self):
    #     from time import sleep
    #     sleep(10)

    def _send_mail(self):
        # cleaned_data = form.cleaned_data
        subject = 'User ContactUs'
        # recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
            Request from: {self.object.name},
            Reply to email: {self.object.email},
            Subject: {self.object.subject},
            Body: {self.object.message},
        '''
        from currency.tasks import send_mail
        # send_mail.delay(subject, message)
        # from datetime import datetime, timedelta
        send_mail.apply_async(
            kwargs={'subject': subject, 'message': message},

            # eta=datetime.now() + timedelta(seconds=10),
            countdown=20
        )
        # from django.core.mail import send_mail
        # self._slow()
        # send_mail(
        #     subject,
        #     message,
        #     recipient,
        #     [recipient],
        #     fail_silently=False,
        # )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect


class SourceListView(FilterView):
    template_name = 'source_list.html'
    queryset = Source.objects.all()
    paginate_by = 10
    filterset_class = SourceFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_pagination'] = '&'.join(
            f'{key}={value}' for key, value in self.request.GET.items() if key != 'page')
        return context


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()

# class ProfileView(LoginRequiredMixin, UpdateView):
#     template_name = 'registration/profile.html'
#     success_url = reverse_lazy('index')
#     # model = get_user_model()
#     queryset = get_user_model().objects.all()
#     fields = (
#         'first_name',
#         'last_name',
#     )
#
#     def get_object(self, queryset=None):
#         return self.request.user

# def get_queryset(self):
#     queryset = super().get_queryset()
#     queryset = queryset.filter(id=self.request.user.id)
#     return queryset
# def list_rates(request):
#     rates = Rate.objects.all()
#     context = {
#         'rates': rates
#     }
#
#     return render(request, 'rates_list.html', context)

# result = []
# for rate in qs:
#     result.append(f'id: {rate.id}, buy: {rate.buy}, sale: {rate.sale}, currency: {rate.currency}, source: {rate.source}, created: {rate.created}<br>')
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
#     return render(request, 'source_update.html', context)
