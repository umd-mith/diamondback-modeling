#!/usr/bin/env python

import os
import re
import json
import codecs
import string
import argparse

from stopwords import stopwords
from glob import iglob
from gensim import corpora, models

def articles():
    i = 0
    for filename in iglob("extractedArticles/**/*.txt", recursive=True):
        w = words(filename)
        if 'freedom' in w:
            yield w
            if i > 100:
                break
            i += 1

def words(filename):
    text = codecs.open(filename, 'r', 'utf8').read().lower()
    return [w for w in re.split(r'\W+', text) if w]

def remove_stopwords(sources):
    def f():
        for doc in sources():
            new_doc = []
            for word in doc:
                if len(word) > 3 and word.lower() not in stopwords:
                    new_doc.append(word)
            yield new_doc
    return f

def get_corpus(dictionary):
    def ids():
        for doc in articles():
            yield dictionary.doc2bow(doc)
    path = "corpus.mm"
    corpora.MmCorpus.serialize(path, ids())
    corpus = corpora.MmCorpus(path)
    return corpus

def topics(sources=articles, num_words=5, num_topics=5, passes=10, iterations=50, ignore=False):

    if ignore:
        sources = remove_stopwords(sources)

    dictionary = corpora.Dictionary(sources())
    corpus = get_corpus(dictionary)

    lda = models.ldamodel.LdaModel(
        corpus, 
        id2word=dictionary,
        num_topics=num_topics,
        passes=passes,
        iterations=iterations
    )

    topics = lda.top_topics(corpus, topn=num_words)

    num = 0
    for topic in topics:
        num += 1
        print("%s. %s" % (num, ', '.join([t[1] for t in topic[0]])))

if __name__ == "__main__":
    print(topics(articles, num_topics=20, ignore=True, passes=20))
