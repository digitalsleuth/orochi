# Generated by Django 5.1 on 2024-09-10 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ya", "0007_rule_search_vector"),
    ]

    operations = [
        migrations.AddField(
            model_name="rule",
            name="error",
            field=models.TextField(blank=True, null=True),
        ),
    ]
