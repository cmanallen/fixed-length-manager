from space_seperated_import import *

char_list = [10, 10, 10, 10]
da_import = SpaceSeperatedImport(open('example.txt'), char_list).convert_file_to_object()
print(da_import)