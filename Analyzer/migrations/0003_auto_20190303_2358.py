# Generated by Django 2.1.7 on 2019-03-03 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Analyzer', '0002_auto_20190303_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='general_expenses',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='general_expenses',
            name='date_spent',
        ),
    ]
