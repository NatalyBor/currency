from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import account.receivers  # noqa: F401
