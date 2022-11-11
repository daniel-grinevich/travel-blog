from django.db import models

class HomePage(models.Model):
    id = models.BigAutoField(primary_key=True)
    header = models.CharField(
        max_length=150,
        null=False,
        unique=False,
        verbose_name ='section header',
        help_text ='format: required, max characters:100'
    )
    subheader = models.CharField(
        max_length=150,
        null=False,
        unique=False,
        verbose_name ='section header',
        help_text ='format: required, max characters:100'
    )
    STYLE_CHOICES = (
        ('H', 'Hero'),
        ('F', 'Featured'),
        ('C', 'Cities'),
        ('R', 'Recent'),
        ('S', 'Scroll'),
    )
    style = models.CharField(max_length=1, choices=STYLE_CHOICES)
    rank = models.IntegerField(
        default=0,
        null=False,
        unique=False,
        blank=False,
        verbose_name='ranking order of homepage',
        help_text='format: required, higher rank has higher priority'
    )
    class Meta: 
        ordering = ('-rank', 'header', 'id')
    
    def __str__(self):
        return self.header

    def viewable_articles(self):
        return self.article_set.all()

    def get_first_featured_image(self):
        return self.article_set.all()

class NavLink(models.Model):
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
    homepage = models.ForeignKey(
        HomePage,
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
        return self.header