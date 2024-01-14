from django.apps import AppConfig

print('**************************** apps')
class TradingcenterConfig(AppConfig):
    name = 'TradingCenter'
    def ready(self):
        import TradingCenter.mysignal