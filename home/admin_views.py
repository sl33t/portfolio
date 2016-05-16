from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from home.forms import BlogForm
from home.forms import PortfolioForm
from home.models import PortfolioItem, BlogPost


@login_required(login_url="/login/")
def admin(request):
    return render(request, "admin.html", {
        'blogForm': BlogForm(),
        'portfolioForm': PortfolioForm(),
        'blogPosts': BlogPost.objects.all(),
        'portfolio': PortfolioItem.objects.all()
    })


@login_required(login_url="/login/")
def add_blog_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        form.save()
    return redirect("/admin")


@login_required(login_url="/login/")
def update_blog_post(request, item_id):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=BlogPost.objects.get(pk=item_id))
        form.save()
        return redirect("/blogChange/edit/" + item_id + "/")
    else:
        item = BlogPost.objects.get(pk=item_id)
        return render(request, "editBlogPost.html", {
            'form': BlogForm(instance=item),
            'item': item
        })


@login_required(login_url="/login/")
def remove_blog_post(request, item_id):
    if request.method == "POST":
        specific_blog_post = BlogPost.objects.get(id=int(item_id))
        specific_blog_post.delete()
    return redirect("/admin")


@login_required(login_url="/login/")
def add_portfolio_item(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        form.save()
    return redirect("/admin")


@login_required(login_url="/login/")
def update_portfolio_item(request, item_id):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES, instance=PortfolioItem.objects.get(pk=item_id))
        form.save()
        return redirect("/portfolioChange/edit/" + item_id + "/")
    else:
        item = PortfolioItem.objects.get(pk=item_id)
        return render(request, "editPortfolio.html", {
            'form': PortfolioForm(instance=item),
            'item': item
        })


@login_required(login_url="/login/")
def remove_portfolio_item(request, item_id):
    if request.method == "POST":
        specific_portfolio_item = PortfolioItem.objects.get(id=int(item_id))
        specific_portfolio_item.delete()
    return redirect("/admin")
