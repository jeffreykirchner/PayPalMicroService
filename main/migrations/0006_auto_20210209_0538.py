# Generated by Django 3.1.5 on 2021-02-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_payments_ip_whitelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ip_whitelist',
            name='name',
            field=models.CharField(default='', max_length=250, unique=True, verbose_name='App Name'),
        ),
    ]
