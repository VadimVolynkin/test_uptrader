# Generated by Django 4.1.7 on 2023-02-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_categorymenu_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymenu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.categorymenu'),
        ),
    ]
