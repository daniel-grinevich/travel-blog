from django.db import models
from tinymce.models import HTMLField

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        null=False,
        unique=False,
        verbose_name='country name',
        help_text='format: required, max characters:30'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id','name')

class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        null=False,
        unique=False,
        verbose_name='city name',
        help_text='format: required, max characters:30'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id','name')


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        max_length=150,
        null=False,
        unique=False,
        verbose_name ='article title',
        help_text ='format: required, max characters:100'
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name='article safe URL',
        help_text='format: required, derived from article title'
    )
    body = HTMLField(
        null=False,
        unique=False,
        blank=False,
    )
    country = models.ForeignKey(
        Country,
        related_name='country',
        on_delete=models.PROTECT,
    )
    city = models.ForeignKey(
        City,
        related_name='city',
        on_delete=models.PROTECT,
    )
    rank = models.IntegerField(
        default=0,
        null=False,
        unique=False,
        blank=False,
        verbose_name='ranking order of articles',
        help_text='format: required, higher rank has higher priority'
    )
    is_visible = models.BooleanField(
        default=True,
        null=False,
        unique=False,
        blank=False,
        verbose_name='article visible',
        help_text='format: required, default=True, True = Visible False = Not visible'
    )
    featured_home = models.BooleanField(
        default=False,
        null=False,
        unique=False,
        blank=False,
        verbose_name='article visible on home page',
        help_text='format: required, default=False, True = Visible False = Not visible'
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

   



# Create your models here.
