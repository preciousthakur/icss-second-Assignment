# Generated by Django 3.1.1 on 2020-11-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_contact_popup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='inquiry',
            field=models.TextField(null=True),
        ),
    ]
