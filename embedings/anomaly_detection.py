import base64
import re
from dotenv import load_dotenv
import google.generativeai as genai
import os
from sklearn.datasets import fetch_20newsgroups
from sklearn.manifold import TSNE
import pandas as pd
load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))


# WIP im trying to understand how this works i need to do it locally not in Colab
# https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/tutorials/anomaly_detection.ipynb


def find_embedding_model():
    for m in genai.list_models():
        if 'embedContent' in m.supported_generation_methods:
            return m.name


if __name__ == "__main__":
    model_name = find_embedding_model()
    print(model_name)

    newsgroups_train = fetch_20newsgroups(subset='train')

    # Check a list of class names for dataset
    print(newsgroups_train.target_names)

    idx = newsgroups_train.data[0].index('Lines')
    print(newsgroups_train.data[0][idx:])

    # data clean up
    # Apply functions to remove names, emails, and extraneous words from data points in newsgroups.data
    # Apply functions to remove names, emails, and extraneous words from data points in newsgroups.data
    newsgroups_train.data = [re.sub(r'[\w\.-]+@[\w\.-]+', '', d) for d in newsgroups_train.data]  # Remove email
    newsgroups_train.data = [re.sub(r"\(.*?\)", "", d) for d in newsgroups_train.data] # Remove names
    newsgroups_train.data = [d.replace("From: ", "") for d in newsgroups_train.data]  # Remove "From: "
    newsgroups_train.data = [d.replace("\nSubject: ", "") for d in newsgroups_train.data]  # Remove "\nSubject: "

    # Cut off each text entry after 5,000 characters
    newsgroups_train.data = [d[0:5000] if len(d) > 5000 else d for d in newsgroups_train.data]

    # Put training points into a dataframe
    df_train = pd.DataFrame(newsgroups_train.data, columns=['Text'])
    df_train['Label'] = newsgroups_train.target
    # Match label to target name index
    df_train['Class Name'] = df_train['Label'].map(newsgroups_train.target_names.__getitem__)



    # Take a sample of each label category from df_train
    SAMPLE_SIZE = 150
    df_train = (df_train.groupby('Label', as_index=False)
                .apply(lambda x: x.sample(SAMPLE_SIZE))
                .reset_index(drop=True))

    # Choose categories about science
    df_train = df_train[df_train['Class Name'].str.contains('sci')]

    # Reset the index
    df_train = df_train.reset_index()
    print(df_train)

    df_train['Class Name'].value_counts()
