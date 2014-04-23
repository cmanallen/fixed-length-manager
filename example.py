from count_delimited_import import *

char_list = [10, 10, 10, 10]
output = CountDelimitedImport(open('example.txt'), char_list).convert_file_to_object()
print(output)