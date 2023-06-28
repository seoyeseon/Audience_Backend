from django.db import models

# Create your models here.
class Comment(models.Model):
    postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)
    userable = models.ForeignKey('employ.Userable', on_delete=models.CASCADE)

class Reply(models.Model):
    postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)
    userable = models.ForeignKey('employ.Userable', on_delete=models.CASCADE)
    comment = models.ForeignKey('comment.Comment', on_delete=models.CASCADE)
