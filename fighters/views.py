from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Fighter
from django.http import JsonResponse

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


def fightCardDetail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    fight_card = getattr(event, 'fight_card', None)

    breadcrumb_items = [
        {"name": "Home", "item": request.build_absolute_uri('/')},
        {"name": "Events", "item": request.build_absolute_uri('/events/')},
        {"name": event.name, "item": request.build_absolute_uri()}
    ]

    context = {
        "event": event,
        "fight_card": fight_card,
        "seo_object": event,
        "breadcrumb_items":breadcrumb_items
    }

    return render(request, "fightcard_detail.html", context)

def fighter_detail(request, slug):
    fighter = get_object_or_404(Fighter, slug=slug)

    breadcrumb_items = [
        {"name": "Home", "item": request.build_absolute_uri('/')},
        {"name": "Fighters", "item": request.build_absolute_uri('/fighters/')},
        {"name": fighter.first_name, "item": request.build_absolute_uri()}
    ]


    context = {
        "event": fighter,
        "seo_object": fighter,
        "breadcrumb_items":breadcrumb_items
    }

    return render(request, "fightcard_detail.html", context)
