# Generated by Django 3.1.7 on 2021-03-16 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['id'],
                'unique_together': {('name',)},
            },
        ),
    ]
