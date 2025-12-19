+---------------------+------------------------------------------+-----------------------+------+-----------+
| Attribute           | Description                              | Standard value        | Unit | Data type |
+=====================+==========================================+=======================+======+===========+
| ``number_of_days``  | Number of days to simulate, starting on  | *required user input* | —    | int       |
|                     |                                          |                       |      |           |
|                     | 1 Jan. A value between 1 and 365 is      |                       |      |           |
|                     |                                          |                       |      |           |
|                     | recommended.                             |                       |      |           |
+---------------------+------------------------------------------+-----------------------+------+-----------+
| ``district_number`` | Unique identification number assigned to | *required user input* | —    | int       |
|                     |                                          |                       |      |           |
|                     | the district. It is the identifier       |                       |      |           |
|                     |                                          |                       |      |           |
|                     | labelled "GGDENR" in the Master File and |                       |      |           |
|                     |                                          |                       |      |           |
|                     | Meta File. For Swiss municipalities,     |                       |      |           |
|                     |                                          |                       |      |           |
|                     | this is the BFS number and can be found  |                       |      |           |
|                     |                                          |                       |      |           |
|                     | online (www.bfs.admin.ch/bfs/de/home/gru |                       |      |           |
|                     |                                          |                       |      |           |
|                     | ndlagen/agvch.html).                     |                       |      |           |
+---------------------+------------------------------------------+-----------------------+------+-----------+
| ``generate_plots``  | The generation of plots can be switched  | *required user input* | —    | bool      |
|                     |                                          |                       |      |           |
|                     | on (true) or off (false).                |                       |      |           |
+---------------------+------------------------------------------+-----------------------+------+-----------+
| ``save_results``    | If set to true, results will be saved in | *required user input* | —    | bool      |
|                     |                                          |                       |      |           |
|                     | files.                                   |                       |      |           |
+---------------------+------------------------------------------+-----------------------+------+-----------+
