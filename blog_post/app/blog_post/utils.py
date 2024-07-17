import structlog
from flask_jwt_extended import get_jwt_identity

from db_utils import db
from deepdiff import DeepDiff
from deepdiff.helper import TREE_VIEW
from models import BlogPost

logger = structlog.getLogger()


def upsert_blog_post(data) -> dict:
    title = data.get("title", None)
    content = data.get("content", None)
    blog_post_id = data.get("id", None)
    # blog_post_id exist => update record
    if blog_post_id:
        logger.info(f"Update blog_post with id: {blog_post_id}")
        blog_post = BlogPost.query.filter_by(id=blog_post_id).first()
        if not blog_post:
            raise Exception(f"Not found blog_post with id: {blog_post_id}")

        before_change = blog_post.as_dict()

        # Update fields
        blog_post.title = title
        blog_post.content = content

        db.session.add(blog_post)
        db.session.commit()

        # Using deepdiff to identify changed fields
        ddiff = DeepDiff(
            before_change,
            data,
            view=TREE_VIEW
        )

        before_change = {}
        after_change = {}

        values_changed = list(ddiff.get('values_changed', []))
        for v in values_changed:
            path = v.path(output_format='list')[0]
            before_change[path] = v.t1
            after_change[path] = v.t2

        dictionary_item_added = list(ddiff.get('dictionary_item_added', []))
        for v in dictionary_item_added:
            path = v.path(output_format='list')[0]
            after_change[path] = v.t2

        logger.info(f"Finish update with information before_change: {before_change} / after_change: {after_change}")

    # blog_post_id does not exist => create record
    else:
        user = get_jwt_identity()
        blog_post = BlogPost(title=title, content=content, user_email=user)
        db.session.add(blog_post)
        db.session.commit()
        logger.info(f"Create blog_post with id: {blog_post.id}")
    return blog_post.as_dict()
