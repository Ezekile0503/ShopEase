# Generated by Django 4.0 on 2023-12-06 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cartname', models.CharField(max_length=255)),
                ('store_wheretobuy', models.CharField(max_length=255)),
                ('date_for_notification', models.DateField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
