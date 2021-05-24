# Generated by Django 3.1.6 on 2021-05-24 20:25

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import main_app.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affectation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Centre_titre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegesterUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Userconnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='SousCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sous_centre_titre', models.CharField(max_length=100)),
                ('centre_titre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.affectation')),
            ],
        ),
        migrations.CreateModel(
            name='MaterielModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero_inventaire_entre', models.CharField(blank=True, default=main_app.utils.create_new_ref_number, editable=False, max_length=10, unique=True)),
                ('Designation_Object', models.CharField(max_length=80)),
                ('Quantite', models.IntegerField()),
                ('Etat', models.CharField(default='Nouveau', max_length=100)),
                ('Emplacement', models.CharField(max_length=100)),
                ('Date_reception', models.DateTimeField(auto_now_add=True)),
                ('Prix_achat_unite', models.FloatField()),
                ('Prix_achat_total', models.FloatField()),
                ('Marque', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('Serie', models.CharField(max_length=100)),
                ('Observation', models.CharField(max_length=100)),
                ('author_reception', models.CharField(max_length=10)),
                ('Category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.categoriesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero_inventaire_sortie', models.CharField(blank=True, default=main_app.utils.create_new_ref_number, editable=False, max_length=10, unique=True)),
                ('Titre_livraison', models.CharField(max_length=100)),
                ('Date_sortie', models.DateTimeField(auto_now_add=True)),
                ('Quantite_livree', models.IntegerField()),
                ('Prix_unitaire', models.FloatField()),
                ('Decompte', models.CharField(max_length=100)),
                ('Signatures', models.CharField(max_length=100)),
                ('author_livraison', models.CharField(max_length=10)),
                ('Affectation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.affectation')),
                ('Materiel', models.ManyToManyField(related_name='Materiel_id', to='main_app.MaterielModel')),
                ('Sous_centre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.souscentre')),
            ],
        ),
        migrations.CreateModel(
            name='historique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Centre_titre', models.CharField(max_length=100)),
                ('Sous_centre_titre', models.CharField(max_length=100)),
                ('Livraison_historique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.livraison')),
                ('Materiel_historique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.materielmodel')),
            ],
        ),
    ]
