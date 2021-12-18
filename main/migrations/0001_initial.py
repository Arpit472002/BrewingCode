# Generated by Django 4.0 on 2021-12-18 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=200)),
                ('item_brand', models.CharField(max_length=100)),
                ('item_price', models.IntegerField()),
                ('item_image', models.ImageField(default='images/default-product-image.jpg', upload_to='images/')),
                ('available_quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('item_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_category', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_bill', models.IntegerField(blank=True, null=True)),
                ('payment_method', models.CharField(choices=[('CASH ON DELIVERY', 'CASH ON DELIVERY'), ('CREDIT CARD', 'CREDIT CARD'), ('NETBANKING', 'NETBANKING'), ('UPI', 'UPI')], max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ordered_items', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.orderitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_signup.myuser')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.itemtype'),
        ),
        migrations.AddField(
            model_name='item',
            name='owned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_signup.myuser'),
        ),
    ]
