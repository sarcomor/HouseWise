import argparse
import csv
import os


def create_file():
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['price', 'size', 'tag'])


if not os.path.exists((os.curdir)+'\data.csv'):
    create_file()


def tag_number():
    values = []
    with open('data.csv', 'r') as file:
        dict_reader_values = list(csv.DictReader(file))
        for i in dict_reader_values:
            values.append((i['size'], i['price'], i['tag']))
            number = i['tag']
    if len(values) < 1:
        number = 0
    return int(number)


def add_(price, size):
    number = tag_number()
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([price, size, number+1])


def delete_(tag_number):
    values = []
    with open('data.csv', 'r') as file:
        dict_reader_values = list(csv.DictReader(file))
        for i in dict_reader_values:
            if i['tag'] != str(tag_number):
                values.append((i['size'], i['price'], i['tag']))
    create_file()
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for i in values:
            writer.writerow([i[1], i[0], i[2]])


def list_():
    with open('data.csv', 'r') as file:
        dict_reader_values = list(csv.DictReader(file))
    for i in dict_reader_values:
        print(int(i['tag']), '- xxxxx')
        print('price', (int(i['price'])), '$')
        print('size', (int(i['size'])), 'm2\n---')


def sort_list_(sort_list):
    values = []
    match sort_list:
        case 'size':
            with open('data.csv', 'r') as file:
                dict_reader_values = list(csv.DictReader(file))
                for i in dict_reader_values:
                    values.append(
                        (int(i['size']), int(i['price']), int(i['tag'])))
                values = sorted(values)
                for i in values:
                    print(int(i[2]), '- xxxxx')
                    print('price', (int(i[1])), '$')
                    print('size', (int(i[0])), 'm2\n---')
        case 'price':
            with open('data.csv', 'r') as file:
                dict_reader_values = list(csv.DictReader(file))
                for i in dict_reader_values:
                    values.append(
                        (int(i['price']), int(i['size']), int(i['tag'])))
                values = sorted(values)
                for i in values:
                    print(int(i[2]), '- xxxxx')
                    print('price', (int(i[0])), '$')
                    print('size', (int(i[1])), 'm2\n---')


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("pos", choices=['list', 'delete', 'add'])
    parser.add_argument("add_values", nargs="*", type=int)
    parser.add_argument("-s", '--sort', choices=['price', 'size'])
    args = parser.parse_args()

    if args.pos == 'add':
        add_(price=args.add_values[0], size=args.add_values[1])

    if args.pos == 'delete':
        delete_(args.add_values[0])

    if args.pos == 'list':
        if args.sort == 'price' or args.sort == 'size':
            sort_list_(sort_list=args.sort)
        else:
            list_()


if __name__ == '__main__':
    main()
