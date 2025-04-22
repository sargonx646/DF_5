from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_visuals(keywords):
    wc = WordCloud(width=800, height=400).generate(" ".join(keywords))
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("visualization.png", bbox_inches='tight')