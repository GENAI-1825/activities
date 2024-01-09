import unittest
import nltk
from src.main.lab import normalizationExercise,tokenizationExercise,findAllExercise

class TestNLTKExercises(unittest.TestCase):
    def test_normalization_exercise(self):
        test = "kool kitties"
        expectation = "KOOL KITTIES"

        result = normalizationExercise(test)

        self.assertEqual(expectation,result)

    def test_normalization_exercise_2(self):
        test = "F@ll"
        expectation = "FLL"

        result = normalizationExercise(test)

        self.assertEqual(expectation,result)

    def test_normalization_exercise_3(self):
        test = "Fr33z3r #@$ brr"
        expectation = "FR33Z3R  BRR"

        result = normalizationExercise(test)

        self.assertEqual(expectation,result)

    def test_tokenization_exercise(self):
        test = "Hello World!"
        word_tokens_expectation = ["Hello", "World", "!"]
        sent_tokens_expectation = ["Hello World!"]
        expectation = {"words":word_tokens_expectation, "sents": sent_tokens_expectation}

        result = tokenizationExercise(test)
        
        self.assertEqual(expectation, result)

    def test_findAllExercise(self):
        expectation = "wounded; great; great; mighty; sperm; sperm; sperm; Norwegian;wondrous; American; American; sperm; dying; Greenland; Greenland; Greenland; Greenland; sperm; sperm; entire; Trumpa; Physeter; Sperm; Greenland; right; sperm; right; right; sperm; humpbacked; Greenland; Greenland; Greenland; sperm; sperm; Hyena; Tusked; Horned; Unicorn; Folio; white; white; white; white; white; white; white; white; white; Albino; sperm; sperm; entire; sperm; sperm; white; white; sperm; sperm; sperm; sperm; sperm; right; sperm; English; snowy; true; Right; stranded; living; Greenland; boiling; foremost; particular; sperm; spermaceti; sperm; stricken; sperm; waning; same; heaving; tremendous; great; beheaded; mightiest; great; sperm; dead; towing; fagged; sperm; right; sperm; sperm; stricken; wounded; sunken; sunken; first; stricken; flying; towing; whole; sperm; towing; unborn; stricken; schoolmaster; controverted; drugged; other; blasted; other; lighter; Dutch; slack; stricken; sperm; white; other; adult; last; hunted; great; eternal; living; last; dead; dead; stricken; white; famous; white; gliding; sperm; white; white; white; white; hated; before; stricken"

        result = findAllExercise()

        self.assertEqual(expectation,result)
        
if __name__ == '__main__':
    nltk.download('popular')
    unittest.main()