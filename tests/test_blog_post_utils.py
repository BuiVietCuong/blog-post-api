from unittest.mock import patch

from blog_post.app.blog_post import utils

def test_upsert_blog_post():
    data = {
        "id": 1,
        "content": "Content one update",
        "title": "Title one"
    }
    with patch('flask_sqlalchemy._QueryProperty.__get__') as queryMOCK:  # setup
        queryMOCK \
            .return_value.filter_by \
            .return_value.first \
            .return_value = data
    blog_post = utils.upsert_blog_post(data)
    assert blog_post.get("id") == 1


test_upsert_blog_post()