# Generated by Django 3.2.8 on 2022-02-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=5)),
                ('review_rating', models.IntegerField()),
                ('date_visited', models.DateField()),
                ('location', models.CharField(max_length=250)),
            ],
        ),
    ]
