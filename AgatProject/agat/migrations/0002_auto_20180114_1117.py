# Generated by Django 2.0.1 on 2018-01-14 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flatpaneldispla',
            old_name='display_test_date',
            new_name='data_testu',
        ),
        migrations.RenameField(
            model_name='flatpaneldispla',
            old_name='box_number_text',
            new_name='numer_kartonu',
        ),
        migrations.RenameField(
            model_name='flatpaneldispla',
            old_name='display_size_text',
            new_name='osoba_testujaca',
        ),
        migrations.RenameField(
            model_name='flatpaneldispla',
            old_name='display_vendor_text',
            new_name='producent_panelu',
        ),
        migrations.RenameField(
            model_name='flatpaneldispla',
            old_name='pallet_number_text',
            new_name='rozmiar_panelu',
        ),
        migrations.RenameField(
            model_name='flatpaneldispla',
            old_name='tester_text',
            new_name='umer_palety',
        ),
    ]
