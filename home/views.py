from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from home.forms import BlogForm, ContactForm, LoginForm
from home.forms import PortfolioForm
from home.models import PortfolioItem, BlogPost


def index(request):
    return render(request, "index.html", {
        'portfolioSnapshot': PortfolioItem.objects.all().order_by("-id")[:3]
    })


def portfolio(request):
    return render(request, "portfolio.html", {
        'portfolio_items': PortfolioItem.objects.all()
    })


def portfolio_item(request, item_id="0"):
    return render(request, "portfolio_item.html", {
        "item": get_object_or_404(PortfolioItem, id=int(item_id))
    })


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
        print(request.user.is_authenticated())
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


def blog(request):
    return render(request, "blog.html", {
        'blog_items': BlogPost.objects.all()
    })


def blog_post(request, item_id="0"):
    return render(request, "blog_post.html", {
        "item": get_object_or_404(BlogPost, id=int(item_id))
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
        print(request.user.is_authenticated())
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


def contact(request):
    return render(request, "contact.html", {'form': ContactForm()})


def send_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(subject=form.cleaned_data['reason'],
                      message=form.cleaned_data['message'] + "\n"
                              + form.cleaned_data['name'] + " at "
                              + form.cleaned_data['sender'],
                      from_email="contactForm@rickycatron.com",
                      recipient_list=['dev@rickycatron.com'],
                      fail_silently=False)
    return redirect("/")


@login_required(login_url="/login/")
def admin(request):
    print(request.user.is_authenticated())
    return render(request, "admin.html", {
        'blogForm': BlogForm(),
        'portfolioForm': PortfolioForm(),
        'blogPosts': BlogPost.objects.all(),
        'portfolio': PortfolioItem.objects.all()
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            login(request, user)
            return redirect("/admin")
        except:
            return redirect("/")
    else:
        return render(request, "login.html", {
            'loginForm': LoginForm(),
        })


def logout_view(request):
    logout(request)
    return redirect("/")
