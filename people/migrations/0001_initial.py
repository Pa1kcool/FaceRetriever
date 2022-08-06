# Generated by Django 4.0 on 2022-05-19 09:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MisingPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, unique=True, verbose_name='Given Name')),
                ('last_name', models.CharField(max_length=200, unique=True, verbose_name='Last Name')),
                ('age', models.CharField(blank=True, max_length=200, null=True, verbose_name='Age of Missing Person')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200, unique=True, verbose_name='Gender of Missing Person')),
                ('last_seen', models.CharField(max_length=200, unique=True, verbose_name='Last Seen Location')),
                ('description', models.TextField(max_length=1000, verbose_name='Any Other Important Details')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='missingpersons/', verbose_name='Upload Photo of Missing Person')),
                ('contact_person', models.CharField(max_length=200, unique=True, verbose_name='Contact Person')),
                ('contact_relationship', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Husband', 'Husband'), ('Wife', 'Wife'), ('Guardian', 'Guardian'), ('Relative', 'Relative'), ('Friend', 'Friend'), ('Other', 'Other')], max_length=200, unique=True, verbose_name='Relationship with Missing Person')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Contact Number')),
                ('status', models.CharField(choices=[('New', 'New'), ('Leads', 'Leads'), ('Found', 'Found'), ('Closed', 'Closed')], max_length=200, unique=True, verbose_name='Current Status')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
    ]