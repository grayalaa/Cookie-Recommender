"""Cookie recommender project for COGS 18."""


class Cookie:
    """Represent one cookie recipe option.

    Parameters
    ----------
    name : str
        Name of the cookie.
    description : str
        Short description of the cookie.
    traits : list of str
        Traits used for recommendation scoring.
    ingredients : list of str
        Ingredient list for the cookie.
    instructions : list of str
        Step-by-step baking instructions.
    """

    def __init__(self, name, description, traits, ingredients, instructions):
        self.name = name
        self.description = description
        self.traits = traits
        self.ingredients = ingredients
        self.instructions = instructions

    def matches_trait(self, trait):
        """Check whether the cookie has a specific trait.

        Parameters
        ----------
        trait : str
            Trait to check.

        Returns
        -------
        bool
            True if the cookie has the trait, otherwise False.
        """
        return trait in self.traits


def get_cookie_data():
    """Create and return all cookie options.

    Returns
    -------
    list of Cookie
        Five cookie objects used in the recommender.
    """
    # Create the five cookie options used by the recommender.
    return [
        Cookie(
            name="NYC Style Cookie",
            description=(
                "A thick, bakery-style cookie with a soft center and "
                "lots of chocolate."
            ),
            traits=["classic", "regular", "thick", "soft", "chocolatey"],
            ingredients=[
                "3 cups plus 2 tablespoons all-purpose flour",
                "1 teaspoon baking powder",
                "1/4 teaspoon baking soda",
                "1 1/2 teaspoons kosher salt",
                "1 cup unsalted butter, cold and cut into cubes",
                "3/4 cup plus 4 teaspoons light or dark brown sugar",
                "1/2 cup granulated sugar",
                "2 cold eggs, lightly beaten",
                "1 teaspoon vanilla extract",
                "2 cups dark chocolate chips",
            ],
            instructions=[
                "Line a large baking sheet with parchment paper.",
                "Mix flour, baking powder, baking soda, and salt.",
                "Beat cold butter until it comes together in one lump.",
                "Add sugars and beat until combined.",
                "Mix in eggs and vanilla.",
                "Add dry ingredients and fold in chocolate chips.",
                "Divide dough into 12 rough balls.",
                "Chill for at least 30 minutes.",
                "Bake at 375°F for 15 to 20 minutes.",
            ],
        ),
        Cookie(
            name="Brown Butter Cookie",
            description=(
                "A chewy cookie with nutty brown butter, caramelized flavor, "
                "and sea salt."
            ),
            traits=["classic", "regular", "thick", "chewy", "caramelized"],
            ingredients=[
                "3/4 cup unsalted butter",
                "1 cup packed light brown sugar",
                "1/4 cup granulated sugar",
                "1 large egg plus 1 large egg yolk",
                "1 tablespoon pure vanilla extract",
                "1 3/4 cups all-purpose flour",
                "3/4 teaspoon baking soda",
                "3/4 teaspoon kosher salt",
                "1 1/4 cups semisweet chocolate chips",
                "Flaky sea salt for sprinkling",
            ],
            instructions=[
                "Brown the butter over medium-low heat for 5 to 7 minutes.",
                "Let the brown butter cool for about 5 minutes.",
                "Mix brown butter, brown sugar, and granulated sugar.",
                "Add egg, egg yolk, and vanilla.",
                "Fold in flour, baking soda, and salt.",
                "Fold in chocolate chips.",
                "Chill dough for at least 1 hour.",
                "Scoop dough onto lined baking sheets.",
                "Bake at 350°F for 12 to 13 minutes.",
                "Sprinkle with flaky sea salt.",
            ],
        ),
        Cookie(
            name="Classic Chocolate Chip Cookie",
            description=(
                "A thinner, buttery chocolate chip cookie with a chewy texture."
            ),
            traits=["classic", "regular", "thin", "chewy", "buttery"],
            ingredients=[
                "1/2 cup salted butter, room temperature",
                "1 cup light brown sugar, packed",
                "1 large egg, room temperature",
                "1 teaspoon vanilla extract",
                "1 cup plus 3 tablespoons all-purpose flour",
                "1/2 teaspoon salt",
                "1/2 teaspoon baking soda",
                "1 teaspoon cornstarch",
                "1 cup bittersweet chocolate chips",
                "Coarse sea salt for topping",
            ],
            instructions=[
                "Preheat oven to 350°F.",
                "Mix butter and brown sugar.",
                "Mix in egg and vanilla.",
                "Combine flour, salt, baking soda, and cornstarch.",
                "Add dry ingredients to wet ingredients.",
                "Mix in chocolate chips.",
                "Scoop dough into 2 tablespoon balls.",
                "Top with extra chocolate chips.",
                "Bake for 10 to 14 minutes.",
            ],
        ),
        Cookie(
            name="Giant Chocolate Chip Cookie",
            description=(
                "A large, spread-out cookie with crisp edges and a chewy center."
            ),
            traits=["classic", "giant", "thin", "crispy edges", "buttery"],
            ingredients=[
                "2 cups all-purpose flour",
                "1 1/2 teaspoons baking soda",
                "1 teaspoon salt",
                "1 cup unsalted butter, room temperature",
                "1 cup granulated sugar",
                "3/4 cup packed light brown sugar",
                "2 large eggs",
                "2 teaspoons pure vanilla extract",
                "12 ounces chocolate chips",
            ],
            instructions=[
                "Preheat oven to 375°F.",
                "Whisk flour, baking soda, and salt.",
                "Beat butter and sugars until light and fluffy.",
                "Add eggs one at a time.",
                "Mix in vanilla.",
                "Add flour mixture on low speed.",
                "Stir in chocolate chips.",
                "Drop 1/4-cup mounds onto baking sheets.",
                "Bake for 15 to 18 minutes.",
            ],
        ),
        Cookie(
            name="Healthy Gluten-Free Cookie",
            description=(
                "A healthier gluten-free cookie made with almond meal, "
                "almond butter, maple syrup, and dark chocolate."
            ),
            traits=["healthy", "gluten-free", "regular", "soft", "nutty"],
            ingredients=[
                "1/2 cup creamy almond butter",
                "1/3 cup coconut oil, melted",
                "6 tablespoons maple syrup",
                "1 egg or flax egg",
                "2 teaspoons vanilla extract",
                "1 3/4 cups almond meal",
                "1/2 teaspoon baking soda",
                "1/2 teaspoon salt",
                "1 1/2 cups dark chocolate chips",
            ],
            instructions=[
                "Mix almond butter, coconut oil, maple syrup, egg, and vanilla.",
                "Add almond meal, baking soda, and salt.",
                "Fold in dark chocolate chips.",
                "Chill dough for at least 1 hour.",
                "Preheat oven to 350°F.",
                "Scoop dough onto parchment-lined baking sheet.",
                "Bake for 10 to 12 minutes.",
                "Cool before serving.",
            ],
        ),
    ]


def validate_choice(choice, valid_choices):
    """Check whether a user's choice is valid.

    Parameters
    ----------
    choice : str
        User's input.
    valid_choices : list of str
        Allowed input options.

    Returns
    -------
    bool
        True if the choice is valid, otherwise False.
    """
    return choice in valid_choices


def ask_question(question, choices):
    """Ask a multiple-choice question until the user enters a valid choice.

    Parameters
    ----------
    question : str
        Question shown to the user.
    choices : dict
        Dictionary where keys are choice numbers and values are traits.

    Returns
    -------
    str
        Trait connected to the user's valid choice.
    """
    print(question)

    for number, option in choices.items():
        print(f"{number}. {option}")

    choice = input("\nEnter the number of your choice: ")

    # Keep asking until the user enters one of the listed numbers.
    while not validate_choice(choice, list(choices.keys())):
        print("Invalid choice. Please enter one of the listed numbers.")
        choice = input("Enter the number of your choice: ")

    return choices[choice]


def calculate_score(cookie, preferences):
    """Calculate how many user preferences match a cookie.

    Parameters
    ----------
    cookie : Cookie
        Cookie being scored.
    preferences : list of str
        User's selected preferences.

    Returns
    -------
    int
        Number of matching traits.
    """
    score = 0

    # Count one point for each user preference that matches the cookie.
    for preference in preferences:
        if cookie.matches_trait(preference):
            score += 1

    return score


def recommend_cookie(cookies, preferences):
    """Recommend the highest-scoring cookie.

    Parameters
    ----------
    cookies : list of Cookie
        Cookie options.
    preferences : list of str
        User's selected preferences.

    Returns
    -------
    tuple
        Best matching Cookie object and its score.
    """
    best_cookie = cookies[0]
    best_score = calculate_score(best_cookie, preferences)

    for cookie in cookies[1:]:
        score = calculate_score(cookie, preferences)

        if score > best_score:
            best_cookie = cookie
            best_score = score

    return best_cookie, best_score


def get_matching_traits(cookie, preferences):
    """Find which traits matched between the user and cookie.

    Parameters
    ----------
    cookie : Cookie
        Recommended cookie.
    preferences : list of str
        User's selected preferences.

    Returns
    -------
    list of str
        Matching traits.
    """
    matches = []

    for preference in preferences:
        if cookie.matches_trait(preference):
            matches.append(preference)

    return matches


def format_recommendation(cookie, score, preferences):
    """Create a readable recommendation message.

    Parameters
    ----------
    cookie : Cookie
        Recommended cookie.
    score : int
        Match score.
    preferences : list of str
        User's selected preferences.

    Returns
    -------
    str
        Formatted recommendation message.
    """
    matching_traits = get_matching_traits(cookie, preferences)
    trait_text = "\n".join(f"- {trait}" for trait in matching_traits)

    return (
        f"\nYour Cookie Match: {cookie.name}\n\n"
        f"Match Score: {score}/{len(preferences)}\n\n"
        f"{cookie.description}\n\n"
        f"Why we chose it:\n{trait_text}"
    )


def display_recipe(cookie):
    """Print a cookie's ingredients and instructions.

    Parameters
    ----------
    cookie : Cookie
        Cookie recipe to display.

    Returns
    -------
    None
        Prints recipe information.
    """
    print(f"\nRecipe for {cookie.name}\n")

    print("Ingredients:")
    for ingredient in cookie.ingredients:
        print(f"- {ingredient}")

    print("\nInstructions:")
    for number, instruction in enumerate(cookie.instructions, start=1):
        print(f"{number}. {instruction}")


def handle_after_recommendation(cookie):
    """Let the user choose what to do after a recommendation.

    Parameters
    ----------
    cookie : Cookie
        Recommended cookie.

    Returns
    -------
    str
        User's next action.
    """
    choices = {
        "1": "view recipe",
        "2": "get another recommendation",
        "3": "exit",
    }

    action = ask_question(
        "\nWhat would you like to do next?",
        choices,
    )

    if action == "view recipe":
        display_recipe(cookie)

    return action


def run_cookie_quiz():
    """Run the full cookie recommendation quiz.

    Returns
    -------
    None
        Runs the interactive program.
    """
    cookies = get_cookie_data()
    keep_running = True

    print("Welcome to the Cookie Recommender!")

    while keep_running:
        craving = ask_question(
            "\nWhich best describes what you're craving today?",
            {
                "1": "classic indulgent cookie",
                "2": "healthy gluten-free cookie",
            },
        )

        # Automatically recommend the healthy gluten-free option.
        if craving == "healthy gluten-free cookie":
            preferences = ["healthy", "gluten-free"]
            cookie = cookies[-1]
            score = calculate_score(cookie, preferences)
        else:
            preferences = ["classic"]

            size = ask_question(
                "\nWhat size cookie sounds best?",
                {
                    "1": "giant",
                    "2": "regular",
                },
            )
            preferences.append(size)

            thickness = ask_question(
                "\nWhich thickness do you prefer?",
                {
                    "1": "thick",
                    "2": "thin",
                },
            )
            preferences.append(thickness)

            texture = ask_question(
                "\nWhich texture sounds best?",
                {
                    "1": "soft",
                    "2": "chewy",
                    "3": "crispy edges",
                },
            )
            preferences.append(texture)

            flavor = ask_question(
                "\nWhich flavor profile sounds most appealing?",
                {
                    "1": "chocolatey",
                    "2": "buttery",
                    "3": "caramelized",
                },
            )
            preferences.append(flavor)

            cookie, score = recommend_cookie(cookies, preferences)

        print(format_recommendation(cookie, score, preferences))

        action = handle_after_recommendation(cookie)

        if action != "get another recommendation":
            keep_running = False

    print("\nThanks for using the Cookie Recommender. Happy baking!")