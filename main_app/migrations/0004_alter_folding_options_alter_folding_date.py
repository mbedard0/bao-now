# Generated by Django 4.0 on 2021-12-31 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_folding'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='folding',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='folding',
            name='date',
            field=models.DateField(verbose_name='Folding date'),
        ),
    ]