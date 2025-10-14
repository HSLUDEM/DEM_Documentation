Model Input Files
================

Master File
-----------

Master file containing information about each individual building. Information about the whole district is extractred from this file by means of aggregation. The file can contain information about multiple district. In a simulation, only the information about buildings for the specified district will be extracted. Each building has a unique identification number (column 0, EGID) and belongs to a municipality identified by a number (column 4, GGDENR). Custom district can also be analysed by specifying (via EGID) which buildings belong to the districts. For Switzerland, data in columns 0 to 15 is extracted from the Federal Register of Buildings and Dwellings (RBD) (Federal Statistical Office, 2025). The naming convention of these columns has been adopted accordingly.

.. csv-table::
	      :file: input_files_csv/master_file_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/master_file_columns.csv
	      :widths: auto
	      :header-rows: 1


References
^^^^^^^^^^^

Federal Statistical Office (FSO). (2025). *Federal register of buildings and dwellings (RBD)*. https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html
