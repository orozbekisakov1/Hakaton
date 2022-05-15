def post_list(request):
    posts = Post.published.all()

    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'blog/post/detail.html', {'post': post})


def category_detail(request, category):
    category = get_object_or_404(Category, slug=category)
    return render(request, 'blog/post/category.html', {'category': category})
