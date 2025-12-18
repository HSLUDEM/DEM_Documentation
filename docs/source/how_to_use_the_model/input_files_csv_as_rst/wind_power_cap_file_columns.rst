+--------+------------------+-----------+------------------------------------------+--------------------------------------+
| Number | Column           | Data type | Description                              | Source for Swiss dataset             |
+========+==================+===========+==========================================+======================================+
| 0      | ``Municipality`` | string    | Name of district according to            | Swisstopo, 2024                      |
|        |                  |           |                                          |                                      |
|        |                  |           | ``GGDENAME`` in :ref:`master_file` and   |                                      |
|        |                  |           |                                          |                                      |
|        |                  |           | ``Municipality`` in :ref:`meta_file`.    |                                      |
+--------+------------------+-----------+------------------------------------------+--------------------------------------+
| 1      | ``p_kW``         | float     | Currently installed wind power capacity  | Swiss Federal Office of Energy SFOE, |
|        |                  |           |                                          |                                      |
|        |                  |           | in kW in the district. This data is used | 2022a                                |
|        |                  |           |                                          |                                      |
|        |                  |           | for computation of the base scenario     |                                      |
|        |                  |           |                                          |                                      |
|        |                  |           | (i.e., current status).                  |                                      |
+--------+------------------+-----------+------------------------------------------+--------------------------------------+
