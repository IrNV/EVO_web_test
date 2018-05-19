from app import app
from products.blueprint import products


app.register_blueprint(products, url_prefix='/products')

if __name__ == '__main__':
    app.run()
