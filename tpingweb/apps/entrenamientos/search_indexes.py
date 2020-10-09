from haystack import indexes
from apps.entrenamientos.models import *

class runningteamIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nombre_runningteam = indexes.CharField(model_attr='nombre_runningteam')
    url_logo = indexes.CharField()

    def preparar_logo_url(self, obj):
       return obj.image_field.path

    def get_model(self):
        return runningteam

    def index_queryset(self, using=None):
        """Queremos que se indexen todos los running teams"""
        return self.get_model().objects.all().select_related()