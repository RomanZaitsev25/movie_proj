# Generated by Django 4.0.3 on 2022-08-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0009_rename_choices_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(blank=True, default=1000000),
        ),
    ]
