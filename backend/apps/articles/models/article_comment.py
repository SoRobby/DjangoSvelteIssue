from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from config import settings
from django.db import models

from .article import Article


# Models
class ArticleComment(UserTrackingModel, SoftDeletionWithUserModel):
    """
    Represents a comment on an article.

    Inherits from UserTrackingModel and SoftDeletionWithUserModel.

    Attributes:
        article (ForeignKey): The article that the comment belongs to.
        user (ForeignKey): The user who made the comment.
        parent (ForeignKey): The parent comment if this comment is a reply.
        content (TextField): The content of the comment.
        up_votes (ManyToManyField): Users who up voted the comment.
        down_votes (ManyToManyField): Users who down voted the comment.
        is_edited (BooleanField): Indicates if the comment has been edited.
        is_flagged (BooleanField): Indicates if the comment has been flagged.

    Meta:
        ordering (list): The default ordering of comments based on date_created.
        verbose_name (str): The singular name of the model.
        verbose_name_plural (str): The plural name of the model.
        indexes (list): Indexes to be created for the model.

    Methods:
        __str__(): Returns a string representation of the comment.
    """

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Article',
                                help_text='Article of the comment')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments',
                             verbose_name='User', help_text='User of the comment')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True,
                               verbose_name='Parent', help_text='Parent of the comment')

    content = models.TextField(max_length=6000, verbose_name='Content', help_text='Content of the comment')

    up_votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='up_voted_comments', blank=True,
                                      verbose_name='Up votes', help_text='Users who up voted the comment')

    down_votes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='down_voted_comments', blank=True,
                                        verbose_name='Down votes', help_text='Users who down voted the comment')

    is_edited = models.BooleanField(default=False, verbose_name='Is edited', help_text='Is the comment edited')

    is_flagged = models.BooleanField(default=False, verbose_name='Is flagged', help_text='Is the comment flagged')

    class Meta:
        ordering = ['date_created']
        verbose_name = 'Article comment'
        verbose_name_plural = 'Article comments'
        indexes = [
            models.Index(fields=['article'])
        ]

    def __str__(self):
        return f'{self.article.title} - {self.user.name} ({self.id})'
