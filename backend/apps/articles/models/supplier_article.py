from django.db import models

from apps.core.models import UserTrackingModel
from apps.supplier.models import Supplier
from .article import Article


# Model
class SupplierArticle(UserTrackingModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='supplier_articles',
                                verbose_name='Article', help_text='Article of the supplier article')

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_articles',
                                 verbose_name='Supplier', help_text='Supplier of the supplier article')

    class Meta:
        ordering = ['article']
        verbose_name = 'Supplier article'
        verbose_name_plural = 'Supplier articles'
        indexes = [
            models.Index(fields=['article'])
        ]

    def __str__(self):
        return f'{self.article.title} - {self.supplier.name}'
