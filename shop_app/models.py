from django.db import models


class TagManager(models.Manager):
    pass


class Category(models.Model):
    objects = TagManager()
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'
        ordering = ['parent__name', 'name']

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.parent:
            return f"{self.parent.get_full_name()}/{self.name}"
        else:
            return self.name


class Product(models.Model):
    objects = TagManager()
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.category}) = {self.price}'


class Review(models.Model):
    objects = TagManager()
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    rating = models.IntegerField(default=0)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
