from django.shortcuts import render
from .models import *
from product import util
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from rest_framework import generics



class Tbl_Cost_RevenueViews(APIView):
    
    def post(self, request):
        try:
            data = request.data
            type_name = data.get("type_name")
            # status = data.get("status")

            if Tbl_Cost_Revenue.objects.filter(type_name=type_name).exists():
                return Response(util.error(self,"This type_name is already exist"))
            else:
                Tbl_Cost_Revenue.objects.create(type_name=type_name)
                return Response(util.success(self,"Tbl Cost Revenue create successfuly"))
        except:
            return Response(util.success(self,"Something went wrong!"))
        
    def get(self, request, id=None):
        try:
            if id is None:
                tbl_Cost_Revenue_obj = Tbl_Cost_Revenue.objects.all()
                serializers_obj = Tbl_Cost_RevenueSerializer(tbl_Cost_Revenue_obj, many=True).data
                return Response(util.success(self,serializers_obj))
            else:
                tbl_Cost_Revenue_obj = Tbl_Cost_Revenue.objects.get(id=id)
                serializers_obj = Tbl_Cost_RevenueSerializer(tbl_Cost_Revenue_obj).data
                return Response(util.success(self,serializers_obj))
        except:
            return Response(util.success(self,"Something went wrong!"))

    def delete(self, request, id=None):
        try:
            tbl_Cost_Revenue_obj=Tbl_Cost_Revenue.objects.get(id=id)
            tbl_Cost_Revenue_obj.delete()
            return Response(util.success(self,"Tbl Cost Revenue data deleted successfuly"))
        except:
            return Response(util.error(self,"Something went wrong!"))
        
    def put(self, request, id=None):
        try:
            data = request.data
            type_name = data.get("type_name")
            # status = data.get("status")

            tbl_Cost_Revenue_obj = Tbl_Cost_Revenue.objects.get(id=id)
            if type_name:
                tbl_Cost_Revenue_obj.type_name=type_name  

            tbl_Cost_Revenue_obj.save()
            return Response(util.success(self,"Tbl Cost Revenue update successfully"))        
        except:
            return Response(util.error(self,"Something went wrong!"))
        
class Tbl_Tax_MViews(APIView):
    
    def post(self, request):
        try:
            data = request.data
            tax_name = data.get("tax_name")
            tax_id = data.get("tax_id")
            tax_code = data.get("tax_code")
            tax_rate = data.get("tax_rate")

            if Tbl_Tax_M.objects.filter(tax_id=tax_id).exists():
                return Response(util.error(self,"This tax_id is already exist"))
            else:
                Tbl_Tax_M.objects.create(tax_name=tax_name, tax_id=tax_id, tax_code=tax_code, tax_rate=tax_rate)
                return Response(util.success(self,"Tbl Tax create successfuly"))
        except Exception as e:
            return Response(util.error(self,"Something went wrong!"))
        
    def get(self, request, id=None):
        try:
            if id is None:
                tbl_tax_obj = Tbl_Tax_M.objects.all()
                serializers_obj = Tbl_Tax_MSerializer(tbl_tax_obj, many=True).data
                return Response(util.success(self,serializers_obj))
            else:
                tbl_tax_obj = Tbl_Tax_M.objects.get(id=id)
                serializers_obj = Tbl_Tax_MSerializer(tbl_tax_obj).data
                return Response(util.success(self,serializers_obj))
        except:
            return Response(util.error(self,"Something went wrong!"))

    def delete(self, request, id=None):
        try:
            tbl_tax_obj=Tbl_Tax_M.objects.get(id=id)
            tbl_tax_obj.delete()
            return Response(util.success(self,"Tbl Tax data deleted successfuly"))
        except:
            return Response(util.error(self,"Something went wrong!"))
        
    def put(self, request, id=None):
        try:
            data = request.data
            tax_name = data.get("tax_name")
            tax_id = data.get("tax_id")
            tax_code = data.get("tax_code")
            tax_rate = data.get("tax_rate")

            tbl_tax_obj = Tbl_Tax_M.objects.get(id=id)
            if tax_name:
                tbl_tax_obj.tax_name=tax_name  
            if tax_id:
                tbl_tax_obj.tax_id=tax_id  
            if tax_code:
                tbl_tax_obj.tax_code=tax_code  
            if tax_rate:
                tbl_tax_obj.tax_rate=tax_rate  

            tbl_tax_obj.save()
            return Response(util.success(self,"Tbl Tax update successfully"))        
        except:
            return Response(util.error(self,"Something went wrong!"))
        
class Tbl_Organization_Ownership_Transfer_Views(APIView):
    
    def post(self, request):
        try:
            data = request.data
            transfer_code = data.get("transfer_code")
            # transfer_code_verify = data.get("transfer_code_verify")
            current_status = data.get("current_status")

            if Tbl_Organization_Ownership_Transfer.objects.filter(transfer_code=transfer_code).exists():
                return Response(util.error(self,"This Ownership Transfer already exist"))
            else:
                Tbl_Organization_Ownership_Transfer.objects.create(transfer_code=transfer_code, current_status=current_status)
                return Response(util.success(self,"Ownership Transfer successfuly"))
        except:
            return Response(util.error(self,"Something went wrong!"))
        
    def get(self, request, id=None):
        try:
            if id is None:
                Ownership_Transfer_obj = Tbl_Organization_Ownership_Transfer.objects.all()
                serializers_obj = Ownership_Transfe_Serializer(Ownership_Transfer_obj, many=True).data
                return Response(util.success(self,serializers_obj))
            else:
                Ownership_Transfer_obj = Tbl_Organization_Ownership_Transfer.objects.get(id=id)
                serializers_obj = Ownership_Transfe_Serializer(Ownership_Transfer_obj).data
                return Response(util.success(self,serializers_obj))
        except:
            return Response(util.error(self,"Something went wrong!"))

    def delete(self, request, id=None):
        try:
            Ownership_Transfer_obj = Tbl_Organization_Ownership_Transfer.objects.get(id=id)
            Ownership_Transfer_obj.delete()
            return Response("Ownership Transfer data deleted successfuly")
        except:
            return Response(util.error(self,"Something went wrong!"))
        
    def put(self, request, id=None):
        try:
            data = request.data
            transfer_code = data.get("transfer_code")
            transfer_code_verify = data.get("transfer_code_verify")
            current_status = data.get("current_status")

            Ownership_Transfer_obj = Tbl_Organization_Ownership_Transfer.objects.get(id=id)
            if transfer_code:
                Ownership_Transfer_obj.transfer_code=transfer_code  
            if transfer_code_verify:
                Ownership_Transfer_obj.transfer_code_verify=transfer_code_verify  
            if current_status:
                Ownership_Transfer_obj.current_status=current_status    

            Ownership_Transfer_obj.save()
            return Response(util.success(self,"Ownership Transfer update successfully"))        
        except:
            return Response(util.error(self,"Something went wrong!"))
        
# class Tbl_User_Purchase_Subscription_Views(APIView):
    
#     def post(self, request):
#         # try:
#             data = request.data
#             # purchase_date = data.get("purchase_date")
#             card_holder_name = data.get("card_holder_name")
#             country = data.get("country")
#             pincode = data.get("pincode")
#             card_last_four_digit = data.get("card_last_four_digit")
#             amount = data.get("amount")

#             if Tbl_User_Purchase_Subscription.objects.filter(card_last_four_digit=card_last_four_digit).exists():
#                 return Response("This Purchase Subscription already exist")
#             else:
#                 Tbl_User_Purchase_Subscription.objects.create(card_holder_name=card_holder_name, country=country, pincode=pincode, card_last_four_digit=card_last_four_digit, amount=amount)
#                 return Response("Purchase Subscription successfuly")
#         # except:
#         #     return Response("Something went wrong!")
        
#     def get(self, request, id=None):
#         try:
#             if id is None:
#                 purchase_subscription_obj = Tbl_User_Purchase_Subscription.objects.all()
#                 serializers_obj = Purchase_Subscription_Serializer(purchase_subscription_obj, many=True).data
#                 return Response(serializers_obj)
#             else:
#                 purchase_subscription_obj = Tbl_User_Purchase_Subscription.objects.get(id=id)
#                 serializers_obj = Purchase_Subscription_Serializer(purchase_subscription_obj).data
#                 return Response(serializers_obj)
#         except:
#             return Response("Something went wrong!")

#     def delete(self, request, id=None):
#         try:
#             purchase_subscription_obj = Tbl_User_Purchase_Subscription.objects.get(id=id)
#             purchase_subscription_obj.delete()
#             return Response("Ownership Transfer data deleted successfuly")
#         except:
#             return Response("Something went wrong!")
        
#     def put(self, request, id=None):
#         try:
#             data = request.data
#             # purchase_date = data.get("purchase_date")
#             card_holder_name = data.get("card_holder_name")
#             country = data.get("country")
#             pincode = data.get("pincode")
#             card_last_four_digit = data.get("card_last_four_digit")
#             amount = data.get("amount")

#             purchase_subscription_obj = Tbl_User_Purchase_Subscription.objects.get(id=id)
#             # if purchase_date:
#             #     purchase_subscription_obj.purchase_date=purchase_date  
#             if card_holder_name:
#                 purchase_subscription_obj.card_holder_name=card_holder_name  
#             if country:
#                 purchase_subscription_obj.country=country    
#             if pincode:
#                 purchase_subscription_obj.pincode=pincode  
#             if card_last_four_digit:
#                 purchase_subscription_obj.card_last_four_digit=card_last_four_digit  
#             if amount:
#                 purchase_subscription_obj.amount=amount    

#             purchase_subscription_obj.save()
#             return Response("Purchase Subscription update successfully")        
#         except:
#             return Response("Something went wrong!")