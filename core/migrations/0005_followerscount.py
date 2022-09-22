# Generated by Django 4.1 on 2022-09-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_post_no_of_likes"),
    ]

    operations = [
        migrations.CreateModel(
            name="FollowersCount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("follower", models.CharField(max_length=100)),
                ("user", models.CharField(max_length=100)),
            ],
        ),
    ]
