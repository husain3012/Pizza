# Generated by Django 3.0.4 on 2020-05-20 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='username',
            field=models.CharField(default='Guest', max_length=64),
        ),
    ]
