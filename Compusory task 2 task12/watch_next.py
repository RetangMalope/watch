import spacy
import numpy as np

def get_similar_movie(description):
    nlp = spacy.load('en_core_web_lg')

    input_vector = nlp(description).vector

    max_similarity = -1
    most_similar_movie = ''

    with open('C:/Users/RMalope/Downloads/movies (1).txt', 'r') as file:
        for line in file:
            movie_title, movie_description = line.strip().split(':')
            movie_vector = nlp(movie_description).vector
            similarity = np.dot(input_vector, movie_vector) / (np.linalg.norm(input_vector) * np.linalg.norm(movie_vector))

            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_movie = movie_title

    return most_similar_movie

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

most_similar_movie = get_similar_movie(description)
print("You should watch:", most_similar_movie)


