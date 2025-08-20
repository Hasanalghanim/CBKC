from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit,ResizeToFill
from fighters.image_processors import PreserveTransparencyResize

# Fighter
class Fighter(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,blank=True, null=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    weight_class = models.CharField(max_length=100, blank=True, null=True)  # e.g. "Lightweight"
    record = models.CharField(max_length=50, default="0-0")  # W-L or W-L-D
    gym = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    # Profile Image
    image = models.ImageField(upload_to="fighters/", default="fighters/SILHOUETTE.jpg")
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



    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name} {self.first_name}" )
            slug = base_slug
            counter = 1
            while Fighter.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def meta_title(self):
        return f"{self.first_name} {self.last_name} | Fighter | Canadian Bare Knuckle Championship"

    @property
    def meta_description(self):
        return (self.bio[:160] if self.bio else f"{self.first_name} {self.last_name} is a fighter under Canadian Bare Knuckle Championship.")
    
    def __str__(self):
        # Show nickname if exists, otherwise just name
        if self.nickname:
            return f"{self.first_name} {self.last_name} ({self.nickname})"
        return self.name
