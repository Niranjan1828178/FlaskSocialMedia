# run.py (CORRECTED)

from Myapp import create_app

# Create the app instance using the factory
app = create_app()

if __name__ == "__main__":
    # Use the app instance to run the development server
    app.run(debug=True)