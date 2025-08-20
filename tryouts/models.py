from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit,ResizeToFill

class TryoutEvent(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=255, blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    banner = models.ImageField(upload_to="tryouts/")

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
    


class TryoutRegistrant(models.Model):
    tryout_event = models.ForeignKey(TryoutEvent, on_delete=models.CASCADE, related_name="registrants")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    # Optional fields for more info
    weight_class = models.CharField(max_length=50, blank=True, null=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)


    image = models.ImageField(upload_to="tryoutRegistrant/", default="fighters/SILHOUETTE.jpg")
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(150, 150)],
        format="PNG",
        options={"quality": 80,"background": (0, 0, 0, 0)}
    )
    image_medium = ImageSpecField(
        source="image",
        processors=[ResizeToFit(600, 600)],
        format="PNG",
        options={"quality": 85}
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.tryout_event.name}"