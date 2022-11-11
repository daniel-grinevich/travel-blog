from django.db import models
from tinymce.models import HTMLField
from travelblog.frontend.models import HomePage
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

class Category(models.Model):
    """
    Inventory Category table implimented with MPTT
    """
    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name='category name',
        help_text='format: required, max-100',
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name='category safe URL',
        help_text='format: required, letters, numbers, underscore, or hyphens',
    )
    is_active = models.BooleanField(
        default=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "article category"
        verbose_name_plural = "article categories"

    def __str__(self):
        return self.name

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        null=False,
        unique=False,
        verbose_name='country name',
        help_text='format: required, max characters:30'
    )
    rank = models.IntegerField(
        default=0,
        null=False,
        unique=False,
        blank=False,
        verbose_name='ranking order of countries',
        help_text='format: required, higher rank has higher priority'
    )

    class Meta:
        ordering = ('id','name')

    def __str__(self):
        return self.name

class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        null=False,
        unique=False,
        verbose_name='city name',
        help_text='format: required, max characters:30'
    )
    rank = models.IntegerField(
        default=0,
        null=False,
        unique=False,
        blank=False,
        verbose_name='ranking order of countries',
        help_text='format: required, higher rank has higher priority'
    )

    class Meta:
        ordering = ('id','name')

    def __str__(self):
        return self.name

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
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.PROTECT,
    )
    rank = models.IntegerField(
        default=0,
        null=False,
        unique=False,
        blank=False,
        verbose_name='rank',
        help_text='format: required, higher rank has higher priority'
    )
    is_visible = models.BooleanField(
        default=True,
        null=False,
        unique=False,
        blank=False,
        verbose_name='Article visible',
        help_text='format: required, default=True, True = Visible False = Not visible'
    )
    featured_home = models.BooleanField(
        default=False,
        null=False,
        unique=False,
        blank=False,
        verbose_name='Homepage visible',
        help_text='format: required, default=False, True = Visible False = Not visible'
    )
    homepage = models.ForeignKey(
        HomePage,
        related_name='article',
        null=True,
        on_delete=models.PROTECT,
    )
    featured_image = models.ImageField(
        unique=False,
        null=True,
        blank=True,
        upload_to='images/',
        default='images/default.png',
        verbose_name='Article Feature Image',
        help_text='format: 1200 x 16000, not required',
    )
    showcase_image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        upload_to='images/',
        default='images/default.png',
        verbose_name='Article Showcase Image',
        help_text='format: 1440 x 900, required',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="created timestamp",
        help_text="format: Y-m-d H:M:S",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="updated timestamp",
        help_text="format: Y-m-d H:M:S",
    )

    class Meta:
        ordering = ("-rank", "title", "id")

    def __str__(self):
        return self.title

    def viewable_sections(self):
        return self.section_set.all()

class Section(models.Model):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )
    header = models.CharField(
        max_length=150,
        null=False,
        unique=False,
        verbose_name ='section header',
        help_text ='format: required, max characters:100'
    )
    body = HTMLField(
        null=True,
        unique=False,
        blank=True,
        verbose_name ='section body',
        help_text ='format: NOT required'
    )
    rank = models.IntegerField(
        default=0,
        null=False,
        unique=False,
        blank=False,
        verbose_name='ranking order of sections',
        help_text='format: required, higher rank has higher priority'
    )
    class Meta: 
        ordering = ('-rank', 'header', 'id')
    
    def __str__(self):
        return self.header

    def viewable_links(self):
        return self.link_set.all()


class Link(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=False,
        blank=False,
        verbose_name='article safe URL',
        help_text='format: required, derived from article title'
    )
    text = models.CharField(
        max_length=150,
        null=False,
        unique=False,
        verbose_name ='link text',
        help_text ='format: required, max characters:100'
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=True,
    )
    rank = models.IntegerField(
        default=0,
        null=False,
        unique=False,
        blank=False,
        verbose_name='ranking order of articles',
        help_text='format: required, higher rank has higher priority'
    )
    class Meta: 
        ordering = ('-rank', 'text', 'id')

    def __str__(self):
        return self.text

class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_file = models.ImageField(
        unique=False,
        null=True,
        blank=True,
        upload_to='images/',
        default='images/default.png',
        verbose_name='Article, Section, Homepage, Images',
        help_text='format: not required, but model should have image or video',
    )
    video_file= models.FileField(
        unique=False,
        null=True, 
        blank=True,
        upload_to='videos/', 
        verbose_name="video file for homepage",
        help_text='format: not required, but model should have image or video',
    )
    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name="alternative text",
        help_text="format: required, max-255",
    )
    caption = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name="caption",
        help_text="format: required, max-255",
    )
    section = models.ForeignKey(
        Section,
        null=True,
        on_delete=models.PROTECT,
    )
    homepage = models.ForeignKey(
        HomePage,
        null=True,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="media created time",
        help_text="format: Y-m-d H:M:S",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="media updated time",
        help_text="format: Y-m-d H:M:S",
    )