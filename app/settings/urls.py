from django.contrib import admin
# from django.contrib.auth import views
# from django.contrib.auth.views import PasswordResetView
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from .views import password_reset_request

from currency.views import IndexView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('account/', include('account.urls')),

    path('auth/login/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', IndexView.as_view(template_name='index.html'), name='index'),

    path('', include('currency.urls')),

    path('', IndexView.as_view()),
]
