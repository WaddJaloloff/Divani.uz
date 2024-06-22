from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.post.title}"

class Buyurtma(models.Model):
    ism = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    manzil = models.TextField()
    umumiy_narx = models.DecimalField(max_digits=10, decimal_places=2)
    mahsulotlar = models.TextField()  # Mahsulotlar maydoni

    def __str__(self):
        return f"Buyurtma - {self.ism}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)  # Default qiymat
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)

    def __str__(self):
        return self.name