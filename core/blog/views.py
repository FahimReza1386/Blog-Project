from django.shortcuts import render , HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect , get_object_or_404
from django.views.generic.base import RedirectView

from .models import Post

# Create your views here.

#a function based view to show index page
"""

def index(request):
    return  HttpResponse('Hi')


"""
class indexview(TemplateView):
    """
        a class based view to show index page
    """
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name']= 'ali'
        return context

""" Function Base View for Redirect
def redirectToMaktab(request):
    return redirect('https://fahimreza.ir')

"""


class redirectToMaktab(RedirectView):
    url = 'https://fahimreza.ir'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args,**kwargs)
