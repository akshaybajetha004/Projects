from blog import create_app
from authlib.integrations.flask_client import OAuth
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
