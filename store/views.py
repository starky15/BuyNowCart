from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
# Create your views here.
def store(request, category_slug=None):
    products = Product.objects.all().filter(is_available=True)

    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category ,is_available=True)
        
    context = {
        'products': products,
        'count': len(products)
    }
    
    return render(request, 'store/store.html', context)


def product(request, category_slug=None, product_slug=None):
    # print(product_slug)
    # In the category__slug example:
    # We are accessing the slug field of a Category model. Because in the Product model we have a field "category" which is a ForeignKey to the Category model.
    # So, if you want to access the field of a ForeignKey model, then you use foreignkeymodelfield__fieldname  that is category__slug
    # Little tricky but easy once understood.

    single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
    
    context = {
        'product': single_product,
    }
    print(context)
    return render(request, 'store/product_detail.html', context)