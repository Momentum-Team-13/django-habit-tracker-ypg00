# Generated by Django 4.0.6 on 2022-07-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_record_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
    ]
