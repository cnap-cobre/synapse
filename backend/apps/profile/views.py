from django.views.generic.base import TemplateView


class UserProfileView(TemplateView):
    template_name = "profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_title'] = 'Profile'
        return context
