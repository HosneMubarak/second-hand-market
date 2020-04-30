from django.shortcuts import render
from django.views.generic import TemplateView
from post.models import PostAd, PostCategory


# Create your views here.


def homepage(request):
    mobiles = PostAd.objects.filter(category__post_category__contains='Mobiles')
    Electromics = PostAd.objects.filter(category__post_category__contains='Electromics')
    Property = PostAd.objects.filter(category__post_category__contains='Property')
    sports = PostAd.objects.filter(category__post_category__contains='Sports & Kids')
    homeandliving = PostAd.objects.filter(category__post_category__contains='Home & Living')
    Vehicles = PostAd.objects.filter(category__post_category__contains='Vehicles')
    PetsAndAnumals = PostAd.objects.filter(category__post_category__contains='Pets & Animals')
    healthFashionBeauty = PostAd.objects.filter(category__post_category__contains='Fashion, Health & Beauty')
    return render(request, 'pages/home_page.html',
                  context={
                      'mobiles': mobiles,
                      'Electromics': Electromics,
                      'Property': Property,
                      'sports': sports,
                      'homeandliving': homeandliving,
                      'Vehicles': Vehicles,
                      'PetsAndAnumals': PetsAndAnumals,
                      'healthFashionBeauty': healthFashionBeauty,
                  })
