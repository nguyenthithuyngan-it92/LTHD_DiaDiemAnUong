# Generated by Django 4.1.7 on 2023-03-29 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menufood', '0004_alter_user_name_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='menuitem_food', to='menufood.menuitem'),
        ),
    ]
