from new_shop.models import Category


# from new_shop.forms import Search


def category(request):
    cat = Category.objects.all()  # filter(rodcat__isnull=True)
    return {'category': cat}
