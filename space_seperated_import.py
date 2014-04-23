class SpaceSeperatedImport(object):

	def __init__(self, uploaded_file, character_list):
		self.uploaded_file = uploaded_file
		self.character_list = character_list

	def convert_file_to_object(self):
		rows = self.uploaded_file.read().split('\n')
		i = 0
		row_object = {}

		for row in rows:
			row_object[i] = self._split_row_into_columns(row, self.character_list)
			i += 1

		return row_object

	def _split_row_into_columns(self, string, column_count):
		position = 0
		j = 0
		column_object = {}

		for column in column_count:
			end = position + column
			column_object[j] = string[position:end:]
			position += column
			j += 1
		
		return column_object