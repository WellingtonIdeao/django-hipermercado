# Generated by Django 2.2.7 on 2019-11-11 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ManyToManyField(to='app.Categoria'),
        ),
    ]