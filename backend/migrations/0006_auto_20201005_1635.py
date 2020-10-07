# Generated by Django 3.0.2 on 2020-10-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200930_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=150, verbose_name='topping')),
                ('price', models.IntegerField(verbose_name='price')),
            ],
            options={
                'verbose_name': 'Topping',
                'verbose_name_plural': 'Toppings',
            },
        ),
        migrations.RemoveField(
            model_name='orderedproduct',
            name='flavour',
        ),
        migrations.RemoveField(
            model_name='product',
            name='flavour',
        ),
        migrations.AddField(
            model_name='orderedproduct',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='orderedtoppings', to='backend.Topping', verbose_name='toppings'),
        ),
        migrations.AddField(
            model_name='product',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='backend.Topping', verbose_name='toppings'),
        ),
    ]