from django.db import models

# Create your models here.

class CategoryMaster(models.Model):
    category_name= models.CharField(max_length=250, blank=True,null=True,default=True)
    description= models.TextField(blank=True,null=True,default=True)
   
    def __str__(self):
        return self.category_name
 
class SubCategoryMaster(models.Model):
    category = models.ForeignKey(to=CategoryMaster, on_delete=models.CASCADE)
    subcategory_name= models.CharField(max_length=250, blank=True,null=True,default=True)
    description= models.TextField(blank=True,null=True,default=True)
 
    def __str__(self):
        return self.subcategory_name
 
class ProductMaster(models.Model):
    subcategory = models.ForeignKey(to=SubCategoryMaster, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=250, blank=True,null=True,default=True)
    description= models.TextField(blank=True,null=True,default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    main_image = models.ImageField(upload_to='Product Main Image',blank=True, null=True)
 
    def __str__(self):
        return self.product_name
 
class ProductImageMaster(models.Model):
    product = models.ForeignKey(to=ProductMaster,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='Product Image',blank=True,null=True)
   
class ReviewProductMaster(models.Model):
    product = models.ForeignKey(to=ProductMaster,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True,null=True,default=True)
    created_at = models.DateTimeField(auto_now_add=True)




# bookeez model
class Tbl_Cost_Revenue(models.Model):
    type_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True, default=False)

class Tbl_Tax_M(models.Model):
    # user_auth_id = models.ForeignKey(to=Tbl_User_Auth , on_delete=models.CASCADE)
    tax_name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=255, unique=True)
    tax_code = models.CharField(max_length=255,unique=True)
    tax_rate = models.CharField(max_length=255)
 
    DisplayList = ['id','tax_name','tax_id','tax_code','tax_rate']
    searchable_fields = ['id']
    class Meta:
        db_table ='masterapp_tbl_tax_m'

class Tbl_Organization_Ownership_Transfer(models.Model):
    # want_to_transfer_tbl_user_auth_id = models.ForeignKey(to=UserAuth, related_name='want_to_transfer', on_delete=models.CASCADE)
    # to_whom_to_transfer_tbl_user_auth_id = models.ForeignKey(to=UserAuth, related_name='to_whom_to_transfer', on_delete=models.CASCADE)
    # tbl_organization_m_id_fk = models.ForeignKey(to=Tbl_Organization_M, on_delete=models.CASCADE)
    transfer_code = models.CharField(max_length=10)
    transfer_code_verify = models.BooleanField(default=False)
    current_status = models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Rejected'), (3, 'Cancelled')])
 
class Tbl_User_Purchase_Subscription(models.Model):
    # tbl_user_auth_id= models.ForeignKey(to = UserAuth, on_delete=models.CASCADE)
    # tbl_subscription_s_id = models.ForeignKey(to = Tbl_Subscription_M, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    card_holder_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    card_last_four_digit = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

# class Tbl_User_Subscription_Cycle(BaseCon... by Ashish Sonewane
# Ashish Sonewane
# 6:46 pm
    
# class Tbl_User_Subscription_Cycle(models.Model):
#     tbl_user_purchase_subscription = models.OneToOneField(to = Tbl_User_Purchase_Subscription, on_delete=models.CASCADE)
#     next_billing_date = models.DateTimeField()
 
# class Tbl_User_Team_Member(models.Model):
#     # tbl_user_auth_id_fk = models.ForeignKey(to=UserAuth, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email_address = models.EmailField()
#     date_invitation = models.DateTimeField()
#     invitation_status = models.IntegerField(choices=[(0, 'Invited'), (1, 'Accepted'), (2, 'Cancelled')])
# has context menu