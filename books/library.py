import json
import csv

from testdata import USERS_FILE_PATH, BOOKS_FILE_PATH, RES_FILE_PATH


def write_users(data):
    with open(RES_FILE_PATH, "w") as f:
        s = json.dumps(data, indent=4)
        f.write(s)


def read_users():
    with open(USERS_FILE_PATH, "r") as f:
        users = json.loads(f.read())
    return users


def main():
    users = read_users()
    users_count = len(users)

    with open(BOOKS_FILE_PATH, "r") as b:
        books = csv.DictReader(b)

        for k, book in enumerate(books):
            u = k % users_count
            if "books" in users[u]:
                users[u]["books"].append(book)
            else:
                users[u]["books"] = [book]

    write_users(users)


if __name__ == "__main__":
    main()
