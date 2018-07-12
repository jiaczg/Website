import datetime
from .models import Blog
from haystack import indexes


class SeekIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        # 当模型的整个索引被更新时使用
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())