from django.shortcuts import render
from django.utils import timezone
from fightCards.models import Event  
from articles.models import Article



def home(request):
    now = timezone.now().date()

    
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')[:3]
    featured_articles = Article.objects.filter(
        is_featured=True).order_by('-published_date')[:4]


    # Prefetch related fight cards and matches with fighters
    # This reduces DB queries and improves efficiency
    upcoming_events = upcoming_events.prefetch_related(
        'fight_card__matches__fighter_red',
        'fight_card__matches__fighter_blue'
    )

    context = {
        "upcoming_events": upcoming_events,
        "featured_articles":featured_articles,
        "seo_object": upcoming_events.first() 
    }

    return render(request, "home.html", context)

