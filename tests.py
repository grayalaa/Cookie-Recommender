"""Unit tests for the cookie recommender project."""

import unittest

import module


class TestCookieRecommender(unittest.TestCase):
    """Test the Cookie Recommender project."""

    def test_cookie_class_stores_attributes(self):
        cookie = module.Cookie(
            name="Test Cookie",
            description="A cookie used for testing.",
            traits=["soft", "chocolatey"],
            ingredients=["flour", "sugar"],
            instructions=["Mix.", "Bake."],
        )

        self.assertEqual(cookie.name, "Test Cookie")
        self.assertIn("soft", cookie.traits)
        self.assertIn("flour", cookie.ingredients)

    def test_validate_choice_accepts_valid_choice(self):
        self.assertTrue(module.validate_choice("1", ["1", "2", "3"]))

    def test_calculate_score_counts_matching_traits(self):
        cookie = module.Cookie(
            name="Chocolate Cookie",
            description="A chocolate cookie.",
            traits=["regular", "soft", "chocolatey"],
            ingredients=[],
            instructions=[],
        )

        preferences = ["regular", "soft", "buttery"]
        score = module.calculate_score(cookie, preferences)

        self.assertEqual(score, 2)

    def test_recommend_cookie_returns_nyc_style_cookie(self):
        cookies = module.get_cookie_data()
        preferences = ["classic", "regular", "thick", "soft", "chocolatey"]

        cookie, score = module.recommend_cookie(cookies, preferences)

        self.assertEqual(cookie.name, "NYC Style Cookie")
        self.assertEqual(score, 5)

    def test_get_matching_traits(self):
        cookie = module.Cookie(
            name="Test Cookie",
            description="A test cookie.",
            traits=["soft", "chocolatey"],
            ingredients=[],
            instructions=[],
        )

        preferences = ["soft", "thin", "chocolatey"]
        matches = module.get_matching_traits(cookie, preferences)

        self.assertEqual(matches, ["soft", "chocolatey"])


if __name__ == "__main__":
    unittest.main()
##
##



                 
    