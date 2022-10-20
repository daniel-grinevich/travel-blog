from travelblog.articles.models import Category

"""
Arrange - setup db
Act - GET data
Assert - Test
"""

def test_create_category(single_category):
    new_category = single_category
    get_category = Category.objects.all().first()
    assert new_category.id == get_category.id 

def test_category_with_child(category_with_child):
    new_sub_category = category_with_child
    get_category = Category.objects.all().first()
    
    assert get_category.children.first().id == new_sub_category.id
    assert get_category.children.first().name == new_sub_category.name