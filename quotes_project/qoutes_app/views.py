from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Quote, Author


# Create your views here.
def main(request):
    quotes = Quote.objects.all().select_related('author').prefetch_related('tags')
    tags = Tag.objects.all()
    print(quotes)
    print(tags)
    return render(request, 'qoutes_app/index.html', {'quotes': quotes})


@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='qoutes_app:main')
        else:
            return render(request, 'qoutes_app/tag.html', {'form': form})

    return render(request, 'qoutes_app/tag.html', {'form': TagForm()})


@login_required
def quote(request):
    tags = Tag.objects.filter(user=request.user).all()
    author = Author.objects.filter(user=request.user).all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='qoutes_app:main')
        else:
            return render(request, 'qoutes_app/quote.html', {"author": author,"tags": tags, 'form': form})
    return render(request, 'qoutes_app/quote.html', {"author": author, "tags": tags, 'form': QuoteForm()})


@login_required
def author(request):

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to='qoutes_app:main')
        else:
            return render(request, 'qoutes_app/author.html', {'form': form})
    return render(request, 'qoutes_app/author.html', {'form': AuthorForm()})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'qoutes_app/author_detail.html', {'author': author})