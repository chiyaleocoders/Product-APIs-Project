from rest_framework import serializers
from .models import *

class CategoryMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMaster
        fields = "__all__"

class SubCategoryMasterSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True, source="category.category_name")
    category_description = serializers.CharField(read_only=True, source="category.description")    
    class Meta:
        model = SubCategoryMaster
        fields = "__all__"

class ProductMasterSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True, source="category.category_name")
    category_description = serializers.CharField(read_only=True, source="category.description")

    subcategory_name = serializers.CharField(read_only=True, source="subcategory.subcategory_name")
    subcategory_description = serializers.CharField(read_only=True, source="subcategory.description") 
    class Meta:
        model = ProductMaster
        fields = "__all__"

class ProductImageMasterSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(read_only=True, source="product.product_name")
    class Meta:
        model = ProductImageMaster
        fields = "__all__"

class ReviewProductMasterSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(read_only=True, source="product.product_name")
    class Meta:
        model = ReviewProductMaster
        fields = "__all__"



# boocees serializers

class Tbl_Cost_RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Cost_Revenue
        fields = "__all__"


class Tbl_Tax_MSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Tax_M
        fields = "__all__"


class Ownership_Transfe_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_Organization_Ownership_Transfer
        fields = "__all__"


class Purchase_Subscription_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tbl_User_Purchase_Subscription
        fields = "__all__"