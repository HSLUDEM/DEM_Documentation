Thermal Energy Storage (TES) - decentralised
=======================================

The TESDC technology represents a small scale scale thermal energy Storage
connected to houses with individual heat pumps. It can be charged by 
the heat pump and, if allowed, by solar thermal collectors.
The thermal energy storage is modelled as a simple
thermal battery. It has a given maximum capacity that can be set
by the optimizer if optimization is activated. When charging and
discharging, a fixed loss rate is applied. Furthermore, the storage
loses energy at a constant rate. The heat stored in the TES is 
assumed to be useful heat that can be directly used for space heating
and domestic hot water.

Using the parameter force_asynchronous_prod_con, the optimizer can be 
forced to never charge and discharge the storage at the same time.
This can be useful to prevent the energy system from disposing of 
thermal energy using the charging and discharging losses of the 
storage.

The initial charge of the storage is usually set to be optimized. Then,
the constraint is that the initial and final storage level have to be 
equal. Alternatively, a fixed initial state of charge can be defined.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/tes_decentralised.rst

The symbols and names of the flows are

.. include:: ../../../how_to_use_the_model/flows_tables/tesdc.rst
