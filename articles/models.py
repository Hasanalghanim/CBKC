from django.db import models

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from fighters.models import Fighter  
from fightCards.models import Event  
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    banner_image = models.ImageField(upload_to='articles/banners/')
    excerpt = models.TextField(max_length=300, blank=True)
    content = RichTextUploadingField()
    author = models.CharField(max_length=255,blank=True)
    fighter = models.ForeignKey(
        Fighter,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles'
    )
    fight_card = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles'
    )


    image_banner = ImageSpecField(
        source="banner_image",
        processors=[ResizeToFill(1920 , 1200)],
        format="PNG",
        options={"quality": 90, "background": (0, 0, 0, 0)}
    )
    image_thumbnail = ImageSpecField(
            source="banner_image",
            processors=[ResizeToFill(280 , 356)],
            format="PNG",
            options={"quality": 90, "background": (0, 0, 0, 0)}
        )

    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)


    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
    

        # ----- Meta/SEO methods -----

    def get_meta_title(self):
        
        meta_title = f"{self.title} | Canadian Bare Knuckle Championship"
        
        if self.fighter:
            fighter_name = f"{self.fighter.first_name} {self.fighter.last_name}"
            meta_title = f"{fighter_name} | {self.title} | Canadian Bare Knuckle Championship"
        return meta_title

    def get_meta_description(self):
        if self.excerpt:
            return self.excerpt
        parts = []
        if self.fighter:
            parts.append(f"Article about {self.fighter.first_name} {self.fighter.last_name}")
        if self.fight_card:
            parts.append(f"covering {self.fight_card.name}")
        parts.append("under Canadian Bare Knuckle Championship.")
        return " ".join(parts)

    def get_meta_keywords(self):
        keywords = ['Bare Knuckle Canada', 'CBKC Article', self.title]
        if self.fighter:
            keywords.append(f"{self.fighter.first_name} {self.fighter.last_name}")
            if self.fighter.nickname:
                keywords.append(self.fighter.nickname)
            if self.fighter.weight_class:
                keywords.append(self.fighter.weight_class)
            if self.fighter.gym:
                keywords.append(self.fighter.gym)
        if self.fight_card:
            keywords.append(self.fight_card.name)
        return keywords

    def get_meta_image(self):
        # Prefer the banner image
        if self.banner_image:
            return self.banner_image.url
        # Or fallback to fighter image
        if self.fighter and self.fighter.image:
            return self.fighter.image.url
        return '/static/images/default-banner.jpg'