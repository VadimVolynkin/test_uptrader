# Generated by Django 4.1.7 on 2023-02-21 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=50)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.categorymenu')),
            ],
        ),
    ]
