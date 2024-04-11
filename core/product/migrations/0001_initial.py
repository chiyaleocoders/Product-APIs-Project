# Generated by Django 4.2.5 on 2024-02-18 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, default=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, default=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, default=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_quantity', models.PositiveIntegerField()),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='Product Main Image')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(blank=True, default=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, default=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categorymaster')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewProductMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, default=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmaster')),
            ],
        ),
        migrations.AddField(
            model_name='productmaster',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategorymaster'),
        ),
        migrations.CreateModel(
            name='ProductImageMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='Product Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmaster')),
            ],
        ),
    ]
