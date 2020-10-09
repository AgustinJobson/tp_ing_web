from haystack import indexes
from apps.entrenamientos.models import *

class runningteamIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nombre_runningteam = indexes.CharField(model_attr='nombre_runningteam')

    def get_model(self):
        return runningteam

    def index_queryset(self, using=None):
        """Queremos que se indexen todos los running teams"""
        return self.get_model().objects.all().select_related()