import argparse
import csv
import os


class Read:
    tag_number = 0

    def read(self):

        path = 'D:/project/data.csv'
        if not os.path.exists(path):
            with open('data.csv', 'a', newline='')as file:
                writer = csv.writer(file)

        with open('data.csv', 'r')as file:
            reader = csv.reader(file)
            list1 = (
                list(map(lambda item: (int(item[0]), int(item[1]), int(item[2])), reader)))
            Read.tag_number = ((list1[-1])[0] if len(list1) > 0 else 0)
            return list1


read_file = Read()


def list_home(a):
    items = read_file.read()
    for i in items:
        print(i)


def sort_price():
    items = read_file.read()
    items = list(sorted(items, key=lambda x: x[2]))
    for i in items:
        print(i)


def sort_size():
    items = read_file.read()
    items = list(sorted(items, key=lambda x: x[1]))
    for i in items:
        print(i)


def add(a, b):
    items = read_file.read()
    tag = read_file.tag_number
    tag += 1
    with open('data.csv', 'a', newline='')as file:
        writer = csv.writer(file)
        writer.writerow([tag, a, b])
        items.append([tag, a, b])


def delete(a):
    items = read_file.read()
    items = list(filter(lambda item: item[0] != a, items))
    with open('data.csv', 'w', newline='')as file:
        writer = csv.writer(file)
        for i in items:
            writer.writerow([i[0], i[1], i[2]])


global_parser = argparse.ArgumentParser(prog="calc")
subparsers = global_parser.add_subparsers(
    title="subcommands", help="arithmetic operations")

list_parser = subparsers.add_parser("list", help="add two numbers a and b")
list_parser.add_argument(type=int, nargs='?', dest="operands")
list_parser.set_defaults(func=list_home)

add_parser = subparsers.add_parser("add", help="subtract two numbers a and b")
add_parser.add_argument(type=int, nargs=2, dest='operands')
add_parser.set_defaults(func=add)

delete_parser = subparsers.add_parser(
    "delete", help="subtract two numbers a and b")
delete_parser.add_argument(type=int, nargs=1, dest='operands')
delete_parser.set_defaults(func=delete)

list_parser.add_argument('--sort')
args = global_parser.parse_args()
if args.func == list_home:
    if args.sort == 'size':
        sort_size()
    elif args.sort == 'price':
        sort_price()
    else:
        args.func(args.operands)
if args.func == add:
    args.func(*args.operands)
if args.func == delete:
    args.func(*args.operands)
#
