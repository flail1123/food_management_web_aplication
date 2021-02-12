# Generated by Django 2.2 on 2021-01-24 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0012_auto_20210124_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='basicplan',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.Plan'),
        ),
        migrations.AlterField(
            model_name='basicplan',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customplan',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.Plan'),
        ),
        migrations.AlterField(
            model_name='customplan',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.FoodSet')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.FoodSet')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_eating', models.DateField()),
                ('food_set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.FoodSet')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=5)),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.Food')),
                ('food_set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.FoodSet')),
            ],
        ),
    ]
