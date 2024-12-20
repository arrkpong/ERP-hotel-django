# Generated by Django 5.1.4 on 2024-12-07 23:42

import django.core.validators
import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guests', '0001_initial'),
        ('rooms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(help_text='วันที่ลูกค้าจะเข้าพัก', verbose_name='วันที่เช็คอิน')),
                ('check_out', models.DateField(help_text='วันที่ลูกค้าจะเช็คเอาท์', verbose_name='วันที่เช็คเอาท์')),
                ('cancellation_fee', models.DecimalField(decimal_places=2, default=0.0, help_text='ค่าธรรมเนียมที่จะถูกเรียกเก็บหากลูกค้ายกเลิกการจอง', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='ค่าธรรมเนียมยกเลิก')),
                ('refundable', models.BooleanField(default=True, help_text='ระบุว่าการจองนี้สามารถขอคืนเงินได้หรือไม่', verbose_name='สามารถคืนเงินได้')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='วันที่และเวลาที่บันทึกการจอง', verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='วันที่และเวลาที่มีการแก้ไขข้อมูลล่าสุด', verbose_name='แก้ไขเมื่อ')),
                ('guest', models.ForeignKey(help_text='ลูกค้าที่ทำการจองห้องพัก', on_delete=django.db.models.deletion.CASCADE, to='guests.guest', verbose_name='ลูกค้า')),
                ('room', models.ForeignKey(help_text='ห้องพักที่ลูกค้าทำการจอง', on_delete=django.db.models.deletion.CASCADE, to='rooms.room', verbose_name='ห้องพัก')),
            ],
            options={
                'verbose_name': 'การจอง',
                'verbose_name_plural': 'การจอง',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalBooking',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('check_in', models.DateField(help_text='วันที่ลูกค้าจะเข้าพัก', verbose_name='วันที่เช็คอิน')),
                ('check_out', models.DateField(help_text='วันที่ลูกค้าจะเช็คเอาท์', verbose_name='วันที่เช็คเอาท์')),
                ('cancellation_fee', models.DecimalField(decimal_places=2, default=0.0, help_text='ค่าธรรมเนียมที่จะถูกเรียกเก็บหากลูกค้ายกเลิกการจอง', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='ค่าธรรมเนียมยกเลิก')),
                ('refundable', models.BooleanField(default=True, help_text='ระบุว่าการจองนี้สามารถขอคืนเงินได้หรือไม่', verbose_name='สามารถคืนเงินได้')),
                ('created_at', models.DateTimeField(blank=True, editable=False, help_text='วันที่และเวลาที่บันทึกการจอง', verbose_name='สร้างเมื่อ')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, help_text='วันที่และเวลาที่มีการแก้ไขข้อมูลล่าสุด', verbose_name='แก้ไขเมื่อ')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('guest', models.ForeignKey(blank=True, db_constraint=False, help_text='ลูกค้าที่ทำการจองห้องพัก', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='guests.guest', verbose_name='ลูกค้า')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, db_constraint=False, help_text='ห้องพักที่ลูกค้าทำการจอง', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='rooms.room', verbose_name='ห้องพัก')),
            ],
            options={
                'verbose_name': 'historical การจอง',
                'verbose_name_plural': 'historical การจอง',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPayment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('CASH', 'เงินสด'), ('CREDIT', 'บัตรเครดิต')], help_text='วิธีการชำระเงินที่ใช้ในการทำรายการ', max_length=50, verbose_name='ช่องทางการชำระเงิน')),
                ('amount_paid', models.DecimalField(decimal_places=2, help_text='จำนวนเงินที่ลูกค้าชำระ', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='จำนวนเงินที่ชำระ')),
                ('payment_date', models.DateTimeField(blank=True, editable=False, help_text='วันที่และเวลาที่ทำรายการชำระเงิน', verbose_name='วันที่ชำระเงิน')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('booking', models.ForeignKey(blank=True, db_constraint=False, help_text='การจองที่เกี่ยวข้องกับการชำระเงินนี้', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='bookings.booking', verbose_name='การจอง')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical การชำระเงิน',
                'verbose_name_plural': 'historical การชำระเงิน',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('CASH', 'เงินสด'), ('CREDIT', 'บัตรเครดิต')], help_text='วิธีการชำระเงินที่ใช้ในการทำรายการ', max_length=50, verbose_name='ช่องทางการชำระเงิน')),
                ('amount_paid', models.DecimalField(decimal_places=2, help_text='จำนวนเงินที่ลูกค้าชำระ', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='จำนวนเงินที่ชำระ')),
                ('payment_date', models.DateTimeField(auto_now_add=True, help_text='วันที่และเวลาที่ทำรายการชำระเงิน', verbose_name='วันที่ชำระเงิน')),
                ('booking', models.OneToOneField(help_text='การจองที่เกี่ยวข้องกับการชำระเงินนี้', on_delete=django.db.models.deletion.CASCADE, to='bookings.booking', verbose_name='การจอง')),
            ],
            options={
                'verbose_name': 'การชำระเงิน',
                'verbose_name_plural': 'การชำระเงิน',
                'ordering': ['-payment_date'],
            },
        ),
        migrations.AddIndex(
            model_name='booking',
            index=models.Index(fields=['guest'], name='bookings_bo_guest_i_05b863_idx'),
        ),
        migrations.AddIndex(
            model_name='booking',
            index=models.Index(fields=['room'], name='bookings_bo_room_id_2bee6f_idx'),
        ),
        migrations.AddConstraint(
            model_name='booking',
            constraint=models.CheckConstraint(condition=models.Q(('check_out__gt', models.F('check_in'))), name='check_out_gt_check_in'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['booking'], name='bookings_pa_booking_3a00cb_idx'),
        ),
    ]
