# Generated by Django 4.2.5 on 2024-02-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_tbl_cost_revenue_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_Tax_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=255)),
                ('tax_id', models.CharField(max_length=255, unique=True)),
                ('tax_code', models.CharField(max_length=255, unique=True)),
                ('tax_rate', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'masterapp_tbl_tax_m',
            },
        ),
    ]
