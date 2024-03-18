import sys
from diarybook import Diary, DiaryBook
from util import read_from_json_into_application

class Menu:

    def __init__(self):
        self.diarybook = DiaryBook()
        self.logged_in_user = None

        self.choices = {
            "1": self.show_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.populate_database,
            '5': self.quit,
            "6": self.sorting,
            "7": self.login,
            "8": self.register
        }

    def display_menu(self):
        print(""" 
                    Notebook Menu  
            1. Show diaries
            2. Add diary
            3. Search diaries
            4. Populate database
            5. Quit program
            6. Sort the diaries
            7. Login
            8. Register
                """)

    def run(self):
        while True:
            if self.logged_in_user:
                print(f"Logged in as: {self.logged_in_user}")
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_diaries(self, diaries=None):
        if not diaries:
            diaries = self.diarybook.diaries
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

    def add_diary(self):
        if not self.logged_in_user:
            print("Please login first.")
            return
        memo = input("Enter a memo:     ")
        tags = input("add tags:      ")
        self.diarybook.new_diary(memo, tags, self.logged_in_user)
        print("Your note has been added")

    def search_diaries(self):
        if not self.logged_in_user:
            print("Please login first.")
            return
        filter_text = input("Search for:  ")
        diaries = self.diarybook.search_diary(filter_text, self.logged_in_user)
        for diary in diaries:
            print(f"{diary.id}-{diary.memo}")

    def quit(self):
        print("Thank you for using diarybook today")
        sys.exit(0)

    def populate_database(self):
        diaries1 = read_from_json_into_application('data.json')
        for diary in diaries1:
            self.diarybook.diaries.append(diary)

    def sorting(self):
        if not self.logged_in_user:
            print("Please login first.")
            return
        n = len(self.diarybook.diaries)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.diarybook.diaries[j].id < self.diarybook.diaries[min_idx].id:
                    min_idx = j
            self.diarybook.diaries[i], self.diarybook.diaries[min_idx] = self.diarybook.diaries[min_idx], self.diarybook.diaries[i]
        self.show_diaries()

    def login(self):
        username = input("Enter your usernae: ")
        password = input("Enter your password:")
        with open('users.txt', 'r') as file:
            users = file.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(',')
                if stored_username == username and stored_password == password:
                    self.logged_in_user = username
                    print("Login successful!")
                    return
            print("Invalid username or password!")

    def register(self):
        username = input("Enter your desired username: ")
        password = input("Enter your password: ")
       

if __name__ == "__main__":
    Menu().run()
