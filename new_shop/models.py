from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Модель категорий"""
    name = models.CharField("Название категории", max_length=100)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    class MPTTMeta:
        order_insertion_by = ['name']


class Product(models.Model):
    """Модель товара"""
    title = models.CharField("Название товара", max_length=100)
    text = models.TextField('Описание товара')
    picture = models.ImageField("Картинка", upload_to="images/", blank=True)
    price = models.DecimalField("Цена", max_digits=9, decimal_places=2, default=0)
    sail = models.DecimalField('Скидка', max_digits=9, decimal_places=2, default=0)
    article = models.IntegerField("артикул", default=0)
    date = models.DateTimeField("дата", auto_now_add=True)
    category = TreeForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Brand(models.Model):
    """Модель брендов"""
    name = models.CharField("Название бренда", max_length=100)
    country = models.CharField("Страна", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Comment(models.Model):
    """Отзывы о товаре"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Текст", max_length=1000)
    new = models.ForeignKey(Product, on_delete=models.CASCADE)
    chek = models.IntegerField("Лайки", default=0)
    like_chek = models.ManyToManyField(User, related_name="like_user")

    def __str__(self):
        return "{}".format(self.new)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class CardItem(models.Model):
    """Карточка товара для корзины"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField("Сумма", max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return "{}".format(self.product.title)

    class Meta:
        verbose_name = 'Карточка товара для корзины'
        verbose_name_plural = 'Карточки товаров для корзины'


class Card(models.Model):
    """Корзина"""
    item = models.ManyToManyField(CardItem, blank=True)
    card_total = models.DecimalField("Общая сумма", max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return "{}".format(self.id)

    def delete_to_card(self, slug):
        card = self
        product = Product.objects.get(id=slug)
        for card_item in card.item.all():
            if card_item.product == product:
                card.item.remove(card_item)
                card.save()

    def add_to_card(self, slug):
        card = self
        product = Product.objects.get(id=slug)
        new_item = CardItem.objects.create(product=product, item_total=product.price)
        if new_item not in card.item.all():
            card.item.add(new_item)
            card.save()

    class Meta:
        verbose_name = 'id козины'
        verbose_name_plural = 'id корзин'


class Zacaz(models.Model):
    """Заказ """
    STATUS = (
        ('1', "В обработке"),
        ('2', "Доставка"),
        ('3', "Готово"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField('статус заказа', choices=STATUS, max_length=10, default='1')
    items = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class Profile(models.Model):
    name = models.CharField('ФИО', max_length=300)
    phone = models.IntegerField(default=0)
    address = models.CharField("адрес", max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
