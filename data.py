import requests


QUIZ_CATEGORY = [
    {0: 'Any Category'},
    {9: 'General Knowledge'},
    {10: 'Entertainment: Books'},
    {11: 'Entertainment: Film'},
    {12: 'Entertainment: Music'},
    {13: 'Entertainment: Musicals and Theatres'},
    {14: 'Entertainment: Television'},
    {15: 'Entertainment: Video Games'},
    {16: 'Entertainment: Board Games'},
    {17: 'Science and Nature'},
    {18: 'Science: Computers'},
    {19: 'Science: Mathematics'},
    {20: 'Mythology'},
    {21: 'Sports'},
    {22: 'Geography'},
    {23: 'History'},
    {24: 'Politics'},
    {25: 'Art'},
    {26: 'Celebrities'},
    {27: 'Animals'},
    {28: 'Vehicles'},
    {29: 'Entertainment'},
    {30: 'Science: Gadgets'},
    {31: 'Entertainment: Japanese Anime and Manga'},
    {32: 'Entertainment: Cartoon and Animations'},
]


# check if variable is valid number
def is_valid_number(variable):
    try:
        int(variable)
        return True
    except ValueError:
        return False


def get_user_inputs():
    while True:
        amount = input("Number of Questions (1-30): ")
        if not is_valid_number(amount):
            print("Invalid input!")
        elif int(amount) > 31 or int(amount) < 0:
            print("Value must be 1-30 only.")
        else:
            break

    for q_category in QUIZ_CATEGORY:
        for cid, cname in q_category.items():
            print(f"Select {cid} for {cname}")

    while True:
        category = input("Select Category: ")
        if not is_valid_number(category) or int(category) not in [key for quiz_dic in QUIZ_CATEGORY for key in quiz_dic]:
            print('Invalid input!')
        else:
            break

    print("\n")

    return {
        'amount': amount,
        'category': category
    }


class QuizData:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

    def create_quiz_data(self):

        if self.category == 0:
            url = f"https://opentdb.com/api.php?amount={self.amount}&type=boolean"
        else:
            url = f"https://opentdb.com/api.php?amount={self.amount}&category={self.category}&type=boolean"

        response = requests.get(url)
        json_data = response.json()

        return json_data['results']
