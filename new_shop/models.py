from django.db import models
from django.contrib.auth.models import User


# написать модель корзины, модель отзывов, выводить в админке, написать вью вывода категорий, подкатегорий и товара,
# добавление товаров в корзину


class Product(models.Model):
    """Модель товара"""
    title = models.CharField("Название товара", max_length=100)
    text = models.TextField('Описание товара')
    picture = models.ImageField("Картинка", upload_to="images/", blank=True)
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2, default=0)
    sail = models.DecimalField('Скидка', max_digits=6, decimal_places=2, default=0)
    article = models.IntegerField("артикул", default=0)

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
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField("Название категории", max_length=100)
    text = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


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
    item = models.ManyToManyField(CardItem)
    card_total = models.DecimalField("Общая сумма", max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = 'id козины'
        verbose_name_plural = 'id корзин'
