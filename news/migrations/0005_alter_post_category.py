# Generated by Django 3.2.12 on 2022-04-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(
                choices=[
                    ('Arts-culture',
                     'Arts-culture'),
                    ('Technology',
                     'Technology'),
                    ('Movies%20and%20Music',
                     'Movies and Music'),
                    ('Travel',
                     'Travel')],
                max_length=250),
        ),
    ]
