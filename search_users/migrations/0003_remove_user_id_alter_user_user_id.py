# Generated by Django 4.0.2 on 2022-02-04 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search_users", "0002_alter_user_user_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="id",),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                max_length=10, primary_key=True, serialize=False, verbose_name="USERID"
            ),
        ),
    ]
