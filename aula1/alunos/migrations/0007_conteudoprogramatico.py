# Generated by Django 5.1.2 on 2024-10-31 00:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0006_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConteudoProgramatico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(null=True)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conteudos_programaticos', to='alunos.disciplina')),
            ],
        ),
    ]
