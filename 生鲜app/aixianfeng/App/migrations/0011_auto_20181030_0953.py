# Generated by Django 2.0.6 on 2018-10-30 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_goods'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='category',
            new_name='categoryid',
        ),
    ]
