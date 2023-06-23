from app import app
from posts.bluerpint import posts


app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    app.run()
