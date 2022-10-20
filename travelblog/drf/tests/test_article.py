from urllib import response
import pytest 


def test_get_article_by_category(api_client, single_article_with_category):
    article = single_article_with_category
    endpoint = f'/api/articles/category/{article.category}/'
    response = api_client().get(endpoint)
    expected_json = [
        {
            'title': article.title,
            'slug': article.slug,
        }
    ]

    assert response.status_code == 200

def test_get_all_articles(api_client, single_article_with_category):
    article = single_article_with_category
    endpoint = f'/api/articles/all/'
    response = api_client().get(endpoint)
    expected_json = [
        {
            'title': article.title,
            'slug': article.slug,
        }
    ]
    assert response.status_code == 200
    assert response.data == expected_json
    
