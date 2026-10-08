import csv


# Task 1
def save_books(books):
    with open("books.txt", "w", encoding="utf-8") as file:
        for book in books:
            file.write(f"{book}\n")


books = [
    "Harry Potter",
    "The Hobbit",
    "1984",
    "The Little Prince"
]

save_books(books)


# Task 2
def read_products(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")


read_products("products.csv")