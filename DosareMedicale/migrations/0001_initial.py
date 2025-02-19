# Generated by Django 5.1.3 on 2024-12-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=20)),
                ('pet_species', models.CharField(max_length=20)),
                ('pet_breed', models.CharField(max_length=20)),
                ('pet_weight', models.DecimalField(decimal_places=2, help_text='Greutatea în kg', max_digits=5)),
                ('pet_color_and_markings', models.CharField(max_length=50)),
                ('pet_gender', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('pet_vaccine', models.CharField(blank=True, help_text='Vaccinările', max_length=20)),
                ('pet_reproductive_status', models.CharField(choices=[('I', 'Intact'), ('S', 'Sterilizat')], max_length=10)),
                ('pet_disease', models.CharField(blank=True, help_text='Boli cronice', max_length=20)),
                ('pet_treatments', models.CharField(blank=True, help_text='Tratamente medicale', max_length=20)),
                ('pet_medication', models.CharField(blank=True, help_text='Medicație curentă', max_length=20)),
            ],
        ),
    ]
