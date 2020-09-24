# Generated by Django 3.0.2 on 2020-09-24 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerId', models.CharField(max_length=100, verbose_name='customer Id')),
                ('fullName', models.CharField(max_length=250, verbose_name='full name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phoneNumber', models.CharField(max_length=50, verbose_name='phone Number')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderId', models.CharField(max_length=50, verbose_name='Order Id')),
                ('total', models.IntegerField(default=1, verbose_name='total')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='backend.Customer', verbose_name='customer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=150, verbose_name='size')),
                ('price', models.IntegerField(verbose_name='price')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('image', models.ImageField(default='image', upload_to='', verbose_name='image')),
                ('flavour', models.CharField(blank=True, default='null', max_length=200, verbose_name='flavour')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.IntegerField(blank=True, default=0, verbose_name='price')),
                ('multipleSIzes', models.ManyToManyField(blank=True, related_name='multiplesizes', to='backend.Size', verbose_name='multiplesizes')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=156, verbose_name='name')),
                ('flavour', models.CharField(default='null', max_length=156, verbose_name='flavour')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantity')),
                ('price', models.IntegerField()),
                ('size', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='backend.Product', verbose_name='product')),
                ('purchaseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchaseId', to='backend.Ordered', verbose_name='purchase id')),
            ],
            options={
                'verbose_name': 'OrderedProduct',
                'verbose_name_plural': 'OrderedProducts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('products', models.ManyToManyField(blank=True, to='backend.Product', verbose_name='products')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
