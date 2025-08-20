import json
from django.shortcuts import get_object_or_404, render
from .models import Event
from django.core.paginator import Paginator

def fightCardDetail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    fight_card = getattr(event, 'fight_card', None)

    # Structured data for SEO
    structured_data = {
        "@context": "https://schema.org",
        "@type": "SportsEvent",
        "name": event.name,
        "startDate": event.date.isoformat(),
        "url": request.build_absolute_uri(),
        "image": request.build_absolute_uri(event.banner.url) if event.banner else "",
    }

    context = {
        "event": event,
        "fight_card": fight_card,
        "structured_data": json.dumps(structured_data),
        "meta_title": event.meta_title,
        "meta_description": event.meta_description
    }

    return render(request, "fightcard_detail.html", context)


def events_list(request):
    events = Event.objects.all().order_by('-date')

    # attach the main_event to each event
    for event in events:
        main_event = event.fight_card.matches.filter(is_main_event=True).first()
        event.main_event = main_event

    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "fight_cards.html", {"page_obj": page_obj})