# Generated by Django 4.2.14 on 2024-08-06 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, help_text="商品更新時間", null=True),
        ),
    ]
