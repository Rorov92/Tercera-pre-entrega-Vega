from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('consola', models.CharField(max_length=256)),
                ('edad', models.CharField(max_length=256)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_hardware', models.CharField(max_length=256)),
                ('consola', models.CharField(max_length=256)),
                ('tipo', models.CharField(max_length=256)),
            ],
        ),
    ]
