from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# a function based view to show index page
"""
def index(request):
    return  HttpResponse('Hi')


"""


class indexview(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        return context


""" Function Base View for Redirect
def redirectToMaktab(request):
    return redirect('https://fahimreza.ir')

"""


class redirectToMaktab(RedirectView):
    url = "https://fahimreza.ir"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class Posts(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    template_name = "base.html"
    permission_required = "blog.view_post"
    context_object_name = "posts"
    paginate_by = 3
    redirect_field_name = "redirect_to"

    ordering = ["id"]
    # def get_queryset(self):
    #     posts=Post.objects.filter(status = True)
    #     return posts


class PostDetails(LoginRequiredMixin, DetailView):
    model = Post


"""
class PostCreateView(FormView):
    template_name = 'blog/contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/contact.html"
    success_url = "/blog/post/"
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = "/blog/post/"
    template_name = "blog/contact.html"
    form_class = PostForm


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"
    template_name = "blog/delete_form.html"


# ---------------------------  Api


@api_view()
def api_post_list_view(request):
    return Response({"name": "fahimreza.ir"})
