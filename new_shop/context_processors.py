from new_shop.models import Category
from pay.models import Wallet


def category(request):
    cat = Category.objects.all()
    return {'category': cat, }


def wallet(request):
    if request.user.is_active:
        balance = Wallet.objects.get(user=request.user)
        return {'balance': balance}
    else:
        return {"balance": 0}

