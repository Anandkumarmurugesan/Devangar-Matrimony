# Generated by Django 3.2.3 on 2021-06-02 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_pages', '0009_bride_jsonfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bride',
            name='Jsonfield',
        ),
    ]