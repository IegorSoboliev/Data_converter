# Generated by Django 2.0.9 on 2020-06-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_register', '0005_auto_20200605_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drvstreet',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='drvstreet',
            name='previous_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
