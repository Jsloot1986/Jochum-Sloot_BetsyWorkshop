from models import *
from peewee import *

db = SqliteDatabase('betsy-data.db')

def make_records():
    if User.select().where(User.first_name == 'Jochum' and User.last_name == 'Sloot'):
        None
    else:
        User.create(
            first_name='Jochum',
            last_name='Sloot',
            address='Elandsgracht 120',
            city='Amsterdam',
            country='Nederland'
        )
    if User.select().where(User.first_name == 'Mirjam' and User.last_name == 'Sloot'):
        None
    else:
        User.create(
            first_name='Mirjam',
            last_name='Sloot',
            address='Nieuwstraat 1',
            city='Oldemarkt',
            country='Nederland'
        )
    if User.select().where(User.first_name == 'Sabrina' and User.last_name == 'Sloot'):
        None
    else:
        User.create(
            first_name='Sabrina',
            last_name='Sloot',
            address='Antwerpenstraat 33',
            city='Antwerpen',
            country='België'
        )
    if User.select().where(User.first_name == 'David' and User.last_name == 'Hello'):
        None
    else:
        User.create(
            first_name='David',
            last_name='Hello',
            address='Insulindeweg 222',
            city='Amsterdam',
            country='Nederland'
        )
    if Product.select().where(Product.product_name == 'Sweater'):
        None
    else:
        Product.create(
            product_name = 'Sweater',
            description = 'Sweater, warm and made from polyeaster',
            price_per_unit=49.999,
            amount_in_stock=10,
            product_owner= User.id == 1
        )
    if Product.select().where(Product.product_name == 'T-shirt'):
        None
    else:
        Product.create(
            product_name = 'T-shirt',
            description = 'T-shirt, with Garfield',
            price_per_unit=9.999,
            amount_in_stock=10,
            product_owner= User.id == 1
        )
    if Product.select().where(Product.product_name == 'Trouser'):
        None
    else:
        Product.create(
            product_name = 'Trouser',
            description = 'Trouser, Levi Jeans',
            price_per_unit=39.999,
            amount_in_stock=20,
            product_owner= User.id == 1
        )
    if Product.select().where(Product.product_name == 'Monopoly'):
        None
    else:
        Product.create(
            product_name = 'Monopoly',
            description = 'Monopoly the New York edition',
            price_per_unit=29.999,
            amount_in_stock=10,
            product_owner= User.id == 2
        )
    if Product.select().where(Product.product_name == 'Cluedo'):
        None
    else:
        Product.create(
            product_name = 'Cluedo',
            description = 'Cluedo the extended version',
            price_per_unit=25.999,
            amount_in_stock=15,
            product_owner= User.id == 2
        )
    if Product.select().where(Product.product_name == 'Apples'):
        None
    else:
        Product.create(
            product_name = 'Apples',
            description = 'Apples, nice and sweet from Spain',
            price_per_unit=2.995,
            amount_in_stock=15,
            product_owner= User.id == 3
        )
    if Product.select().where(Product.product_name == 'Grapes'):
        None
    else:
        Product.create(
            product_name = 'Grapes',
            description = 'Grapes, tasty from France',
            price_per_unit=1.999,
            amount_in_stock=25,
            product_owner= User.id == 3
        )

    if Tag.select().where(Tag.name == 'Clothes'):
        None
    else:
        Tag.create(name='Clothes')
    if Tag.select().where(Tag.name == 'Winter'):
        None
    else:
        Tag.create(name='Winter')
    if Tag.select().where(Tag.name == 'Domestic'):
        None
    else:
        Tag.create(name='Domestic')
    if Tag.select().where(Tag.name == 'Games'):
        None
    else:
        Tag.create(name='Games')
    if Tag.select().where(Tag.name == 'Family'):
        None
    else:
        Tag.create(name='Family')
    if Tag.select().where(Tag.name == 'Fruit'):
        None
    else:
        Tag.create(name='Fruit')
    if Tag.select().where(Tag.name == 'Healthy'):
        None
    else:
        Tag.create(name='Healthy')
    if Tag.select().where(Tag.name == 'Books'):
        None
    else:
        Tag.create(name='Books')
    if Tag.select().where(Tag.name == 'Thriller'):
        None
    else:
        Tag.create(name='Thriller')

    if ProductTag.select.where(ProductTag.product == 'Sweater' and ProductTag.tag == 'Clothes'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Sweater'),
            tag = (Tag.name == 'Clothes')
        )
    if ProductTag.select.where(ProductTag.product == 'Sweater' and ProductTag.tag == 'Winter'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Sweater'),
            tag = (Tag.name == 'Winter')
        )
    if ProductTag.select.where(ProductTag.product == 'Trouser' and ProductTag.tag == 'Clothes'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Trouser'),
            tag = (Tag.name == 'Clothes')
        )
    if ProductTag.select.where(ProductTag.product == 'Monopoly' and ProductTag.tag == 'Games'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Monopoly'),
            tag = (Tag.name == 'Games')
        )
    if ProductTag.select.where(ProductTag.product == 'Monopoly' and ProductTag.tag == 'Family'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Monopoly'),
            tag = (Tag.name == 'Family')
        )
    if ProductTag.select.where(ProductTag.product == 'Cluedo' and ProductTag.tag == 'Games'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Cluedo'),
            tag = (Tag.name == 'Games')
        )
    if ProductTag.select.where(ProductTag.product == 'Apples' and ProductTag.tag == 'Fruit'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Apples'),
            tag = (Tag.name == 'Fruit')
        )
    if ProductTag.select.where(ProductTag.product == 'Apples' and ProductTag.tag == 'Sweet'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Apples'),
            tag = (Tag.name == 'Sweet')
        )
    if ProductTag.select.where(ProductTag.product == 'Grapes' and ProductTag.tag == 'Fruit'):
        None
    else:
        ProductTag.create(
            product = (Product.product_name == 'Grapes'),
            tag = (Tag.name == 'Fruit')
        )

    