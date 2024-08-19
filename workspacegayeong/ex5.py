import  wikipedia
# wiki=wikipedia.page('Artificial Intelligence')
# text=wiki.content
# print(text)
text="the soft part containing seeds that is produced by a plant. Many types of fruit are sweet and can be eaten, Apricots are the one fruit I don't like.,"
print(text)
from wordcloud import WordCloud
wd=WordCloud(width =2000, height = 1500).generate(text)


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wd)
plt.show()