from django.db import models


class Chapter(models.Model):
    chapter_name = models.CharField(max_length=150)

    def __str__(self):
        return self.chapter_name

    @staticmethod
    def get_all_chapter():
        return Chapter.objects.all()
