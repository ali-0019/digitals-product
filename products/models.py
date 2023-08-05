from django.db import models
from django.utils.translation import gettext_lazy as _#for translate to molty language

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self',verbose_name=_('parent'),blank=True, null=True,on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='categoties/')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'),auto_now_add=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Categories')
        verbose_name_plural = _('Categories')
    
class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='products/')
    is_enable = models.BooleanField(_('is_enable'),default=True)
    Categories = models.ManyToManyField('Category',verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'),auto_now_add=True)
    
    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')

    

class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('prosuct'), on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'),auto_now_add=True)
    is_enable = models.BooleanField(_('is_enable'),default=True)
    
    
    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
