# Generated by Django 3.1.5 on 2021-02-07 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210207_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parameters',
            old_name='contactEmail',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='parameters',
            old_name='maxDailyEarnings',
            new_name='max_daily_earnings',
        ),
        migrations.RenameField(
            model_name='parameters',
            old_name='siteURL',
            new_name='site_URL',
        ),
    ]