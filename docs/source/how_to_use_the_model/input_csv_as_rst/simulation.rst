+-----------------+------------------------------------------+----------------+------+-----------+--------+
| Attribute       | Description                              | Standard value | Unit | Data type | Source |
+=================+==========================================+================+======+===========+========+
| number_of_days  | Number of days to simulate, starting on  |                | —    | int       |        |
|                 |                                          |                |      |           |        |
|                 | 1 Jan. Mainly for testing the model.     |                |      |           |        |
+-----------------+------------------------------------------+----------------+------+-----------+--------+
| district_number | Unique identification number assigned to |                | —    | int       |        |
|                 |                                          |                |      |           |        |
|                 | the district. It is the identifier       |                |      |           |        |
|                 |                                          |                |      |           |        |
|                 | labelled "GGDENR" in the Master File and |                |      |           |        |
|                 |                                          |                |      |           |        |
|                 | Meta File. For Swiss municipalities,     |                |      |           |        |
|                 |                                          |                |      |           |        |
|                 | this is the BFS number and can be found  |                |      |           |        |
|                 |                                          |                |      |           |        |
|                 | online (www.bfs.admin.ch/bfs/de/home/gru |                |      |           |        |
|                 |                                          |                |      |           |        |
|                 | ndlagen/agvch.html).                     |                |      |           |        |
+-----------------+------------------------------------------+----------------+------+-----------+--------+
| generate_plots  | The generation of plots can be switched  |                | —    | bool      |        |
|                 |                                          |                |      |           |        |
|                 | on (true) or off (false).                |                |      |           |        |
+-----------------+------------------------------------------+----------------+------+-----------+--------+
| save_results    | If set to true, results will be saved in |                | —    | bool      |        |
|                 |                                          |                |      |           |        |
|                 | files.                                   |                |      |           |        |
+-----------------+------------------------------------------+----------------+------+-----------+--------+
