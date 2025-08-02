import json
import os
from flask import session, flash


basedir = os.path.abspath(os.path.dirname(__file__))

project_root = os.path.dirname(basedir)

USER_DATA_PATH = os.path.join(project_root, 'data', 'users.json')

def get_users():
    try:
        with open(USER_DATA_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def put_user(new_user_data):
    all_users = get_users()
    all_users.update(new_user_data)
    data_directory = os.path.dirname(USER_DATA_PATH)
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    with open(USER_DATA_PATH, "w") as file:
        json.dump(all_users, file, indent=4)

def flash_overwrite(message, category='message'):
    """Flashes a message and clears any existing ones."""
    # This line clears the list of flashed messages
    session.pop('_flashes', None)
    # This line adds the new message
    flash(message, category)