# Generated by Django 3.1.4 on 2021-01-01 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_remove_post_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(default='test', upload_to='media'),
            preserve_default=False,
        ),
    ]