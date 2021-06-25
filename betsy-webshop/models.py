from enum import unique
from operator import index
from peewee import (
    CharField, 
    Check, 
    DecimalField, 
    ForeignKeyField, 
    IntegerField, 
    Model, 
    SqliteDatabase, 
    DateField,
    TextField)
from playhouse.sqlite_ext import SqliteExtDatabase

from datetime import datetime

db = SqliteExtDatabase('betsy-data.db', pragmas=(
    ('foreign_keys', 1), ('journal_mode', 'wall')))

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    first_name = CharField(index=True, max_length=30)
    last_name = CharField(max_length=100)
    address = CharField(max_length=200)
    city = CharField(max_length=40)
    country = CharField(max_length=50)

class Product(BaseModel):
    product_name = CharField(max_length=50)
    description = TextField(null=True)
    price_per_unit = DecimalField(
        constraints=[Check('price_per_unit >= 0')],
        decimal_places=2,
        auto_round=True,
        null=True,
        default=0,
        max_digits=10
    )
    amount_in_stock = IntegerField(default=1)
    product_owner = ForeignKeyField(User, backref='products')

Product.add_index(Product.product_name, Product.description)

class Tag(BaseModel):
    name = CharField(unique=True, max_length=30)

class ProductTag(BaseModel):
    product = ForeignKeyField(Product, index=True, backref='tags')
    tag = ForeignKeyField(Tag, index=True, backref='products')

class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='transactions', index=True)
    product_bought = ForeignKeyField(Product, index=True)
    amount = IntegerField()
    transaction_date = DateField(formats='%Y=%m-%d %H:%M', default=datetime.utcnow())

def create_tables():
    with db:
        db.create_tables([User, Product, Tag, ProductTag, Transaction])