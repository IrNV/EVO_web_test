from flask import Blueprint, render_template
from models import TV, Fridge
from app import db


products = Blueprint('products ', __name__, template_folder='templates', static_folder='static')


@products.route("/tvs")
def tvs_page():
    all_tv = TV.query.all()
    return render_template("products.html", products=all_tv, class_name="tv")


@products.route("/fridges")
def fridges_page():
    all_fridges = Fridge.query.all()
    return render_template("products.html", products=all_fridges, class_name="fridges")


@products.route('/click/<data>')
def product_click(data):
    """
    Функция вызываемая, когжа AJAX делает запрос, сигнализируя, что был сделан клик
    :param data: type=name, принимает тип продукта и его название в виде параметра
    """
    data_split = data.split("=")
    TYPE = 0  # константа типа продукта
    NAME = 1  # константа названия продукта

    if data_split[TYPE] == "fridges":
        product = Fridge.query.filter(Fridge.name == data_split[NAME]).first()
        all_products = Fridge.query.all()
    else:
        product = TV.query.filter(TV.name == data_split[NAME]).first()
        all_products = TV.query.all()

    product.click_count += 1
    db.session.commit()

    return render_template("products.html", products=all_products)
