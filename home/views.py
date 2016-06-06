from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from home.forms import ContactForm
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


def blog(request):
    return render(request, "blog.html", {
        'blog_items': BlogPost.objects.all()
    })


def blog_post(request, item_id="0"):
    return render(request, "blog_post.html", {
        "item": get_object_or_404(BlogPost, id=int(item_id))
    })


def contact(request):
    return render(request, "contact.html", {'form': ContactForm()})


@require_POST
def send_email(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        message = form.cleaned_data['message'] + "\n"
        message += form.cleaned_data['name'] + " at "
        message += form.cleaned_data['sender']
        send_mail(subject=form.cleaned_data['reason'],
                  message=message,
                  from_email="contactForm@rickycatron.com",
                  recipient_list=['dev@rickycatron.com'],
                  fail_silently=False)
        feedback = "Thanks for your message."
        feedback += "I will get back to you shortly."
        messages.info(request, feedback)
    else:
        feedback = "Your email failed!"
        feedback += "Please try again."
        messages.error(request, feedback)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
