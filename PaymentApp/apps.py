from django.apps import AppConfig


class PaymentAppConfig(AppConfig):
    name = 'PaymentApp'

    def ready(self):
        import PaymentApp.signals