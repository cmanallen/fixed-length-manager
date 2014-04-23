Simple Character Delimited Import
by Colton Allen

Use case: This is an import I wrote to handle files from a large, publicly traded, American corporation.

Warning: Double check your files before importing.  This import will insert bogus information into your system if you're not careful.

Description: The import requires two pieces of information.  First, you will need to provide a file.  Second you will need to provide a list of column counts.  These will have to be counted manually. You can see example usage in the example.py file and an example import in the example.txt file.

Todo:
    *Handle headings
    *Automatically count characters per column