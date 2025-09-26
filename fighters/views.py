from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Fighter
from fightCards.models import Match
from django.http import JsonResponse
from django.db.models import Q

def allFighters(request):
    fighters_qs = Fighter.objects.all().order_by('last_name')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(fighters_qs, 8)
    fighters = paginator.get_page(page_number)

    breadcrumb_items = [
        {"name": "Home", "item": request.build_absolute_uri('/')},
        {"name": "Fighters", "item": request.build_absolute_uri('/fighters/')},
    ]

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render(request, "_fighter_cards.html", {"fighters": fighters}).content.decode('utf-8')
        return JsonResponse({
            'html': html,
            'has_next': fighters.has_next()  # key change here
        })

    return render(request, "allFighters.html", {
        "fighters": fighters,
        "breadcrumb_items": breadcrumb_items
    })



def fighter_detail(request, slug):
    fighter = get_object_or_404(Fighter, slug=slug)
    articles = fighter.articles.all()

    # Pull all matches where this fighter was red or blue
    previous_fights = Match.objects.filter(
        Q(fighter_red=fighter) | Q(fighter_blue=fighter)
    ).order_by('-fight_card__event__date')  

    breadcrumb_items = [
        {"name": "Home", "item": request.build_absolute_uri('/')},
        {"name": "Fighters", "item": request.build_absolute_uri('/fighters/')},
        {"name": fighter.first_name, "item": request.build_absolute_uri()}
    ]

    context = {
        "fighter": fighter,
        "previous_fights": previous_fights,
        "articles":articles,
        "seo_object": fighter,
        "breadcrumb_items": breadcrumb_items
    }

    return render(request, "fighterProfile.html", context)
