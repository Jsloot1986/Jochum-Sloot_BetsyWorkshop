__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from peewee import fn
from making_records import make_records



def search(term) -> list[Product.product_name]:
    search_list = []
    search_product = Product.select().where(fn.Upper(Product.product_name).contains(fn.Upper(term)))
    for product in search_product:
        search_list.append(product.product_name)
    return search_list


def list_user_products(user_id) -> list[User.products]:
    user_product_list = []
    user_products = Product.select().join(User).where(Product.product_owner == user_id)
    for product in user_products:
        user_product_list.append(product.product_name)
    return user_product_list



def list_products_per_tag(tag_id) -> list[Tag.name]:
    tag_list =[]
    tags = (Product.select().join(ProductTag).where(Tag.id == tag_id))
    for tag in tags:
        tag_list.append(tag.name)
    return tag_list


def add_product_to_catalog(user_id, product) -> None:
    user = User.get_by_id(user_id)
    Product.create(name=product, product_owner=user)


def update_stock(product_id, new_quantity) -> None:
    product = Product.get_by_id(product_id)
    product.amount_in_stock = new_quantity
    product.save()
    

def purchase_product(product_id, buyer_id, quantity) -> None:
    product = Product.get_by_id(product_id)
    if product.amount_in_stock < quantity:
        raise ValueError("Amount not available in stock")
    Transaction.create(buyer=buyer_id, product_bought=product_id, amount=quantity)
    product.amount_in_stock -= quantity
    product.save()


def remove_product(product_id) -> None:
    Product.delete_by_id(product_id)

create_tables()
make_records()

"""
Functie calls for checking the functies.
First creating the tables and make the records.
"""

print("First we search for the product Sweater")
print(search('Sweater'))

print("Now we want to see all the products with user_id 1")
print(list_user_products(1))

print("Now we want to see al the tags with id 1")
print(list_products_per_tag(1))

print("Now we gonna add a product to the catalog")
print(add_product_to_catalog(2, 'Uno'))

print("Now we gonna update the stock from a product")
print(update_stock(1, 100))

print("Now we gonna purchase a product")
print(purchase_product(1, 4, 10))

print("And now we gonna remove a product")
print(remove_product(6))