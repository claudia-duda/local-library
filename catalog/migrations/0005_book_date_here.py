# Generated by Django 3.0.5 on 2020-05-27 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_book_book_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_here',
            field=models.DateField(default=datetime.date(2020, 5, 27)),
        ),
    ]