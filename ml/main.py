import numpy as np
import pandas as pd
from joblib import dump
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from ml import cutoff


def main(filename: str):
    df = pd.read_csv('data/filename', names=['message', 'label'])

    messages = df['message'].values
    labels = df['label'].values

    messages_train, messages_test, y_train, y_test = train_test_split(messages, labels, random_state=1000)

    # Use the first <cutoff> characters to not bias towards shorter messages
    messages_train = [np.str_(str(x)[:cutoff]) for x in messages_train]
    messages_test = [np.str_(str(x)[:cutoff]) for x in messages_test]

    vectorizer = CountVectorizer()
    vectorizer.fit(messages_train)

    x_train = vectorizer.transform(messages_train)
    x_test = vectorizer.transform(messages_test)

    classifier = LogisticRegression()
    classifier.fit(x_train, y_train)
    score = classifier.score(x_test, y_test)

    print(f'Accuracy for data: {score:.4f}')

    dump(classifier, 'overwatch_messages.model')
    dump(vectorizer, 'overwatch_messages.vectorizer')


if __name__ == '__main__':
    main(filename='2020-12-13-to-2021-2-13-data-even.csv')
