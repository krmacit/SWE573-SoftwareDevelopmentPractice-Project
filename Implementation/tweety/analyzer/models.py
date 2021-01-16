from django.db import models


class TweetSummary(models.Model):
    tweet_id = models.BigIntegerField()
    entity = models.CharField(max_length=100)
    date = models.DateField()
    semantic_neg = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    semantic_neu = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    semantic_pos = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    semantic_compound = models.DecimalField(null=True, max_digits=6, decimal_places=4)
    location = models.CharField(max_length=5, null=True)
    country_code = models.CharField(null=True, max_length=3)
