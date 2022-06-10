from django.db import models # django에서 제공하는 models를 사용

class Product(models.Model):
    class Meta: # 모델의 정보
        db_table = "product" # db 테이블명 설정

    name = models.CharField(max_length=20, null=False)
    category = models.ManyToManyField('Category')
    image = models.CharField(max_length=256, null=False)
    desc = models.CharField(max_length=256, null=False)
    price = models.IntegerField()
    count = models.IntegerField()

class Category(models.Model):
    class Meta: # 모델의 정보
        db_table = "category" # db 테이블명 설정
    category = models.CharField(max_length=20)

class ProductOrder(models.Model):
    class Meta: # 모델의 정보
        db_table = "product_order" # db 테이블명 설정
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    order_count = models.IntegerField()

class UserOrder(models.Model):
    class Meta: # 모델의 정보
        db_table = "user_order" # db 테이블명 설정
    adress = models.CharField(max_length=256, null=False)
    order_time = models.DateTimeField(auto_now_add=True)
    order_products = models.ManyToManyField('ProductOrder')
    order_price = models.IntegerField()
    discount = models.IntegerField()
    payment = models.IntegerField()
    paymented = models.BooleanField(default=False)