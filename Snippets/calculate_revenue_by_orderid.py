import sys
from functools import reduce

def show_total_by_order_id(path, order_id):
    # Opens a file given a specific path
    file = open(path, 'r')
    file_read = file.read()
    items = file_read.splitlines()

    # Filter data from the specified order_id
    filter_items = filter(lambda rec: int(rec.split(',')[1]) == order_id, items)

    # Select the revenue column for the specifid order_id records
    map_items = map(lambda rec: float(rec.split(',')[4]), filter_items)

    # Summarization of the selected records
    revenue = reduce(lambda total, element: total + element, map_items)
    print(revenue)

def index_error_message():
    # If there's an IndexError while calculating the two input variables this will be printed
    print('IndexError: This program needs exactly two arguments to function correctly.')
    print('Please enter the arguments in the following order: [1]path_to file, [2]orderId')

try:
    path = sys.argv[1]
    order_id = int(sys.argv[2])
except IndexError:
    index_error_message()
    sys.exit()

if __name__ == "__main__":
    show_total_by_order_id(path, order_id)
