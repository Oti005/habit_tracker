from flask import Blueprint, request, jsoninfy
from werkzeug.security import generate_password_hash, check_password_hash
from flsk_jwt_extended import create_access_token
from models import db, User

