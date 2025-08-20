from django.shortcuts import render
from django.utils import timezone
from fightCards.models import Event  



def home(request):
    now = timezone.now().date()

    # Get next 3 upcoming events
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')[:3]

    # Prefetch related fight cards and matches with fighters
    # This reduces DB queries and improves efficiency
    upcoming_events = upcoming_events.prefetch_related(
        'fight_card__matches__fighter_red',
        'fight_card__matches__fighter_blue'
    )

    context = {
        "upcoming_events": upcoming_events
    }

    return render(request, "home.html", context)

