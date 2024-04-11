from django.urls import path
from .views import *
from .booceezviews import *

urlpatterns = [

# categorymaster
    path('categorymaster/', CategoryMasterViews.as_view(), name='categorymaster'),
    path('categorymaster/<int:category_id>/', CategoryMasterViews.as_view(), name='categorymaster'),


    # subcategorymaster
    path('subcategorymaster/', SubCategoryMasterViews.as_view(),name='subcategorymaster'),
    path('categorymaster/<int:category_id>/subcategorymaster/', SubCategoryMasterViews.as_view(),name='subcategorymaster'),
    path('categorymaster/<int:category_id>/subcategorymaster/<int:subcategory_id>/', SubCategoryMasterViews.as_view(),name='subcategorymaster'),

    # productmaster
    path('productmaster/', ProductMasterViews.as_view(),name='productmaster'),
    path('categorymaster/<int:category_id>/subcategorymaster/<int:subcategory_id>/productmaster/', ProductMasterViews.as_view(),name='productmaster'),
    path('categorymaster/<int:category_id>/subcategorymaster/<int:subcategory_id>/productmaster/<int:product_id>/', ProductMasterViews.as_view(), name='productmaster'),

    # image
    path('categorymaster/<int:category_id>/subcategorymaster/<int:subcategory_id>/productmaster/<int:product_id>/image/', ProductImageMasterViews.as_view(),name='image'),
    path('categorymaster/<int:category_id>/subcategorymaster/<int:subcategory_id>/productmaster/<int:product_id>/image/<int:image_id>/', ProductImageMasterViews.as_view(), name='image'),

    # review
    path('categorymaster/<int:category_id>/subcategorymaster/<int:subcategory_id>/productmaster/<int:product_id>/review/', ReviewProductMasterViews.as_view(),name='review'),
    path('categorymaster/<int:category_id>/subcategorymaster/<int:subcategory_id>/productmaster/<int:product_id>/review/<int:reviews_id>/', ReviewProductMasterViews.as_view(), name='review'),



    # booceez urls
    path('tblcostrevenue/', Tbl_Cost_RevenueViews.as_view(), name='tblcostrevenue'),
    path('tblcostrevenue/<int:id>/', Tbl_Cost_RevenueViews.as_view(), name='tblcostrevenue'),
    
    path('tax/', Tbl_Tax_MViews.as_view(), name='tax'),
    path('tax/<int:id>/', Tbl_Tax_MViews.as_view(), name='tax'),
    
    path('ownershiptransfer/', Tbl_Organization_Ownership_Transfer_Views.as_view(), name='ownershiptransfer'),
    path('ownershiptransfer/<int:id>/', Tbl_Organization_Ownership_Transfer_Views.as_view(), name='ownershiptransfer'),
    
    path('purchasesubscription/', Tbl_Organization_Ownership_Transfer_Views.as_view(), name='purchasesubscription'),
    path('purchasesubscription/<int:id>/', Tbl_Organization_Ownership_Transfer_Views.as_view(), name='purchasesubscription'),

]
