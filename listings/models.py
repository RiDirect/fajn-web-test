from django.db import models

# Create your models here.




class Main_Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name

def img_path_sub_category(instance, filename):
    return f"{instance.main_category}/{instance.name}/{filename}"


class Sub_Category(models.Model):
    name = models.CharField(max_length=200)
    main_category = models.ForeignKey(Main_Category,blank = True,null =True,related_name='mistnost',on_delete=models.PROTECT)
    description = models.TextField(max_length=500)
    img = models.ImageField(upload_to=img_path_sub_category, null=False, blank=False)
    img_alt = models.CharField(max_length=200)
    def __str__(self):
        return self.name
def img_path_sub_sub_category(instance, filename):
    return f"{instance.main_category}/{instance.sub_category}/{instance.name}/{filename}"


class Sub_sub_Category(models.Model):
    main_category = models.ForeignKey(Main_Category,blank = True,null =True,related_name='sub_category',on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    sub_category = models.ForeignKey(Sub_Category,blank=True,related_name='subcategory',on_delete=models.PROTECT)
    description = models.TextField(max_length=300)
    img = models.ImageField(upload_to=img_path_sub_sub_category, null=False, blank=False)
    img_alt = models.CharField(max_length=200)
    def __str__(self):
        return self.name
def img_path(instance, filename):
    return f"{instance.main_category}/{instance.category}/{instance.sub_category}/{filename}"
class Brand(models.Model):
    brand_id=models.IntegerField()
    name = models.CharField(max_length=200)

class Produkt(models.Model):
    ean = models.ForeignKey(Brand,blank = True,null =True,related_name='brand',on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    main_category = models.ForeignKey(Main_Category,blank = True,null =True,related_name='mistnost',on_delete=models.PROTECT)
    category = models.ForeignKey(Sub_Category,blank = True,null =True,related_name='subcategory',on_delete=models.PROTECT)
    sub_category = models.ForeignKey(Sub_sub_Category,blank = True,null =True,related_name='subcategory',on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8,decimal_places = 1)
    short_description= models.TextField(max_length=600)
    long_description = models.TextField(max_length=600)
    primary_img = models.ImageField(upload_to=img_path, null=False, blank=False)
    primary_alt = models.CharField(max_length=200)
    img1= models.ImageField(upload_to=img_path, null=True, blank=True)
    img1_alt=models.CharField(max_length=200,null=True, blank=True)
    img2= models.ImageField(upload_to=img_path, null=True, blank=True)
    img2_alt=models.CharField(max_length=200,null=True, blank=True)
    img3= models.ImageField(upload_to=img_path, null=True, blank=True)
    img3_alt=models.CharField(max_length=200,null=True, blank=True)
    img4= models.ImageField(upload_to=img_path, null=True, blank=True)
    img4_alt=models.CharField(max_length=200,null=True, blank=True)
    stock = models.IntegerField()
    brand = models.ForeignKey(Brand,blank = True,null =True,related_name='brand',on_delete=models.PROTECT)
    eta = models.IntegerField()
    def __str__(self):
        return self.name

def img_path_varianta(instance, filename):
    return f"{instance.main_category}/{instance.category}/{instance.sub_category}/{instance.product_name}/{instance.varianta_img}"
def img_path_barva(instance, filename):
    return f"{instance.main_category}/{instance.category}/{instance.sub_category}/{instance.product_name}/{instance.barva_img}"

class Variants(models.Model):
    eanv=models.ForeignKey(Produkt,blank = True,null =True,related_name='brand',on_delete=models.PROTECT)
    product_name = models.ForeignKey(Produkt,blank = True,null =True,related_name='brand',on_delete=models.PROTECT)
    rozmery_sirka = models.IntegerField()
    rozmery_delka = models.IntegerField()
    varianta_img = models.ImageField(upload_to=img_path_varianta, null=True, blank=True)
    barva = models.CharField(max_length=200)
    barva_img = models.ImageField(upload_to=img_path_barva, null=True, blank=True)
