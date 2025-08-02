# Myapp/__init__.py (CORRECTED)

from flask import Flask

# This will hold our app instance.
app = Flask(__name__) # <--- CREATE THE APP INSTANCE HERE, GLOBALLY WITHIN THE MODULE

def create_app():
    """Construct the core application."""

    # --- Configuration ---
    app.config['SECRET_KEY'] = 'a-very-secret-key-please-change-it'
    # Add other configurations if needed, e.g., database URI

    with app.app_context():
        # --- Import Routes ---
        # Import routes here. They will use the 'app' instance we created above.
        from . import routes

    return app