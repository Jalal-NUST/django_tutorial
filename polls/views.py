from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name= 'polls/home.html'

class AboutPageView(TemplateView):
    template_name= 'polls/about.html'

