# Generated by Django 2.2.6 on 2019-11-04 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20191103_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobjective',
            name='objective_description',
            field=models.TextField(),
        ),
    ]
