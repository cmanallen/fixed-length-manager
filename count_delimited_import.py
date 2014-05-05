class CountDelimitedImport(object):

	def __init__(self, uploaded_file, character_list):
		self.uploaded_file = uploaded_file
		self.character_list = character_list

	def convert_file_to_object(self):
		rows = self.uploaded_file.read().split('\n')
		row_object = {}

		i = 0
		for row in rows:
			row_object[i] = self._split_row_into_columns(row, self.character_list)
			i += 1

		return row_object

	def _split_row_into_columns(self, string, column_count):
		column_object = {}

		position = 0
		j = 0
		for column in column_count:
			column_object[j] = string[position:position+column].strip()
			position += column
			j += 1
		
		return column_object