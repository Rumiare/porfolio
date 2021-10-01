# Generated by Django 3.2.6 on 2021-09-28 05:36

import blogs.models
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_testupload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testupload',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blogs.models.TestUpload.image),
        ),
    ]