# Generated by Django 4.1.7 on 2023-04-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menufood', '0005_alter_order_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]