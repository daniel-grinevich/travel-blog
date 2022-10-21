import pytest
from travelblog.frontend.models import HomePage

@pytest.fixture
def homepage_with_multiple_styles(db):
    homepage = HomePage.objects.bulk_create([
        HomePage(
            id=1,
            header='default',
            subheader='default',
            style='H',
            rank=0,
        ),
        HomePage(
            id=2,
            header='default',
            subheader='default',
            style='F',
            rank=1,
        ),
        HomePage(
            id=3,
            header='default',
            subheader='default',
            style='C',
            rank=2,
        ),
        HomePage(
            id=4,
            header='default',
            subheader='default',
            style='R',
            rank=3,
        ),
        HomePage(
            id=5,
            header='default',
            subheader='default',
            style='S',
            rank=4,
        ),
    ])
    return homepage


