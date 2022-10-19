from travelblog.articles.models import Article

def test_insert_single_article_with_sub_category(single_article_with_category):
    new_article = single_article_with_category
    get_article = Article.objects.all().first()
    assert new_article.id == get_article.id
