from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_model(df):

    tfidf = TfidfVectorizer(
        stop_words="english"
    )

    matrix = tfidf.fit_transform(
        df["ingredients"].astype(str)
    )

    similarity = cosine_similarity(
        matrix
    )

    return similarity


def recommend(recipe_name, df, similarity):

    indices = pd.Series(
        df.index,
        index=df["title"]
    ).drop_duplicates()

    if recipe_name not in indices:
        return None

    idx = indices[recipe_name]

    scores = list(
        enumerate(similarity[idx])
    )

    scores = sorted(
        scores,
        key=lambda x:x[1],
        reverse=True
    )

    recipe_indices = [
        i[0]
        for i in scores[1:6]
    ]

    return df.iloc[recipe_indices]
