# Generated by Django 3.0.7 on 2020-07-27 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0026_auto_20200724_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfop',
            name='kved',
        ),
        migrations.RemoveField(
            model_name='rfop',
            name='state',
        ),
        migrations.RemoveField(
            model_name='ruo',
            name='kved',
        ),
        migrations.RemoveField(
            model_name='ruo',
            name='state',
        ),
        migrations.RenameField(
            model_name='fop',
            old_name='hash_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='historicalfop',
            old_name='hash_code',
            new_name='code',
        ),
        migrations.DeleteModel(
            name='Founders',
        ),
        migrations.DeleteModel(
            name='Rfop',
        ),
        migrations.DeleteModel(
            name='Ruo',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]