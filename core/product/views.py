from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from rest_framework import generics

# Create your views here.

class CategoryMasterViews(APIView):

    def post(self, request, format=None):
        try:
            data = request.data
            category_name = data.get("category_name") 
            description = data.get("description") 
            
            if CategoryMaster.objects.filter(category_name=category_name).exists():
                return Response("This Category name is already in database")
            else:
                CategoryMaster.objects.create(category_name=category_name, description=description)
                return Response("Category create successfuly")
        except:
            return Response("Something went wrong!")
        
    def get(self, request, format=None, category_id=None):
        try:
            if category_id is None:  
                category_master_obj = CategoryMaster.objects.all()
                serializers_obj=CategoryMasterSerializer(category_master_obj,many=True).data
                return Response(serializers_obj)
            else:
                category_master_obj = CategoryMaster.objects.get(id=category_id)
                serializers_obj=CategoryMasterSerializer(category_master_obj).data
                return Response(serializers_obj)
        except:
            return Response("Something went wrong!")
        
    def delete(self, request, category_id=None):
        try:
            category_master_obj=CategoryMaster.objects.get(id=category_id)
            category_master_obj.delete()
            return Response("Category data deleted successfuly")
        except:
            return Response("Something went wrong!")
        
    def put(self, request, category_id=None):
        try:
            data = request.data
            category_name=data.get("category_name")
            description=data.get("description")

            category_master_obj = CategoryMaster.objects.get(id=category_id)
            if category_name:
                category_master_obj.category_name=category_name  
            if description:
                category_master_obj.description=description
            category_master_obj.save()
            return Response("Category update successfully")        
        except:
            return Response("Something went wrong!")

class SubCategoryMasterViews(APIView):
    
    def post(self, request):
        try:
            data = request.data
            subcategory_name = data.get("subcategory_name")
            description = data.get("description")
            category_id = data.get("category_id")

            if CategoryMaster.objects.filter(id=category_id).exists():
                category_master_obj = CategoryMaster.objects.get(id=category_id)
                            
                if SubCategoryMaster.objects.filter(category_id=category_id, subcategory_name=subcategory_name).exists():
                    return Response("Sub-Category already added for this category")
                else:
                    SubCategoryMaster.objects.create(category_id=category_master_obj.id, subcategory_name=subcategory_name, description=description)
                    return Response("Sub-Category created successfully")
            else:
                return Response("Category id is not match")            
        except:
            return Response("Something went wrong!")
    
    def get(self, request, category_id=None, subcategory_id=None):
        try:
            if category_id is not None:
                category_master_obj = CategoryMaster.objects.get(id=category_id)

                if subcategory_id is not None:
                    subcategory_master_obj = SubCategoryMaster.objects.get(id=subcategory_id, category_id=category_master_obj)
                    serializers_obj = SubCategoryMasterSerializer(subcategory_master_obj).data
                    return Response(serializers_obj)
                else:
                    subcategory_master_obj = SubCategoryMaster.objects.filter(category_id=category_master_obj)
                    serializers_obj = SubCategoryMasterSerializer(subcategory_master_obj, many=True).data
                    return Response(serializers_obj)
            else:
                return Response("Category ID is required")
        except:
            return Response("Something went wrong!")
        
    def delete(self, request, category_id=None, subcategory_id=id):
        try:
            subcategory_master_obj = SubCategoryMaster.objects.get(id=subcategory_id)
            subcategory_master_obj.delete()
            return Response("Sub-Category Data Deleted Successfully")
        except:
            return Response("Something went wrong!")
    
    def put(self, request, category_id=None, subcategory_id=None):
        try:
            if subcategory_id is not None:
                data = request.data
                subcategory_name = data.get("subcategory_name")
                description = data.get("description")

                category_master_obj = CategoryMaster.objects.get(id=category_id)
                subcategory_master_obj = SubCategoryMaster.objects.get(id=subcategory_id, category_id=category_master_obj)

                if subcategory_name:
                    subcategory_master_obj.subcategory_name = subcategory_name

                if description:
                    subcategory_master_obj.description = description

                subcategory_master_obj.save()
                return Response("Sub-Category updated successfully")
            else:
                return Response("Sub-category ID is required")
        except:
            return Response("Something went wrong:")

class ProductMasterViews(APIView):

    def post(self, request, category_id=None, subcategory_id=None, product_id=None):
        try:
           
            data = request.data
            subcategory_id = data.get("subcategory_id")
            product_name = data.get("product_name")
            description = data.get("description")
            price = data.get("price")
            stock_quantity = data.get("stock_quantity")
            main_image = request.FILES.get("main_image")

            if SubCategoryMaster.objects.filter(id=subcategory_id).exists():
                subcategory_master_obj = SubCategoryMaster.objects.get(id=subcategory_id)

                if ProductMaster.objects.filter(subcategory_id=subcategory_id, product_name=product_name).exists():
                    return Response("Product Is Already In This Category And Sub-Category ")
                else:
                    ProductMaster.objects.create(
                        subcategory_id=subcategory_master_obj.id,
                        product_name=product_name,
                        description=description,
                        price=price,
                        stock_quantity=stock_quantity,
                        main_image=main_image
                    )
                    return Response("Product Created Successfully")
            else:
                return Response("Sub-category ID is required")
        except:
            return Response("Something went wrong!")

    def get(self, request, category_id=None, subcategory_id=None, product_id=None):
        try:

                if subcategory_id is not None:
                    subcategory_master_obj = SubCategoryMaster.objects.get(id=subcategory_id)

                    if product_id is not None:
                        product_master_obj = ProductMaster.objects.get(id=product_id, subcategory_id=subcategory_master_obj)
                        serializers_obj = ProductMasterSerializer(product_master_obj).data
                        return Response(serializers_obj)
                    else:
                        product_master_obj = ProductMaster.objects.filter(subcategory_id=subcategory_master_obj)
                        serializers_obj = ProductMasterSerializer(product_master_obj, many=True).data
                        return Response(serializers_obj)
                else:
                    return Response("Sub-Category ID is required")
            
        except:
            return Response("Something went wrong!")

    def delete(self, request, category_id=None, subcategory_id=None, product_id=None):
        try:
            if product_id is not None:
                product_master_obj = ProductMaster.objects.get(id=product_id)
                product_master_obj.delete()
                return Response("Product deleted successfully")
            else:
                return Response("Product ID is required")
        except:
            return Response("Something went wrong!")

    def put(self, request, category_id=None, subcategory_id=None, product_id=None):
        try:
            if product_id is not None:
                data = request.data
                product_name = data.get("product_name")
                description = data.get("description")
                price = data.get("price")
                stock_quantity = data.get("stock_quantity")
                main_image = request.FILES.get("main_image")

                subcategory_master_obj = SubCategoryMaster.objects.get(id=subcategory_id)
                product_master_obj = ProductMaster.objects.get(id=product_id, subcategory_id=subcategory_master_obj)

                if product_name:
                    product_master_obj.product_name=product_name
                if description:
                    product_master_obj.description=description
                if price:
                    product_master_obj.price=price
                if stock_quantity:
                    product_master_obj.stock_quantity=stock_quantity
                if main_image:
                    product_master_obj.main_image=main_image

                product_master_obj.save()
                return Response("Product updated successfully")
            else:
                return Response("Product ID is required")
        except:
            return Response("Something went wrong!")
        
class ProductImageMasterViews(APIView):

    def post(self, request, category_id=None, subcategory_id=None, product_id=None):
        try:
            data = request.data
            product_id = data.get("product_id")
            product_image = request.FILES.get("product_image")
            
            if product_id is None:
                return Response("Product ID is required")
            if ProductMaster.objects.filter(id=product_id).exists():
                product_master_obj = ProductMaster.objects.get(id=product_id)

                if ProductImageMaster.objects.filter(product_id=product_id, product_image=product_image).exists():
                    return Response("Product Image is already in this product")
                else:
                    ProductImageMaster.objects.create(product_id=product_master_obj.id, product_image=product_image)
                    return Response("Product Image added successfully")
            else:
                return Response("Product ID is required")
        except:
            return Response("Something went wrong!")

    def get(self, request, category_id=None, subcategory_id=None, product_id=None, image_id=None):
        try:
            if product_id is not None:
                product_master_obj = ProductMaster.objects.get(id=product_id)

                if image_id is not None:
                    image_master_obj = ProductImageMaster.objects.get(id=image_id, product_id=product_master_obj)
                    serializers_obj = ProductImageMasterSerializer(image_master_obj).data
                    return Response(serializers_obj)
                else:
                    image_master_obj = ProductImageMaster.objects.filter(product_id=product_master_obj)
                    serializers_obj = ProductImageMasterSerializer(image_master_obj, many=True).data
                    return Response(serializers_obj)
        except:
            return Response("Something went wrong!")
        
    def delete(self, request, category_id=None, subcategory_id=None, product_id=None, image_id=None):
        try:
            if image_id is not None:
                image_master_obj = ProductImageMaster.objects.get(id=image_id)
                image_master_obj.delete()
                return Response("Product Image deleted successfully")
            else:
                return Response("Product Image ID is required")
        except:
            return Response("Something went wrong!")
    
    def put(self, request, category_id=None, subcategory_id=None, product_id=None, image_id=None):
        try:
            if image_id is not None:
                data = request.data
                product_image = request.FILES.get("product_image")

                product_master_obj = ProductMaster.objects.get(id=product_id)
                image_master_obj = ProductImageMaster.objects.get(id=image_id, product_id=product_master_obj)

                if product_image:
                    image_master_obj.product_image=product_image
                
                image_master_obj.save()
                return Response("Product Image updated successfully")
            else:
                return Response("Product Image ID is required")
        except:
            return Response("Something went wrong!")     

class ReviewProductMasterViews(APIView):

    def post(self, request, category_id=None, subcategory_id=None, product_id=None):
        try:
             if product_id is not None:
                data = request.data
                product_id = data.get("product_id")
                rating = data.get("rating")
                comment = data.get("comment")

                if ProductMaster.objects.filter(id=product_id).exists():
                    product_master_obj = ProductMaster.objects.get(id=product_id)

                    if ReviewProductMaster.objects.filter(product_id=product_id, rating=rating, comment=comment).exists():
                        return Response("This Review Is Already In That Product")
                    else:
                        ReviewProductMaster.objects.create(product_id=product_master_obj.id, rating=rating, comment=comment)
                        return Response("Review added successfully")
                else:
                    return Response("Review not found")
             else:
                 return Response("Product image ID is required")
        except:
            return Response("Something went wrong!")
        
    def get(self, request,category_id=None, subcategory_id=None, product_id=None ,reviews_id=None):
        try:
             if product_id is not None:
                product_master_obj = ProductMaster.objects.get(id=product_id)

                if reviews_id is not None:
                    reviews_master_obj = ReviewProductMaster.objects.get(id=reviews_id, product_id=product_master_obj)
                    serializers_obj = ReviewProductMasterSerializer(reviews_master_obj).data
                    return Response(serializers_obj)
                else:
                    reviews_master_obj =ReviewProductMaster.objects.filter(product_id=product_master_obj)
                    serializers_obj = ReviewProductMasterSerializer(reviews_master_obj, many=True).data
                    return Response(serializers_obj)

             else:
                 return Response("Product image ID is required")
        except:
            return Response("Something went wrong!")
        
    def delete(self, request,category_id=None, subcategory_id=None, product_id=None, reviews_id=None):
        try:
            if reviews_id is not None:
                reviews_master_obj = ReviewProductMaster.objects.get(id=reviews_id)
                reviews_master_obj.delete()
                return Response("Review deleted successfully")
            else:
                return Response("Review ID is required")
        except:
            return Response("Something went wrong!")
        
    def put(self, request,category_id=None, subcategory_id=None, product_id=None, reviews_id=None):
        try:
            if reviews_id is not None:
                data = request.data
                rating = data.get("rating")
                comment = data.get("comment")

                product_master_obj = ProductMaster.objects.get(id=product_id)
                reviews_master_obj = ReviewProductMaster.objects.get(id=reviews_id, product_id=product_master_obj)

                if rating:
                    reviews_master_obj.rating=rating
                if comment:
                    reviews_master_obj.comment=comment

                reviews_master_obj.save()
                return Response("Review Updated Successfully")
            else:
                return Response("Review ID is required")
        except:
            return Response("Something Went Wrong!")
        
