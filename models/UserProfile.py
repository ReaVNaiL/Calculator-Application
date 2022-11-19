class UserProfile:
    score = 0
    problem_count = 0
    max_difficulty = "easy"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (
            "Name: "
            + self.name
            + ", Age: "
            + str(self.age)
            + ", Score: "
            + str(self.score)
        )

    def __repr__(self):
        return f"Profile({self.name}, {self.age}):\n Score: {self.score}\n  Problem Count: {self.problem_count}\n  Max Difficulty: {self.max_difficulty}"

    def update_score(self, score):
        self.score = score
