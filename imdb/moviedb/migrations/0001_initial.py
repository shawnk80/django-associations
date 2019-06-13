# Generated by Django 2.1.5 on 2019-06-13 19:06

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviedb.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviedb.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(related_name='movie', through='moviedb.Role', to='moviedb.Actor'),
        ),
    ]
