from rest_framework import status
from product.models import *

def success(self, msg):
    response = {
                    "message": msg,
                    "status" : "success",
                    "code"   : status.HTTP_200_OK
                }
    return response

def error(self, msg, errmsg=None):
    response = {    
                    "errmsg":errmsg,
                    "message": msg,
                    "status" : "failed",
                    "code"   : status.HTTP_400_BAD_REQUEST
                }
    return response

# def loginsuccess(self, msg,statuss):
#     response = {
#                     "message": msg,
#                     "status" : "success",
#                     "code"   : status.HTTP_200_OK,
#                     "verify_status": statuss
#                 }
#     return response

# def loginerror(self, msg,statuss):
#     response = {
#                     "message": msg,
#                     "status" : "failed",
#                     "code"   : status.HTTP_400_BAD_REQUEST,
#                     "verify_status": statuss
#                 }
#     return response

# from datetime import timedelta

# def otp_send(base,user):
#     user_otp=random.randint(100000, 999999)
#     now = timezone.now()
#     expire_at = now + timedelta(minutes = 10)
#     UserAuth.objects.filter(email = user).update(otp = user_otp, otp_expire_at = expire_at)
#     # Send Email to user
#     en = EmailNotification()
#     detail = {'email': str(user), 'Otp':user_otp}
#     print("data",detail)
#     email_status = en.send_email(user, 'Otp-Verification','', 'otp-verification', detail)
#     return email_status

# from datetime import timedelta  # Import timedelta from the datetime module

# def otpsend(base, user):
#     user_otp = random.randint(100000, 999999)
#     now = timezone.now()
#     expire_at = now + timedelta(minutes=10)
#     UserEmailChangeLog.objects.filter(new_email=user).update(otp=user_otp, otp_expire_at=expire_at)
#     en = EmailNotification()
#     detail = {'email': str(user), 'Otp': user_otp}
#     email_status = en.send_email(user, 'Otp-Verification', '', 'otp-verification', detail)
#     return user_otp, email_status
