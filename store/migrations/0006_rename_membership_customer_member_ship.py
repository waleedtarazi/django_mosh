# Generated by Django 4.1.3 on 2022-11-08 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_auto_20221108_1710"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="membership",
            new_name="member_ship",
        ),
    ]
