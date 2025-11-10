import json
from django.shortcuts import get_object_or_404, render
from .models import Event
from django.core.paginator import Paginator


def test_event_meta(request, slug):
    event = get_object_or_404(Event, slug=slug)
    print("Rendering template with event:", event)
    return render(request, 'test_event_meta.html', {'event': event})


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

def fightCardVideoPlayer(request, slug):
    event = get_object_or_404(Event, slug=slug)
    

    breadcrumb_items = [
        {"name": "Home", "item": request.build_absolute_uri('/')},
        {"name": "Events", "item": request.build_absolute_uri('/events/')},
        {"name": event.name, "item": request.build_absolute_uri()}
    ]

    context = {
        "event": event,
        "seo_object": event,
        "breadcrumb_items":breadcrumb_items
    }

    return render(request, "fightCardPlayer.html", context)


def events_list(request):
    events = Event.objects.all().order_by('-date')

    # attach the main_event (if it exists) to each event
    for event in events:
        if hasattr(event, "fight_card"):  # make sure fight_card exists
            main_event = event.fight_card.matches.filter(is_main_event=True).first()
        else:
            main_event = None
        event.main_event = main_event

    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "fight_cards.html", {"page_obj": page_obj,"seo_object": events.first()})