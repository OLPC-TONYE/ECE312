# Generated by Django 4.1.3 on 2022-11-25 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calculation_title', models.CharField(max_length=200)),
                ('calculation_date', models.DateTimeField(verbose_name='date_calculated')),
            ],
        ),
        migrations.CreateModel(
            name='CalculationVariables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electrical_mobility', models.FloatField(verbose_name='dm')),
                ('mass', models.FloatField(verbose_name='m')),
                ('result', models.FloatField(verbose_name='effective_density')),
                ('calculation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.calculation')),
            ],
        ),
    ]