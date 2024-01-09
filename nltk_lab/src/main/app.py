from src.main.lab import sampleNormalization, sampleTokenization,tokenizationExercise, normalizationExercise, sampleStopwordRemoval, sampleFindAll, findAllExercise
import nltk

if __name__ == '__main__':
    nltk.download('popular')

    print(sampleNormalization())
    print(normalizationExercise(''))

    print(sampleTokenization())
    print(tokenizationExercise(''))

    print(sampleStopwordRemoval())

    print(sampleFindAll())
    print(findAllExercise())