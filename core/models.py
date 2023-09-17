from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _

from core.utils.slug_title import generate_slug


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=255)
    content = RichTextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='product', null=True, blank = True)
    shipping_time = models.IntegerField(default=1)
    weight = models.FloatField(default=1)
    color = models.ForeignKey('Colors', on_delete=models.CASCADE, related_name='%(class)s_product', default=None)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='%(class)s_product', default=None)
    free_pickup = models.BooleanField(default=False)
    heart = models.IntegerField(default=0)
    retweet = models.IntegerField(default=0)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, related_name='product')
    slug = models.SlugField(unique=True, null=True, blank=True)


    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(Product, self).save(*args, **kwargs)

    
class Blog(BaseModel):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='blog', null=True, blank = True)
    comment = models.IntegerField(default=0)
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE, related_name='blog')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)
    

class ProductCategory(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='department_image', null=True, blank=True)
    slug = models.SlugField(unique=True)


    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(ProductCategory, self).save(*args, **kwargs)
    

class BlogCategory(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = _('Blog Category')
        verbose_name_plural = _('Blog Categories')
    

class Banner(BaseModel):
    img = models.ImageField(upload_to='blog', null=True, blank = True)


class Settings(BaseModel):
    address = models.TextField()
    phone = models.CharField(max_length=255)
    e_mail = models.CharField(max_length=255)

    def __str__(self):
        return self.address


    class Meta:
        verbose_name= _('Settings')
        verbose_name_plural = _('Settings')


class Discount_Product(BaseModel):
    name = models.CharField(max_length=255)
    content = RichTextField()
    price = models.FloatField(default=0)
    discount_persentage = models.IntegerField()
    weight = models.FloatField(default=1)
    shipping_time = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product', null=True, blank = True)
    heart = models.IntegerField(default=0)
    retweet = models.IntegerField(default=0)
    category = models.ForeignKey('Discount_category', on_delete=models.CASCADE, related_name='product')
    color = models.ForeignKey('Colors', on_delete=models.CASCADE, related_name='%(class)s_product')
    size = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='%(class)s_product')
    slug = models.SlugField(unique=True)

    
    class Meta:
        verbose_name = _('Discount Product')
        verbose_name_plural = _('Discount_Products')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(Discount_Product, self).save(*args, **kwargs)


class Discount_category(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='discount_images', null=True, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _('Discount Category')
        verbose_name_plural = _('Discount Categories')


class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class Colors(BaseModel):
    title = models.CharField(max_length=255)


    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

        
    def __str__(self):
        return self.title
    


class Size(BaseModel):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Size')
        verbose_name_plural = _('Size')

    def __str__(self):
        return self.title
