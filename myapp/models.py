from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    name = models.CharField(max_length=255)
    title = models.JSONField(default=dict, blank=True, null=True)

    LANGUAGES = [(lang_code, _(lang_name)) for lang_code, lang_name in settings.LANGUAGES]
    default_language = models.CharField(max_length=7, choices=LANGUAGES, default=settings.LANGUAGE_CODE)

    def get_data_field(self, field_name):
        return self.data.get(field_name)

    def set_data_field(self, field_name, value):
        self.data[field_name] = value
        self.save()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.default_language:
            raise ValidationError(_("Default language field is required"))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
