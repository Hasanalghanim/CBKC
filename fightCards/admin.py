from django.contrib import admin
from .models import Event, FightCard,Match

# Register your models here.






@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("fight_card", "fighter_red", "fighter_blue", "weight_class", "order", "is_main_event", "is_co_main_event", "is_feature_bout", "winner")
    list_filter = ("fight_card", "weight_class", "is_main_event", "is_co_main_event", "is_feature_bout")
    search_fields = ("fighter_red__name", "fighter_blue__name", "fight_card__event__name")
    ordering = ("order",)






admin.site.register(Event)
admin.site.register(FightCard)


