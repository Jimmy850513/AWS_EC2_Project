# Generated by Django 4.2.14 on 2024-08-06 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_item_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="status",
            field=models.CharField(help_text="商品目前的狀態", max_length=20, null=True),
        ),
    ]
