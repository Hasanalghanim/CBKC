from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

class Fighter(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    weight_class = models.CharField(max_length=100, blank=True, null=True)  
    record = models.CharField(max_length=50, default="0-0")
    gym = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)


    image = models.ImageField(upload_to="fighters/", default="fighters/SILHOUETTE.jpg")
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(300, 300)],
        format="PNG",
        options={"quality": 80, "background": (0, 0, 0, 0)}
    )
    image_medium = ImageSpecField(
        source="image",
        processors=[ResizeToFit(600, 600)],
        format="PNG",
        options={"quality": 85}
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name} {self.last_name or ''}")
            slug = base_slug
            counter = 1
            while Fighter.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        if self.nickname:
            return f"{self.first_name} {self.last_name or ''} ({self.nickname})"
        return f"{self.first_name} {self.last_name or ''}"
    
    @property
    def jsonld_type(self):
        return "Person"

    # ----- Meta/SEO methods -----



    def get_meta_title(self):
        display_name = f"{self.first_name} {self.last_name or ''}".strip()
        
        if self.nickname:
            display_name += f' "{self.nickname}"'
        return f"{display_name} | Fighter | Canadian Bare Knuckle Championship"

    def get_meta_description(self):

        display_name = f"{self.first_name} {self.last_name or ''}".strip()
        if self.nickname:
            display_name += f' "{self.nickname}"'
        desc_parts = [display_name]
        if self.weight_class:
            desc_parts.append(f"is a {self.weight_class} fighter")
        if self.gym:
            desc_parts.append(f"training out of {self.gym}")
        desc_parts.append("under Canadian Bare Knuckle Championship.")
        return " ".join(desc_parts)

    def get_meta_keywords(self):

        keywords = ['Bare Knuckle Canada', 'CBKC Fighter']
        keywords.append(f"{self.first_name} {self.last_name or ''}")
        if self.nickname:
            keywords.append(self.nickname)
        if self.weight_class:
            keywords.append(self.weight_class)
        if self.gym:
            keywords.append(self.gym)
        return keywords

    def get_meta_image(self):

        if self.image:
            return self.image.url
        return '/static/images/default-banner.jpg'