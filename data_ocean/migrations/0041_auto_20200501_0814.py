# Generated by Django 2.0.9 on 2020-05-01 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data_ocean', '0040_auto_20200501_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfop',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rfop',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='rfop',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]