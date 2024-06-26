# Generated by Django 4.2.5 on 2024-02-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_tbl_organization_ownership_transfer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_User_Purchase_Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('card_holder_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
                ('card_last_four_digit', models.CharField(max_length=4)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
