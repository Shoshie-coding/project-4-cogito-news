# Generated by Django 3.2.12 on 2022-03-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='default', max_length=250),
            preserve_default=False,
        ),
    ]