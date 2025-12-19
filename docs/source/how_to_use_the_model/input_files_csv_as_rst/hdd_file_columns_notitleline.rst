+--------+------------------+-----------+-----------------------------------------------+----------------------------------------+
| Number | Column           | Data type | Description                                   | Source for |Swiss_data_Zenodo_link|    |
+--------+------------------+-----------+-----------------------------------------------+----------------------------------------+
| 0      | ``Municipality`` | string    | Name of district according to ``GGDENAME``    | Swisstopo, 2024                        |
|        |                  |           |                                               |                                        |
|        |                  |           | in :ref:`master_file` and ``Municipality`` in |                                        |
|        |                  |           |                                               |                                        |
|        |                  |           | :ref:`meta_file`.                             |                                        |
+--------+------------------+-----------+-----------------------------------------------+----------------------------------------+
| 1      | ``HDD_12_2023``  | float     | Heating degree days for the district          | Computed based on temperature data of  |
|        |                  |           |                                               |                                        |
|        |                  |           | based on a reference temperature (start       | 2023 using the methods of Schneeberger |
|        |                  |           |                                               |                                        |
|        |                  |           | temperature for heating) of 12°C.             | et al. (2025)                          |
+--------+------------------+-----------+-----------------------------------------------+----------------------------------------+
| 2      | ``HDD_15_2023``  | float     | Heating degree days for the district          | Computed based on temperature data of  |
|        |                  |           |                                               |                                        |
|        |                  |           | based on a reference temperature (start       | 2023 using the methods of Schneeberger |
|        |                  |           |                                               |                                        |
|        |                  |           | temperature for heating) of 15°C.             | et al. (2025)                          |
+--------+------------------+-----------+-----------------------------------------------+----------------------------------------+
| 3      | ``GGDENR``       | int       | According to ``GGDENR`` in                    | Federal Statistical Office, 2025       |
|        |                  |           |                                               |                                        |
|        |                  |           | :ref:`master_file` and :ref:`meta_file`.      |                                        |
+--------+------------------+-----------+-----------------------------------------------+----------------------------------------+
