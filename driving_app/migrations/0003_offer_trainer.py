# Generated by Django 4.2 on 2023-05-10 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("driving_app", "0002_feedback"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
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
                ("contents", models.CharField(max_length=100)),
                ("date", models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Trainer",
            fields=[
                (
                    "trainerid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=45)),
                ("name", models.CharField(max_length=30)),
                ("address", models.TextField(verbose_name=45)),
                ("email", models.EmailField(max_length=45)),
                ("gender", models.CharField(max_length=6)),
                ("phone", models.IntegerField(max_length=10)),
                ("age", models.IntegerField()),
                ("cityname", models.CharField(max_length=45)),
                ("experience", models.CharField(max_length=45)),
                ("otherdetails", models.TextField()),
                (
                    "trainerpic",
                    models.FileField(default="", upload_to="driving_app/picture"),
                ),
            ],
        ),
    ]
