# Generated by Django 3.2.6 on 2021-08-13 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indica si el objeto ha sido eliminado o no.')),
                ('deleted_at', models.DateTimeField(help_text='Día y hora en que se eliminó el objeto', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Día y hora de creación del objeto')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Día y hora de modificación del objeto')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'actor',
                'verbose_name_plural': 'actors',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indica si el objeto ha sido eliminado o no.')),
                ('deleted_at', models.DateTimeField(help_text='Día y hora en que se eliminó el objeto', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Día y hora de creación del objeto')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Día y hora de modificación del objeto')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'director',
                'verbose_name_plural': 'directors',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indica si el objeto ha sido eliminado o no.')),
                ('deleted_at', models.DateTimeField(help_text='Día y hora en que se eliminó el objeto', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Día y hora de creación del objeto')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Día y hora de modificación del objeto')),
                ('name', models.CharField(max_length=10)),
                ('price', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'format',
                'verbose_name_plural': 'formats',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indica si el objeto ha sido eliminado o no.')),
                ('deleted_at', models.DateTimeField(help_text='Día y hora en que se eliminó el objeto', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Día y hora de creación del objeto')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Día y hora de modificación del objeto')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indica si el objeto ha sido eliminado o no.')),
                ('deleted_at', models.DateTimeField(help_text='Día y hora en que se eliminó el objeto', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Día y hora de creación del objeto')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Día y hora de modificación del objeto')),
                ('name', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('clasification', models.CharField(choices=[('1', 'A - Todo público'), ('2', 'B - Todo público, mayores de 6 años'), ('3', 'B12 - Mayores de 12 años'), ('4', 'B15 - Mayores de 15 años'), ('5', 'C - Mayores de 18 años')], default='1', max_length=3)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
                'ordering': ['name', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indica si el objeto ha sido eliminado o no.')),
                ('deleted_at', models.DateTimeField(help_text='Día y hora en que se eliminó el objeto', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Día y hora de creación del objeto')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Día y hora de modificación del objeto')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('movie_format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.format')),
            ],
            options={
                'verbose_name': 'screening',
                'verbose_name_plural': 'screenings',
                'ordering': ['movie_format', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Casting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='Indica si el objeto ha sido eliminado o no.')),
                ('deleted_at', models.DateTimeField(help_text='Día y hora en que se eliminó el objeto', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Día y hora de creación del objeto')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Día y hora de modificación del objeto')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'verbose_name': 'casting',
                'verbose_name_plural': 'castings',
                'ordering': ['movie', 'id'],
            },
        ),
    ]
