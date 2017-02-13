from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ModelTranslationDBConfig(AppConfig):
    name = 'modeltranslation_db'
    verbose_name = _("ModelTranslation DB")
