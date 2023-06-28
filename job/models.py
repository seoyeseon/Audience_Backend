from django.db import models

# Create your models here.
class Job_post(models.Model):
    image = models.ImageField(upload_to='uploads/')
    postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)
    userable = models.ForeignKey('employ.Userable', on_delete=models.CASCADE)

class Freepost(models.Model):
    postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)

class report(models.Model):
    CONTENT_CHOICES = (('a','신고 사유 선택'),('b','사기/도배'),('c','욕설/비하'))
    content = models.CharField(max_length=1, default='a', choices=CONTENT_CHOICES)
    postable = models.ForeignKey('employ.Postable', on_delete=models.CASCADE)

