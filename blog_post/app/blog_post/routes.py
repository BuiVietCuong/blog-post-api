from http import HTTPStatus

import structlog
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from blog_post.app.blog_post import utils
from blog_post.app.blog_post.schemas import BlogPostUpSertSchema
from db_utils import db
from models.blog_post import BlogPost

blog_post_blue_print = Blueprint('blog_post', __name__)

blog_post_upsert_schema = BlogPostUpSertSchema()

logger = structlog.getLogger()

prefix_log = "[Blog Post API]"


@blog_post_blue_print.route("/")
@jwt_required()
def find_all_blog_post():
    logger.info(f"{prefix_log} Find all blog post by author")
    email = get_jwt_identity()
    blog_posts = BlogPost.query.filter_by(user_email=email).all()
    return jsonify([s.as_dict() for s in blog_posts]), HTTPStatus.OK


@blog_post_blue_print.route("/<id>")
@jwt_required()
def find_blog_post_by_id(id):
    logger.info(f"{prefix_log} Find blog post by id: {id}")
    user = get_jwt_identity()
    blog_post = BlogPost.query.filter_by(id=id, user_email=user).first()
    if blog_post:
        return blog_post.as_dict(), HTTPStatus.OK
    else:
        return jsonify({"msg": 'Not Found'}), HTTPStatus.NOT_FOUND


@blog_post_blue_print.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete_blog_post_by_id(id):
    logger.info(f"{prefix_log} Delete blog post by id: {id}")
    user = get_jwt_identity()
    blog_post = BlogPost.query.filter_by(id=id, user_email=user).first()
    if blog_post:
        BlogPost.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify({"msg": 'Deleted'}), HTTPStatus.OK
    else:
        return jsonify({"msg": 'Blog Post does not exist or you are not authorized'}), HTTPStatus.BAD_REQUEST


@blog_post_blue_print.route("/", methods=["POST"])
@jwt_required()
def upsert_blog_post():
    logger.info(f"{prefix_log} Start upsert blog post")
    data = blog_post_upsert_schema.load(request.json)
    blog_post = utils.upsert_blog_post(data)

    return blog_post, HTTPStatus.CREATED
