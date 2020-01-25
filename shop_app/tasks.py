from shop_parse.celery_app import app
from .models import Product
import json


@app.task
def save_products(items):
    for item in items:
        Product.objects.create(
            p_url=item['url'],
            price=item['price'],
            category=item['category'],
            title=item['title'],
            sizes=item['sizes'],
            images=item['images'],
            description=item['description']
        )
    return {'status': True}
