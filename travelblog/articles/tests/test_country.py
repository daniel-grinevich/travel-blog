from travelblog.articles.models import Country


def test_country_created(single_country):
    new_country = single_country
    get_country = Country.objects.all().first()
    assert new_country.id == get_country.id
  
