from django.db import models


class TweetSummary(models.Model):
    tweet_id = models.BigIntegerField()
    entity = models.CharField(max_length=100)
    date = models.DateField()
    semantic_neg = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    semantic_neu = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    semantic_pos = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    semantic_compound = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    location = models.CharField(max_length=50, null=True)
    country_code = models.CharField(null=True, max_length=3)
    country = models.CharField(null=True, max_length=25)
    continent = models.CharField(null=True, max_length=15)


class FinalTable(models.Model):
    region = models.CharField(null=True, max_length=25)
    entity = models.CharField(max_length=100)
    date = models.DateField()
    semantic_compound = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    tweet_count = models.IntegerField(default=0)


class FinalTableAll(models.Model):
    entity = models.CharField(max_length=100)
    date = models.CharField(max_length=30)
    semantic_compound = models.DecimalField(null=True, max_digits=6, decimal_places=5)
    tweet_count = models.IntegerField(default=0)
