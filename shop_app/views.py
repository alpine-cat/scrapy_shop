from django.views.generic import ListView, DetailView
import redis
from django.http import HttpResponseRedirect
from .models import Product


class ShopView(ListView):
    context_object_name = 'products_list'
    queryset = Product.objects.all()
    template_name = 'shop_app/index.html'
    paginate_by = 30

    def post(self, request, *args, **kwargs):
        send_req = redis.Redis()
        send_req.lpush('net-a-porter:start_urls', 'https://www.net-a-porter.com/ua/en/d/shop/Clothing/Activewear')
        send_req.lpush('net-a-porter:start_urls', 'https://www.net-a-porter.com/ua/en/d/shop/Clothing/Beachwear')
        send_req.lpush('net-a-porter:start_urls', 'https://www.net-a-porter.com/ua/en/d/shop/Clothing/Bridalwear')
        return HttpResponseRedirect('')


