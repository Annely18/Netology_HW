import sqlalchemy
from sqlalchemy.orm import sessionmaker
from HW_DB_6_models import Publisher, Book, Shop, Stock, Sale, create_tables


DSN = ""
engine = sqlalchemy.create_engine(DSN)

# Задание 2
# Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.
#
# Напишите Python скрипт, который:
# - Подключается к БД любого типа на ваш выбор (например, к PostgreSQL).
# - Импортирует необходимые модели данных.
# - Выводит издателя (publisher), имя или идентификатор которого принимается через input().

if __name__ == '__main__':
    create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# СОЗДАНИЕ ОБЪЕКТОВ
pub1 = Publisher(name='Эксмо')
pub2 = Publisher(name='АСТ')
session.add_all([pub1, pub2])
session.commit()

book1 = Book(title='Хижина', publisher=pub1)
book2 = Book(title='Скотный двор', publisher=pub2)
session.add_all([book1, book2])
session.commit()

sh1 = Shop(name='Буквоед')
sh2 = Shop(name='Дом книги')
sh3 = Shop(name='Лабиринт')
session.add_all([sh1, sh2, sh3])
session.commit()

st1 = Stock(book=book1, shop=sh1, count=204)
st2 = Stock(book=book1, shop=sh2, count=54)
st3 = Stock(book=book1, shop=sh3, count=105)
st4 = Stock(book=book2, shop=sh3, count=15)
session.add_all([st1, st2, st3, st4])
session.commit()

sale1 = Sale(price=1000, date_sale='2022-09-22', stock=st1, count=72)
session.add(sale1)
session.commit()

# ============

pub_name = input('Название издательства: ')
pub_id = input('Идентификатор издательства: ')



def get_shop_by_publisher(publisher_name=None, publisher_id=None):
    if publisher_id is not None and publisher_name is None:
        for c in session.query(Shop.name).join(Stock.shop).join(Stock.book).join(Book.publisher).filter(Publisher.id == int(publisher_id)):
            print(c)
    elif publisher_name is not None and publisher_id is None:
        for c in session.query(Shop.name).join(Stock.shop).join(Stock.book).join(Book.publisher).filter(Publisher.name == publisher_name):
            print(c)
    elif publisher_name is not None and publisher_id is not None:
        for c in session.query(Shop.name).join(Stock.shop).join(Stock.book).join(Book.publisher).filter(Publisher.name == publisher_name, Publisher.id == int(publisher_id)):
            print(c)

if __name__ == '__main__':
    #get_shop_by_publisher(publisher_name=pub_name)
    get_shop_by_publisher(publisher_id=pub_id)
    #get_shop_by_publisher(publisher_id=pub_id, publisher_name=pub_name)

session.close()
