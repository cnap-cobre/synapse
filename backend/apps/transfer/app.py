from django.apps import AppConfig

class TransferConfig(AppConfig):
    name = 'apps.transfer'

    def ready(self):
        import apps.transfer.signals