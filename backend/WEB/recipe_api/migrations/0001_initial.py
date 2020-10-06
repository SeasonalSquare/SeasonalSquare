# Generated by Django 3.1.1 on 2020-10-06 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calorie', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=150)),
                ('main_grocery', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('writer', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('allergies', models.ManyToManyField(blank=True, related_name='allergy_recipe', to='accounts.Allergy')),
                ('ingredients', models.ManyToManyField(blank=True, related_name='ingredients_recipe', to='recipe_api.Grocery')),
            ],
        ),
    ]
