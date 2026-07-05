from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages
from app1.forms import ContactForm, NewsletterForm
from app2.models import Post
from app1.models import Contact

def home_view(request):
    posts = Post.objects.filter(
        status=True,
        published_at__lte=timezone.now()
        ).order_by('-published_at')[:6].prefetch_related('category') # prefetch because of the query for categories in the template

    context = {'posts': posts}
    return render(request, 'app1/index.html', context)

def about_view(request):
    return render(request, 'app1/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # c = form.save(commit=False)
            # c.name = 'unknown'
            # c.save()

            messages.success(request, 'Commit Successfully!')
        else:
            messages.error(request, 'Invalid Contact!')

    form = ContactForm()

    return render(request, "app1/contact.html", {'form': form})

def elements_view(request):
    return render(request, "app1/elements.html")

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    
    else:
        return HttpResponseRedirect('/')
    
    # we dont render anything here !!!

def test(request):

    return render(request, 'app1/test.html')