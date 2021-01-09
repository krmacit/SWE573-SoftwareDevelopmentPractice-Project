from django.db import models


class Tweet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author_id = models.ForeignKey("User", on_delete=models.CASCADE)
    like_count = models.IntegerField()
    quote_count = models.IntegerField()
    reply_count = models.IntegerField()
    retweet_count = models.IntegerField()
    text = models.CharField(max_length=400)


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)


class ContextAnnotation(models.Model):
    tweet_id = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    domain_description = models.CharField(max_length=50)
    domain_id = models.BigIntegerField()
    domain_name = models.CharField(max_length=50)
    entity_description = models.CharField(max_length=50)
    entity_id = models.BigIntegerField()
    entity_name = models.CharField(max_length=50)


class EntityAnnotation(models.Model):
    tweet_id = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    start_char = models.IntegerField()
    end_char = models.IntegerField()
    probability = models.DecimalField(null=True, decimal_places=4)
    type = models.CharField(max_length=50)
    normalized_text = models.CharField(max_length=100)
