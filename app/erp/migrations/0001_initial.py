# Generated by Django 5.0.1 on 2024-01-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=255, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'nuevo_producto',
            },
        ),
    ]
