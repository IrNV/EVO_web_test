from flask import Blueprint, render_template, request
from models import TV, Fridge
from app import db


products = Blueprint('products ', __name__, template_folder='templates', static_folder='static')


def sort(data, requset):
    # Сортируем по параметру выбранном пользователем
    if request.form["sort"] == "click_amount":
        data.sort(key=lambda fridge: fridge.click_count, reverse=True)
    else:
        data.sort(key=lambda fridge: fridge.name)


@products.route("/tvs", methods=['GET', 'POST'])
def tvs_page():
    all_tvs = TV.query.all()

    if "sort" in request.form:
        sort(all_tvs, request)

    return render_template("products.html", products=all_tvs, type="tvs")


@products.route("/fridges", methods=['GET', 'POST'])
def fridges_page():
    all_fridges = Fridge.query.all()

    if "sort" in request.form:
        sort(all_fridges, request)

    return render_template("products.html", products=all_fridges, type="fridges")


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

    return render_template("products.html", products=all_products, type=data_split[TYPE])

