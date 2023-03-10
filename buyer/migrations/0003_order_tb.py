# Generated by Django 3.2.8 on 2022-09-27 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_rename_categotyid_addproduct_tb_categoryid'),
        ('buyer', '0002_cart_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shippindaddress', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('phonenumber', models.CharField(max_length=20)),
                ('totalprice', models.IntegerField()),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyerregistration_tb')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.addproduct_tb')),
                ('sellerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.sellerregistration_tb')),
            ],
        ),
    ]
