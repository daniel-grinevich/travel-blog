# Generated by Django 4.1.1 on 2022-10-20 18:01

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='format: required, max characters:100', max_length=150, verbose_name='article title')),
                ('slug', models.SlugField(help_text='format: required, derived from article title', max_length=150, verbose_name='article safe URL')),
                ('body', tinymce.models.HTMLField()),
                ('rank', models.IntegerField(default=0, help_text='format: required, higher rank has higher priority', verbose_name='ranking order of articles')),
                ('is_visible', models.BooleanField(default=True, help_text='format: required, default=True, True = Visible False = Not visible', verbose_name='article visible')),
                ('featured_home', models.BooleanField(default=False, help_text='format: required, default=False, True = Visible False = Not visible', verbose_name='article visible on home page')),
                ('featured_image', models.ImageField(blank=True, default='images/default.png', help_text='format: not required, but model should have image or video', null=True, upload_to='images/', verbose_name='Article Feature Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='created timestamp')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='format: Y-m-d H:M:S', verbose_name='updated timestamp')),
            ],
            options={
                'ordering': ('-rank', 'title', 'id'),
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='format: required, max characters:30', max_length=30, verbose_name='city name')),
                ('rank', models.IntegerField(default=0, help_text='format: required, higher rank has higher priority', verbose_name='ranking order of countries')),
            ],
            options={
                'ordering': ('id', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='format: required, max characters:30', max_length=30, verbose_name='country name')),
                ('rank', models.IntegerField(default=0, help_text='format: required, higher rank has higher priority', verbose_name='ranking order of countries')),
            ],
            options={
                'ordering': ('id', 'name'),
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('header', models.CharField(help_text='format: required, max characters:100', max_length=150, verbose_name='section header')),
                ('subheader', models.CharField(help_text='format: required, max characters:100', max_length=150, verbose_name='section header')),
                ('style', models.CharField(choices=[('H', 'Hero'), ('F', 'Featured'), ('C', 'Cities'), ('R', 'Recent'), ('S', 'Scroll')], max_length=1)),
                ('rank', models.IntegerField(default=0, help_text='format: required, higher rank has higher priority', verbose_name='ranking order of homepage')),
            ],
            options={
                'ordering': ('-rank', 'header', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('header', models.CharField(help_text='format: required, max characters:100', max_length=150, verbose_name='section header')),
                ('body', tinymce.models.HTMLField(blank=True, help_text='format: NOT required', null=True, verbose_name='section body')),
                ('rank', models.IntegerField(default=0, help_text='format: required, higher rank has higher priority', verbose_name='ranking order of sections')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
            options={
                'ordering': ('-rank', 'header', 'id'),
            },
        ),
        migrations.CreateModel(
            name='NavLink',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(help_text='format: required, derived from article title', max_length=150, verbose_name='article safe URL')),
                ('text', models.CharField(help_text='format: required, max characters:100', max_length=150, verbose_name='link text')),
                ('rank', models.IntegerField(default=0, help_text='format: required, higher rank has higher priority', verbose_name='ranking order of articles')),
                ('homepage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.homepage')),
            ],
            options={
                'ordering': ('-rank', 'text', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image_file', models.ImageField(blank=True, default='images/default.png', help_text='format: not required, but model should have image or video', null=True, upload_to='images/', verbose_name='Article, Section, Homepage, Images')),
                ('video_file', models.FileField(blank=True, help_text='format: not required, but model should have image or video', null=True, upload_to='videos/', verbose_name='video file for homepage')),
                ('alt_text', models.CharField(help_text='format: required, max-255', max_length=255, verbose_name='alternative text')),
                ('caption', models.CharField(help_text='format: required, max-255', max_length=255, verbose_name='caption')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='format: Y-m-d H:M:S', verbose_name='media created time')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='format: Y-m-d H:M:S', verbose_name='media updated time')),
                ('homepage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='articles.homepage')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='articles.section')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(help_text='format: required, derived from article title', max_length=150, verbose_name='article safe URL')),
                ('text', models.CharField(help_text='format: required, max characters:100', max_length=150, verbose_name='link text')),
                ('rank', models.IntegerField(default=0, help_text='format: required, higher rank has higher priority', verbose_name='ranking order of articles')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.section')),
            ],
            options={
                'ordering': ('-rank', 'text', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='format: required, max-100', max_length=100, verbose_name='category name')),
                ('slug', models.SlugField(help_text='format: required, letters, numbers, underscore, or hyphens', max_length=150, verbose_name='category safe URL')),
                ('is_active', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='format: not required', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='articles.category', verbose_name='parent of category')),
            ],
            options={
                'verbose_name': 'article category',
                'verbose_name_plural': 'article categories',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=mptt.fields.TreeManyToManyField(to='articles.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='city', to='articles.city'),
        ),
        migrations.AddField(
            model_name='article',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='country', to='articles.country'),
        ),
        migrations.AddField(
            model_name='article',
            name='homepage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='articles.homepage'),
        ),
    ]
