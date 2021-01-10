import os
from os.path import dirname

import matplotlib.pyplot as plt
from wordcloud import WordCloud

from twitter.models import Entities


def generate_worldcloud():
    values = Entities.objects.values("normalized_text")
    result = [value["normalized_text"] for value in values]
    wordcloud = WordCloud(width=480, height=480, colormap="Blues").generate(' '.join(result))
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
    my_path = os.path.abspath(__file__)
    plt.savefig(dirname(dirname(my_path)) + "/static/wordcloud.jpg")
