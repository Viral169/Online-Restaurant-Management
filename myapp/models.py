from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(null=False,default=False)
    mobile = models.CharField(max_length=10, null=True)
    address = models.TextField(blank=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = 'Profile'


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    @staticmethod
    def get_all_category():
        return Category.objects.all()

    def __str__(self):
        return self.category_name


class Food(models.Model):
    food_name = models.CharField(max_length=150)
    food_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    dec = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="static/img", default="")

    @staticmethod
    def get_all_Food():
        return Food.objects.all()

    @staticmethod
    def get_all_Food_by_category_id(category_id):
        if category_id:
            return Food.objects.filter(food_category=category_id)
        else:
            return Food.get_all_Food()

    def __str__(self):
        return self.food_name


class Cart(models.Model):
    email = models.EmailField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default="1")
    price = models.IntegerField(default="0")


STATUS_CHOICE=(
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)
class OrderDetail(models.Model):
    user=models.CharField(max_length=50,default=True)
    food_name=models.CharField(max_length=250)
    image=models.ImageField(null=True,blank=True)
    qty=models.PositiveIntegerField(default=1)
    price=models.IntegerField()
    address = models.TextField(blank=True)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,default='Pending',choices=STATUS_CHOICE)

class Delivery_boy_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=False, default=False)
    mobile = models.CharField(max_length=10, null=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = 'Delivery Boy Profile'


PAYMENT_STATUS = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted')
)

class Delivery_order(models.Model):
    user=models.CharField(max_length=50,default=True)
    food_name=models.CharField(max_length=250)
    address = models.TextField(blank=True)
    qty=models.PositiveIntegerField(default=1)
    price=models.IntegerField()
    status=models.ForeignKey(OrderDetail,on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(auto_now_add=True,null=True)
    payment_status = models.CharField(max_length=50, default='Pending', choices=PAYMENT_STATUS)
    delivery_status=models.CharField(max_length=50,default='Pending',choices=STATUS_CHOICE)

    def __str__(self):
        return self.user


