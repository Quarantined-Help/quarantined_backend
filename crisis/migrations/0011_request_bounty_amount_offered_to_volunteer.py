# Generated by Django 3.0.4 on 2021-03-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("crisis", "0010_auto_20201017_1005")]

    operations = [
        migrations.AddField(
            model_name="request",
            name="bounty_amount_offered_to_volunteer",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        )
    ]