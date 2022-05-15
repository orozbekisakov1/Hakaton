from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.db.models import Q
from blog.models import Post, Place
from product.models import Category, Product
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


# def shop_app(request):
#     return render(request, 'blog/shop.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'object_list'
    ordering = ['-post_date']  #выводит последний добавленный пост

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(title__incontains=query) |
                Q(author__username__incontains=query)
            )
        return qs

 
class ProductListView(ListView):
    model = Product
    template_name = 'blog/shop_list.html'
    context_object_name = 'product_list'  #выводит последний добавленный пост

    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.all()
        for q in qs:
            print(q.category)
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) #|
                # Q(author__username__incontains=query)
            )
        return qs

class ProductListArtsView(ListView):
    model = Product
    template_name = 'blog/arts.html'
    context_object_name = 'product_list'
    ordering = ['-added_date']  #выводит последний добавленный пост

    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(title__incontains=query) |
                Q(author__username__incontains=query)
            )
        return qs


class ProductListHandeView(ListView):
    model = Product
    template_name = 'blog/handmade.html'
    context_object_name = 'product_list'
    ordering = ['-added_date']  #выводит последний добавленный пост

    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(title__incontains=query) |
                Q(author__username__incontains=query)
            )
        return qs

class PlaceListView(ListView):
    model = Place
    template_name = 'blog/place.html'
    context_object_name = 'place_list'
    ordering = ['-post_date']

    def get_queryset(self, *args, **kwargs):
        qs = Place.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(title__incontains=query) |
                Q(author__username__incontains=query)
            )
        return qs



class PostCreateView(LoginRequiredMixin, CreateView): #запрашивает залогиниться логинреквайрд
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #[2] когда поля заполняем чтобы все было правильно-проверяет
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: #если юзер это автор то тру
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #[2] if u r author you can delete it
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




class PostCreateView(LoginRequiredMixin, CreateView): #запрашивает залогиниться логинреквайрд
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #[2] когда поля заполняем чтобы все было правильно-проверяет
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: #если юзер это автор то тру
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #[2] if u r author you can delete it
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




