# importing the class
from parser_class import Parser

# importing time function
import time

start_time = time.time()


def main():
    new_parser = Parser("example.txt")
    text = new_parser.parser_func()
    print(text)


# pass

if __name__ == '__main__':
    main()

print("%s seconds pass for reading and printing file" % (time.time() - start_time))
