import random
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers 
from travelblog.articles.models import Category, City, Country, Article
from travelblog.frontend.models import HomePage

ARTICLES = [
    "A-Week-in-France",
    "Jumping-around-Japan",
    "Touring-the-truffle-side-of-Italy",
    "Loving-Slovenia",
    "Things-to-aviod-when-traveling",
    "Best-Travel-Credit-Cards",
    "Hostel-hopping-in-Europe",
    "Taxi-Ride-interviews",
    "DIY-Travel-hacks!",
    "Best-spot-in-Iceland",
    "Hygge,-cozy-cozy-wow!",
    "Coping-and-hanging-in-Denmark",
    "Iceland-more-like-niceland",
    "Fjord-Jumping-in-Norway",
    "I-fell-out-of-an-airplane-no-clickbait",
    "Monthly-recap-of-my-travels",
    "One-week-in-London",
    "24-hours-in-the-Fashion-Capital",
    "How-to-book-cheap-flights",
    "Give-East-Europe-a-chance!",
    "Why-I-think-you-should-always-journal-on-a-trip",
]
CATEGORIES = [
    "City-Guides",
    "Food",
    "Travel-Tips",
    "Interview",
    "Recap",
    "Travel-Story",
    "Reviews",
    "Lodging",
    "Fun-stories",
    "Live-Laugh-Love",
    "Photo-Dump",
]

class Provider(faker.providers.BaseProvider):
    def travelblog_categories(self):
        return self.random_element(CATEGORIES)

    def travelblog_articles(self):
        return self.random_element(ARTICLES)
      
class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(["en_US"])
        fake.add_provider(Provider)
        
        for _ in range(8):
            d = fake.unique.travelblog_categories()
            Category.objects.create(name=d, slug=d)
        
        check_categories = Category.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Categories: {check_categories}"))

        for _ in range(2000):
            c = fake.text(max_nb_chars=15)
            d = fake.text(max_nb_chars=15)
            rid = _
            City.objects.create(name=c, rank=rid)
            Country.objects.create(name=d, rank=rid)

        check_city = City.objects.all().count()
        check_country = Country.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Cities: {check_city}"))
        self.stdout.write(self.style.SUCCESS(f"Number of Countries: {check_country}"))

        for _ in range(2000):
            t = fake.travelblog_articles()
            b = fake.text(max_nb_chars=100)
            cid = random.randint(1,2000)
            did = random.randint(1,2000)
            catid = random.randint(1,8)
            rid = _
            hid = random.randint(1,5)
            Article.objects.create(
                title=t,
                slug=t,
                body=b,
                country=Country.objects.get(id=cid),
                city=City.objects.get(id=did),
                category = Category.objects.get(id=catid),
                rank=rid,
                is_visible=True,
                featured_home=True,
                homepage=HomePage.objects.get(id=hid),
            )
           
        check_articles = Article.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Articles: {check_articles}"))




    
