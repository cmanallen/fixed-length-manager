class SpaceSeperatedImport(object):

	def __init__(self, uploaded_file, character_list):
		self.uploaded_file = uploaded_file
		self.character_list = character_list

	def convert_file_to_object(self):
		rows = self.uploaded_file.split('\n')
		row_array = {}

		for row in rows:
			row_array.append(self.split_row_into_columns(row, self.character_list))

		return row_array

	def split_row_into_columns(self, string, column_count):
		position = 0
		column_array = {}

		for column in column_count:
			column_array.append(column[position:position+column])
			position += column
		
		return column_array