# Generated by Django 2.1.5 on 2019-01-24 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statmoney', '0002_auto_20190124_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balanco',
            old_name='Aplicacoes_Interfinanceiras_Liquidez',
            new_name='Aplic_Interf_Liq1',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Imobilizado_Arrendamento',
            new_name='Aplic_Interf_Liq2',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Imobilizado_Uso',
            new_name='Imob_Arrendamento',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Obrigacoes_por_Emprestimos',
            new_name='Imob_Uso',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Obrigacoes_por_Repasse_do_Exterior',
            new_name='Obrig_Emprestimos',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Obrigacoes_por_Repasse_do_Pais',
            new_name='Obrig_Repasse_Exterior',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Operacoes_Arrendamento_Mercantil',
            new_name='Obrig_Repasse_Pais',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Operacoes_Credito',
            new_name='Opr_Arrendamento_Mercantil',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Outras_Obrigacoes',
            new_name='Opr_Credito',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Outros_Valores_Bens',
            new_name='Outras_Obrig',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Recursos_Aceites_Emissao_Titulos',
            new_name='Outros_Val_Bens',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Relacoes_Interdependencias',
            new_name='Recursos_Aceites_Emissao_Tit',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Relacoes_Interfinanceiras',
            new_name='Relac_Interdep',
        ),
        migrations.RenameField(
            model_name='balanco',
            old_name='Titulos_Valores_Mobiliarios',
            new_name='Relac_Interf',
        ),
        migrations.AddField(
            model_name='balanco',
            name='Tit_Val_Mobil',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
        ),
    ]
