from travelblog.articles.models import City


def test_cuty_created(single_city):
    new_city = single_city
    get_city = City.objects.all().first()
    assert new_city.id == get_city.id
  
