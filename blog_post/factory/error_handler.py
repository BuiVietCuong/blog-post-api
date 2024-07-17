from http import HTTPStatus

import structlog
from flask import jsonify

from marshmallow import ValidationError

log = structlog.get_logger()


def handle_validation_error(e: ValidationError):
    return jsonify({"error": e.messages}), HTTPStatus.BAD_REQUEST


def handle_exception(e):
    return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
