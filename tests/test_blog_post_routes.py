from unittest import mock


from blog_post import create_app

upsert_blog_post_url = "/api/blog-post/"

@mock.patch("blog_post.app.blog_post.utils.upsert_blog_post")
def test_upsert_blog_post_unauthorized(mock_upsert_blog_post):
    mock_upsert_blog_post.return_value = {
        "id": 1,
        "content": "Content one update",
        "title": "Title one"
    }

    response = create_app().test_client().post(
        upsert_blog_post_url,
    )

    assert response.status_code == 401

test_upsert_blog_post_unauthorized()