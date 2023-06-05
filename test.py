import random


def random_line(fname):
    products = []
    words_number = 5

    lines = open(fname).read().splitlines()

    for _ in range(words_number):
        products.append(random.choice(lines))
    return products



if __name__ == '__main__':
    products = random_line('products.txt')
    print(products)