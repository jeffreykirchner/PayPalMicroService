# Generated by Django 3.1.5 on 2021-02-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210209_0538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Payment', 'verbose_name_plural': 'Payments'},
        ),
        migrations.AddField(
            model_name='parameters',
            name='paypal_token',
            field=models.CharField(default='https://www.google.com/', max_length=200),
        ),
    ]
