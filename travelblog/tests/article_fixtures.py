import pytest
from travelblog.articles.models import Category, Article, City, Country

@pytest.fixture
def single_country(db):
    return Country.objects.create(name='default')

@pytest.fixture
def single_city(db):
    return City.objects.create(name='default')

@pytest.fixture
def single_category(db):
    return Category.objects.create(name='default',slug='default')

@pytest.fixture
def category_with_child(db):
    parent = Category.objects.create(name='parent',slug='parent')
    parent.children.create(name='child',slug='child')
    child = parent.children.first()
    return child 

@pytest.fixture()
def single_article_with_category(db, category_with_child,single_city,single_country):
    article = Article.objects.create(
        title='default',
        slug='default',
        body='deault',
        country=single_country,
        city=single_city,
        is_visible=True,
        featured_home=False,
    )
    return article