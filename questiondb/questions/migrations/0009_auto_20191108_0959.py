# Generated by Django 2.2.7 on 2019-11-08 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_question_upload_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='upload_img',
            new_name='document',
        ),
    ]
