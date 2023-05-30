from currency.models import ContactUs
from django.utils import timezone


def test_get_contact_us(client):
    response = client.get('/currency/contact-us/create/')
    assert response.status_code == 200


def test_post_empty_form(client):
    response = client.post('/currency/contact-us/create/')
    assert response.status_code == 200


def test_post_empty_errors(client):
    response = client.post('/currency/contact-us/create/')
    assert response.context_data['form']._errors == {
        'created': ['This field is required.'],
        'name': ['This field is required.'],
        'email': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
    }


def test_post_invalid_email_200(client):
    payload = {
        'name': 'Igor',
        'email': 'INVALID_EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.status_code == 200


def test_post_invalid_email_error(client):
    payload = {
        'name': 'Igor',
        'email': 'INVALID_EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.context_data['form']._errors == {
        'created': ['This field is required.'],
        'email': ['Enter a valid email address.']
    }


def test_post_valid_email(client):
    initial_count = ContactUs.objects.count()
    payload = {
        'created': timezone.now(),
        'name': 'Igor',
        'email': 'igor@exaple.com',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.status_code == 302
    assert response['location'] == '/'
    assert ContactUs.objects.count() == initial_count + 1


def test_post_valid_data(client, mailoutbox, settings):
    initial_count = ContactUs.objects.count()
    payload = {
        'created': timezone.now(),
        'name': 'Igor',
        'email': 'igor@exaple.com',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contact-us/create/', data=payload)
    assert response.status_code == 302
    assert response['location'] == '/'
    assert ContactUs.objects.count() == initial_count + 1
    assert len(mailoutbox) == 1
    assert mailoutbox[0].from_email == settings.DEFAULT_FROM_EMAIL
