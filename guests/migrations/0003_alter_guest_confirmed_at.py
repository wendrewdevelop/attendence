# Generated by Django 5.0.7 on 2024-07-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_alter_guest_confirmed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='confirmed_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de confirmação'),
        ),
    ]