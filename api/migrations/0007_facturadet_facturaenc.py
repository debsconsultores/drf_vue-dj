# Generated by Django 3.1 on 2021-01-04 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.cliente')),
            ],
            options={
                'verbose_name_plural': 'Encabezados de Factura',
            },
        ),
        migrations.CreateModel(
            name='FacturaDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('cabecera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='api.facturaenc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.producto')),
            ],
            options={
                'verbose_name_plural': 'Detalles de Factura',
            },
        ),
    ]