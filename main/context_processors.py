from products.models import Category

def for_all_pages(request):
    categories = Category.objects.all()
    return {"categories": categories}