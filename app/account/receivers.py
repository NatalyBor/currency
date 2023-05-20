from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

User = get_user_model()


@receiver(pre_save, sender=User)
def user_pre_save_signal(sender, instance, **kwargs):
    print("pre_save")
    if instance.email:
        instance.email = instance.email.lower()


@receiver(post_save, sender=User)
def user_post_save_signal(sender, **kwargs):
    print("post_save")


@receiver(pre_save, sender=User)
def user_phone_pre_save_signal(sender, instance, **kwargs):
    print("pre_save")
    if instance.phone:
        if type(instance.phone) != int:
            choices = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            phone = ""
            for _ in instance.phone:
                if _ in choices:
                    phone = phone + _
            print('Phone: ', phone)
            instance.phone = int(phone)


@receiver(post_save, sender=User)
def user_phone_post_save_signal(sender, **kwargs):
    print("post_save")
