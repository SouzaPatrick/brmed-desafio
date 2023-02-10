from django.views.generic import TemplateView


class HighchartsView(TemplateView):
    template_name = "pages/highcharts.html"
