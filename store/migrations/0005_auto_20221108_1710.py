# Generated by Django 4.1.3 on 2022-11-08 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_adress_zip"),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO store_collection (tittle)
        VALUES ('collection1')
        """ , """
        DELETE FROM store_collection
        WHERE tittle = 'collection1' 
        """)

    ]
