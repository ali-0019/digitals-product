from rest_framework import serializers

from .models import Product, File, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['title', 'description', 'avatar']
        
class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    
    class Meta:
        model  = File
        fields = ['id','title', 'file','file_type']
        
    def get_file_type(self, object):
        return object.get_file_type_display()
        
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    Categories = CategorySerializer(many = True)
    files = FileSerializer(many= True)
    
    class Meta:
        model  = Product
        fields = ['id','title', 'description', 'avatar', 'Categories', 'files','url']