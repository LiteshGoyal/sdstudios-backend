# Generated by Django 5.1.4 on 2025-01-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_rename_subheading_blogs_subtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]