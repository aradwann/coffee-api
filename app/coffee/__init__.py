from flask import Blueprint


coffee = Blueprint('coffee', __name__)

# we import coffee views here to avoid circular dependancy issues
from . import views
