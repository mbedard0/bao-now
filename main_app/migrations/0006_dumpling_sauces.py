# Generated by Django 4.0 on 2022-01-01 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_sauce'),
    ]

    operations = [
        migrations.AddField(
            model_name='dumpling',
            name='sauces',
            field=models.ManyToManyField(to='main_app.Sauce'),
        ),
    ]
