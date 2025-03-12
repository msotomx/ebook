# Generated by Django 4.2 on 2025-03-11 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13)),
                ('sexo', models.CharField(default='M', max_length=1)),
                ('telefono', models.CharField(max_length=12)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('direccion', models.TextField()),
                ('campo_libre', models.CharField(max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('numero_pedido', models.CharField(max_length=20, null=True)),
                ('monto_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estado', models.CharField(choices=[('0', 'Solicitado'), ('1', 'Pagado')], default='0', max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='sku',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='comentarios',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='plazo_credito',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.producto')),
            ],
        ),
    ]
