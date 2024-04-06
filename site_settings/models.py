from django.db import models
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
# from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.fields import RichTextField
# from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)


@register_setting
class SiteSettings(BaseSiteSetting):
    author_name = models.CharField(max_length=128)
    favicon = models.ForeignKey('wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+')
    copyright_text = RichTextField()

    panels = [
        FieldPanel("author_name"),
        FieldPanel('favicon'),
        FieldPanel("copyright_text"),
    ]


@register_setting
class GoogleAnalyticsSettings(BaseSiteSetting):
    analytics_code = models.TextField(blank=True, null=True, help_text='Your analytics tracking code')

    panels = [
        FieldPanel('analytics_code'),
    ]


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    zoom = models.CharField(max_length=255, blank=True, null=True, help_text='Please, enter your skype name.')

    panels = [
        MultiFieldPanel([
            FieldPanel('linkedin'),
            FieldPanel('github'),
            FieldPanel('zoom'),
            FieldPanel('instagram'),
        ], heading="Social Media Settings"),
    ]
