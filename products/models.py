from app import db


# Модели телевизора и холодильника будут отдельными классами, т. к.
# в реальности они имеют разные параметры не смотря на то, что в наше задаче
# можно было бы хранить их в одной таблице добавив колонку "тип продукта"
class TV(db.Model):
    """
    Модель телевизора
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    click_count = db.Column(db.Integer)

    def __init__(self, tv_name):
        self.name = tv_name
        self.click_count = 0

    def __repr__(self):
        return self.name


class Fridge(db.Model):
    """
    Модель холодильника
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    click_count = db.Column(db.Integer)

    def __init__(self, fridge_name):
        self.name = fridge_name
        self.click_count = 0

    def __repr__(self):
        return self.name