from django.shortcuts import render,get_object_or_404

from .models import Article




def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
   

    breadcrumb_items = [
        {"name": "Home", "item": request.build_absolute_uri('/')},
        {"name": "articles", "item": request.build_absolute_uri('/articles/')},
        {"name": article.title, "item": request.build_absolute_uri()}
    ]

    context = {

        "article":article,
        "seo_object": article,
        "breadcrumb_items": breadcrumb_items
    }

    return render(request, "article_detail.html", context)