from flask import Blueprint, jsonify

from app_exceptions import UserInputError
from .models import Service

service_app = Blueprint('service_app', __name__)

