# Generated by Django 3.2.3 on 2021-05-28 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_pages', '0004_auto_20210528_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bride',
            old_name='Under_Graduation',
            new_name='Post_Graduation_Degree',
        ),
        migrations.AddField(
            model_name='bride',
            name='Under_Graduation_Degree',
            field=models.CharField(max_length=200, null=True),
        ),
    ]