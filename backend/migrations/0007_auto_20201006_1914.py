# Generated by Django 3.0.2 on 2020-10-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20201005_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedproduct',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='product',
            name='toppings',
        ),
        migrations.CreateModel(
            name='ToppingsCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('toppings', models.ManyToManyField(blank=True, related_name='toppings', to='backend.Topping', verbose_name='toppings')),
            ],
            options={
                'verbose_name': 'ToppingsCollection',
                'verbose_name_plural': 'ToppingsCollections',
            },
        ),
    ]
