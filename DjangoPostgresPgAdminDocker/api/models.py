from django.db import models

# Create your models here.

class Base(models.Model):

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:

        abstract = True

class Category(Base):

    name = models.CharField(max_length=60)

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ['id']

    def __str__(self):

        return self.name.title()

class Product(Base):

    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:

        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        unique_together = ['name']
        ordering = ['id']

    def __str__(self):

        return self.name.title()


