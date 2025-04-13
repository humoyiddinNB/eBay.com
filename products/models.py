from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=100000000, decimal_places=2)
    address= models.CharField(max_length=300)
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=17)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name_plural = 'ModelNames'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image', )


class Comment(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

