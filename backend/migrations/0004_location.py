# Generated by Django 3.0.2 on 2020-09-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_ordered_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=150, verbose_name='location')),
                ('price', models.IntegerField(verbose_name='price')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
    ]
