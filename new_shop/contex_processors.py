from new_shop.models import Category
from pay.models import Wallet


def category(request):
    cat = Category.objects.all()
    balance = Wallet.objects.filter(name=request.user)
    return {'category': cat, 'balance': balance}
