from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail

class BlogType(models.Model):
    type_name = models.CharField(max_length=15, verbose_name='分类列表')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural  = verbose_name

class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name='文章分类')
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    lsat_updated_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客文章'
        verbose_name_plural = verbose_name