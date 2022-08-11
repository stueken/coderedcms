# Generated by Django 4.0.7 on 2022-08-10 20:37

from django.db import migrations, models


def copy_settings(apps, schema_editor):
    LayoutSettings = apps.get_model("coderedcms", "LayoutSettings")
    GeneralSettings = apps.get_model("coderedcms", "GeneralSettings")
    GoogleApiSettings = apps.get_model("coderedcms", "GoogleApiSettings")
    MailchimpApiSettings = apps.get_model("coderedcms", "MailchimpApiSettings")
    for s in LayoutSettings.objects.all():
        gen = GeneralSettings.objects.filter(site=s.site).first()
        goog = GoogleApiSettings.objects.filter(site=s.site).first()
        mc = MailchimpApiSettings.objects.filter(site=s.site).first()
        if gen:
            s.external_new_tab = gen.external_new_tab
            s.from_email_address = gen.from_email_address
            s.search_num_results = gen.search_num_results
        if goog:
            s.google_maps_api_key = goog.google_maps_api_key
        if mc:
            s.mailchimp_api_key = mc.mailchimp_api_key
        s.save()


class Migration(migrations.Migration):

    dependencies = [
        ('coderedcms', '0034_delete_adasettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layoutsettings',
            options={'verbose_name': 'CRX Settings'},
        ),
        migrations.AddField(
            model_name='layoutsettings',
            name='external_new_tab',
            field=models.BooleanField(default=False, verbose_name='Open all external links in new tab'),
        ),
        migrations.AddField(
            model_name='layoutsettings',
            name='from_email_address',
            field=models.CharField(blank=True, help_text='The default email address this site appears to send from. For example: "sender@example.com" or "Sender Name <sender@example.com>" (without quotes)', max_length=255, verbose_name='From email address'),
        ),
        migrations.AddField(
            model_name='layoutsettings',
            name='google_maps_api_key',
            field=models.CharField(blank=True, help_text='The API Key used for Google Maps.', max_length=255, verbose_name='Google Maps API Key'),
        ),
        migrations.AddField(
            model_name='layoutsettings',
            name='mailchimp_api_key',
            field=models.CharField(blank=True, help_text='The API Key used for Mailchimp.', max_length=255, verbose_name='Mailchimp API Key'),
        ),
        migrations.AddField(
            model_name='layoutsettings',
            name='search_num_results',
            field=models.PositiveIntegerField(default=10, verbose_name='Number of results per page'),
        ),

        # Copy the settings over.
        migrations.RunPython(copy_settings),

        # Delete the old fields and models.
        migrations.RemoveField(
            model_name='generalsettings',
            name='site',
        ),
        migrations.RemoveField(
            model_name='googleapisettings',
            name='site',
        ),
        migrations.RemoveField(
            model_name='mailchimpapisettings',
            name='site',
        ),
        migrations.DeleteModel(
            name='GeneralSettings',
        ),
        migrations.DeleteModel(
            name='GoogleApiSettings',
        ),
        migrations.DeleteModel(
            name='MailchimpApiSettings',
        ),
    ]
