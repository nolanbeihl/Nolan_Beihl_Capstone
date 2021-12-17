# Generated by Django 3.2.8 on 2021-12-17 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entertainments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExplorerEntertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entertainmentId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entertainments.entertainment')),
            ],
        ),
    ]
