from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from fighters.models import Fighter



class Event(models.Model):
    name = models.CharField(max_length=200)  # "BKFC 70", "House of Gaia Tryouts"
    date = models.DateField()
    location = models.CharField(max_length=255)
    venue = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    banner = models.ImageField(upload_to="events/")
    banner_web = ImageSpecField(
        source="banner",
        processors=[ResizeToFit(1200, 600)],
        format="JPEG",
        options={"quality": 85}
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

    @property
    def meta_title(self):
        return f"{self.name} | Fight Card | Canadian Bare Knuckle Championship"

    @property
    def meta_description(self):
        return f"{self.name} takes place on {self.date}. View the fight card and fighters."



class FightCard(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="fight_card")
    published = models.BooleanField(default=False)  # when ready to go public

    def __str__(self):
        return f"Fight Card - {self.event.name}"


class Match(models.Model):
    fight_card = models.ForeignKey(FightCard, on_delete=models.CASCADE, related_name="matches")
    fighter_red = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="red_corner")
    fighter_blue = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name="blue_corner")
    weight_class = models.CharField(max_length=100)

    # Sorting & Positioning
    order = models.PositiveIntegerField(default=0, help_text="Manually set fight order (1 = first fight)")
    is_main_event = models.BooleanField(default=False)
    is_co_main_event = models.BooleanField(default=False)
    is_feature_bout = models.BooleanField(default=False)

    # Results
    winner = models.ForeignKey(
        Fighter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wins"
    )

    class Meta:
        ordering = ["order"]  # always sorted by the manual order field

    def __str__(self):
        return f"{self.fighter_red} vs {self.fighter_blue} ({self.fight_card.event.name})"
