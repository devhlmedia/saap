# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 13:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cerimonial', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parlamentares', '0021_merge'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefone',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='operadora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='telefone_set', to='cerimonial.OperadoraTelefonia', verbose_name='Operadora de Telefonia'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='telefone_set', to='cerimonial.TipoTelefone', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='processo',
            name='assuntos',
            field=models.ManyToManyField(blank=True, related_name='processo_set', to='cerimonial.AssuntoProcesso', verbose_name='Assuntos'),
        ),
        migrations.AddField(
            model_name='processo',
            name='classificacoes',
            field=models.ManyToManyField(blank=True, related_name='processo_set', to='cerimonial.ClassificacaoProcesso', verbose_name='Classificações'),
        ),
        migrations.AddField(
            model_name='processo',
            name='contatos',
            field=models.ManyToManyField(blank=True, related_name='processo_set', to='cerimonial.Contato', verbose_name='Contatos Interessados no Processo'),
        ),
        migrations.AddField(
            model_name='processo',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='processo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='processo',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='processo_set', to='cerimonial.StatusProcesso', verbose_name='Status do Processo'),
        ),
        migrations.AddField(
            model_name='processo',
            name='topicos',
            field=models.ManyToManyField(blank=True, related_name='processo_set', to='cerimonial.TopicoProcesso', verbose_name='Tópicos'),
        ),
        migrations.AddField(
            model_name='processo',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processo_set', to='core.AreaTrabalho', verbose_name='Área de Trabalho'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localtrabalho_set', to='cerimonial.Contato', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='distrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='localtrabalho_set', to='core.Distrito', verbose_name='Distrito'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='localtrabalho_set', to='parlamentares.Municipio', verbose_name='Município'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='regiao_municipal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='localtrabalho_set', to='core.RegiaoMunicipal', verbose_name='Região Municipal'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='localtrabalho_set', to='cerimonial.TipoLocalTrabalho', verbose_name='Tipo do Local de Trabalho'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='trecho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='localtrabalho_set', to='core.Trecho', verbose_name='Trecho'),
        ),
        migrations.AddField(
            model_name='filiacaopartidaria',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filiacaopartidaria_set', to='cerimonial.Contato', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='filiacaopartidaria',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='filiacaopartidaria',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='filiacaopartidaria',
            name='partido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filiacaopartidaria_set', to='parlamentares.Partido', verbose_name='Partido'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='bairro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_set', to='core.Bairro', verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco_set', to='cerimonial.Contato', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='distrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_set', to='core.Distrito', verbose_name='Distrito'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_set', to='parlamentares.Municipio', verbose_name='Município'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='regiao_municipal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_set', to='core.RegiaoMunicipal', verbose_name='Região Municipal'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_set', to='cerimonial.TipoEndereco', verbose_name='Tipo do Endereço'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='trecho',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_set', to='core.Trecho', verbose_name='Trecho'),
        ),
        migrations.AddField(
            model_name='email',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_set', to='cerimonial.Contato', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='email',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='email',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='email',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_set', to='cerimonial.TipoEmail', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='dependente',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependente_set', to='cerimonial.Contato', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='dependente',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='dependente',
            name='nivel_instrucao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dependente_set', to='cerimonial.NivelInstrucao', verbose_name='Nivel de Instrução'),
        ),
        migrations.AddField(
            model_name='dependente',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='dependente',
            name='parentesco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='cerimonial.Parentesco', verbose_name='Parentesco'),
        ),
        migrations.AddField(
            model_name='contato',
            name='estado_civil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contato_set', to='cerimonial.EstadoCivil', verbose_name='Estado Civil'),
        ),
        migrations.AddField(
            model_name='contato',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='contato',
            name='nivel_instrucao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contato_set', to='cerimonial.NivelInstrucao', verbose_name='Nivel de Instrução'),
        ),
        migrations.AddField(
            model_name='contato',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='contato',
            name='perfil_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contato_set', to=settings.AUTH_USER_MODEL, verbose_name='Perfil do Usuário'),
        ),
        migrations.AddField(
            model_name='contato',
            name='pronome_tratamento',
            field=models.ForeignKey(blank=True, help_text='O pronome de tratamento é opcional, mas será         obrigatório caso seja selecionado um tipo de autoridade.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contato_set', to='cerimonial.PronomeTratamento', verbose_name='Pronome de Tratamento'),
        ),
        migrations.AddField(
            model_name='contato',
            name='tipo_autoridade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contato_set', to='cerimonial.TipoAutoridade', verbose_name='Tipo de Autoridade'),
        ),
        migrations.AddField(
            model_name='contato',
            name='workspace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contato_set', to='core.AreaTrabalho', verbose_name='Área de Trabalho'),
        ),
        migrations.AddField(
            model_name='assuntoprocesso',
            name='modifier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='modifier'),
        ),
        migrations.AddField(
            model_name='assuntoprocesso',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='assuntoprocesso',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assuntoprocesso_set', to='core.AreaTrabalho', verbose_name='Área de Trabalho'),
        ),
        migrations.CreateModel(
            name='DependentePerfil',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Dependentes do Perfil',
                'proxy': True,
                'verbose_name': 'Dependente do Perfil',
            },
            bases=('cerimonial.dependente',),
        ),
        migrations.CreateModel(
            name='EmailPerfil',
            fields=[
            ],
            options={
                'verbose_name_plural': "Email's do Perfil",
                'proxy': True,
                'verbose_name': 'Email do Perfil',
            },
            bases=('cerimonial.email',),
        ),
        migrations.CreateModel(
            name='EnderecoPerfil',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Endereços do Perfil',
                'proxy': True,
                'verbose_name': 'Endereço do Perfil',
            },
            bases=('cerimonial.endereco',),
        ),
        migrations.CreateModel(
            name='LocalTrabalhoPerfil',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Locais de Trabalho do Perfil',
                'proxy': True,
                'verbose_name': 'Local de Trabalho do Perfil',
            },
            bases=('cerimonial.localtrabalho',),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('cerimonial.contato',),
        ),
        migrations.CreateModel(
            name='ProcessoContato',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Processos',
                'proxy': True,
                'verbose_name': 'Processo',
            },
            bases=('cerimonial.processo',),
        ),
        migrations.CreateModel(
            name='TelefonePerfil',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Telefones do Perfil',
                'proxy': True,
                'verbose_name': 'Telefone do Perfil',
            },
            bases=('cerimonial.telefone',),
        ),
    ]
