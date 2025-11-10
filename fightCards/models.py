from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from fighters.models import Fighter
from meta.models import ModelMeta  

class Event(ModelMeta, models.Model): 
    name = models.CharField(max_length=200) 
    date = models.DateField()
    location = models.CharField(max_length=255)
    venue = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    start_time = models.DateTimeField(blank=True, null=True)
    ticket_url = models.CharField(max_length=255,blank=True, null=True)
    playerUrl = models.CharField(max_length=255, blank=True, null=True)

    banner = models.ImageField(upload_to="events/")
    banner_web = ImageSpecField(
        source="banner",
        processors=[ResizeToFit(1200, 600)],
        format="JPEG",
        options={"quality": 85}
    )
    @property
    def jsonld_type(self):
        return "SportsEvent"

    _metadata = {
        'title': 'get_meta_title',
        'description': 'get_meta_description',
        'keywords': 'get_meta_keywords',
        'image': 'get_meta_image',
    }

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_meta_title(self):
        return f"{self.name} | Fight Card | Canadian Bare Knuckle Championship"

    def get_meta_description(self):
        desc = self.description or ""
        return f"{self.name} takes place on {self.date}. {desc[:150]} View the fight card and fighters."

    def get_meta_keywords(self):
        # you can customize or pull keywords dynamically
        return ['Bare Knuckle Canada', self.name, self.location, 'Fight Card', 'CBKC Canada']

    def get_meta_image(self):
        if self.banner:
            return self.banner.url
        return '/static/images/default-banner.jpg'


class FightCard(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="fight_card")
    published = models.BooleanField(default=False) 

    def __str__(self):
        return f"Fight Card - {self.event.name}"


class Match(models.Model):
    fight_card = models.ForeignKey(FightCard, on_delete=models.CASCADE, related_name="matches")
    fighter_red = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="red_corner")
    fighter_blue = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="blue_corner")
    weight_class = models.CharField(max_length=100)

    order = models.PositiveIntegerField(default=0, help_text="Manually set fight order (1 = first fight)")
    is_main_event = models.BooleanField(default=False)
    is_co_main_event = models.BooleanField(default=False)
    is_feature_bout = models.BooleanField(default=False)

    winner = models.ForeignKey(
        Fighter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wins"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.fighter_red} vs {self.fighter_blue} ({self.fight_card.event.name})"
