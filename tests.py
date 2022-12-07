import unittest

import movies


class UnitTests(unittest.TestCase):
    def test_print(self):
        movie = movies.TMDB(18)

        self.assertEqual(
            str(movie),
            "The Fifth Element",
            "Expected title of the movie with id 18 in TMDB.",
        )


if __name__ == "__main__":
    unittest.main()
