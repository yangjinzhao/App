# Generated by Django 2.0.6 on 2018-10-29 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '导航表',
                'verbose_name_plural': '导航表',
                'db_table': 'axf_nav',
            },
        ),
    ]
