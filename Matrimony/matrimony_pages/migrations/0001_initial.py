# Generated by Django 3.2.3 on 2021-05-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.CharField(max_length=3, null=True)),
                ('thegai', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
