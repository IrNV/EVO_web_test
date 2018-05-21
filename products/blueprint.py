from flask import Blueprint, render_template, request

from app import db
from products.models import TV, Fridge

products = Blueprint('products', __name__, template_folder='templates', static_folder='static')


def sort(data):
    # Сортируем по параметру выбранном пользователем
    if request.form["sort"] == "click_amount":
        data.sort(key=lambda product: product.click_count, reverse=True)
    else:
        data.sort(key=lambda product: product.name)


@products.route("/tvs", methods=['GET', 'POST'])
def tvs_page():
    all_tvs = TV.query.all()

    # Проверяем есть ли запрос на сортировку с формы
    if "sort" in request.form:
        sort(all_tvs)
    else:
        # Если с формы запрос не отправлен, то сортируем по имени
        all_tvs.sort(key=lambda tv: tv.name)

    return render_template("products.html", products=all_tvs, type="tvs")


@products.route("/fridges", methods=['GET', 'POST'])
def fridges_page():
    all_fridges = Fridge.query.all()

    # Проверяем есть ли запрос на сортировку с формы
    if "sort" in request.form:
        sort(all_fridges)
    else:
        # Если с формы запрос не отправлен, то сортируем по имени
        all_fridges.sort(key=lambda fridges: fridges.name)

    return render_template("products.html", products=all_fridges, type="fridges")


@products.route('/click', methods=['POST'])
def product_click():
    """
    Функция вызываемая, когда AJAX делает запрос, сигнализируя, что был сделан клик
    """
    data = eval(request.data)

    if data['type'] == "fridges":
        product = Fridge.query.filter(Fridge.name == data['name']).first()
        all_products = Fridge.query.all()
    else:
        product = TV.query.filter(TV.name == data['name']).first()
        all_products = TV.query.all()

    product.click_count += 1
    db.session.commit()

    return render_template("products.html", products=all_products, type=data['type'])

