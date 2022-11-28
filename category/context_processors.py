from .models import Category

# make sure to add this in settings.py
# and it will be template wide available now

def menu_links(request):
    """CP to get links"""
    links = Category.objects.all()
    return dict(links=links)