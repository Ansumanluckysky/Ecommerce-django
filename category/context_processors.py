
from category.models import Category

# This menu link we have defined as context_processors this will be available across all the templates.

def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)