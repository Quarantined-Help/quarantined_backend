# Generated by Django 3.0.4 on 2020-03-23 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0002_ability_verb"),
        ("crisis", "0004_auto_20200323_2112"),
    ]

    operations = [
        migrations.AlterField(
            model_name="participant",
            name="abilities",
            field=models.ManyToManyField(to="management.Ability"),
        )
    ]
