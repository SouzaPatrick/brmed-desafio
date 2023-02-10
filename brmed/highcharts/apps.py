from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HighchartsConfig(AppConfig):
    name = "brmed.highcharts"
    verbose_name = _("Highcharts")

    def ready(self):
        try:
            import brmed.users.signals  # noqa F401
        except ImportError:
            pass

