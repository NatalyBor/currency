# from django.urls import reverse
from django.utils import timezone
from rest_framework import serializers

from currency.models import Rate, Source, ContactUs

from django.core.mail import send_mail

# from app.settings import settings


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'source'
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name'
        )


class ContactUsSerializer(serializers.Serializer):
    email = serializers.EmailField()
    created = serializers.DateTimeField(default=timezone.now())
    name = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()

    class Meta:
        model = ContactUs
        fields = (
            'email',
            'created',
            'name',
            'subject',
            'message'
        )

    def create(self, validated_data):
        instance = ContactUs.objects.create(**validated_data)
        send_mail(
            'Instance {} has been created'.format(instance),
            'Here is the message. DATA: {}'.format(validated_data),
            'from@example.com',
            ['to@example.com']
        )
        return instance

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.message = validated_data.get('message', instance.message)
        instance.created = validated_data.get('created', instance.created)
        send_mail(instance.subject, instance.message, instance.email, ['to@example.com'])
        instance.save()
        return instance
