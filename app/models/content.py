from time import timezone

from django.db import models
from .chapter import Chapter


class Content(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    chapter_name = models.ForeignKey(Chapter, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    @staticmethod
    def get_all_contents():
        return Content.objects.all()

    @staticmethod
    def get_all_contents_by_id(chapter_id):
        if chapter_id:
            return Content.objects.filter(chpter=chapter_id)
        else:
            return Content.get_all_contents()
