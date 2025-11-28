Gas Tank Energy Storage (GTES)
=======================================

The GTES technology represents a gas tank. 
It can be charged from the gas network, either by 
gas bought from the grid or by locally produced 
biogas. 
It is modelled like a battery. 
It has a given maximum capacity that can be set
by the optimizer if optimization is activated. When charging and
discharging, a fixed loss rate is applied. Furthermore, the storage
loses energy at a constant rate. 

Using the parameter force_asynchronous_prod_con, the optimizer can be 
forced to never charge and discharge the storage at the same time.
This can be useful to prevent the energy system from disposing of 
gas using the charging and discharging losses of the 
storage.

The initial charge of the storage is usually set to be optimized. Then,
the constraint is that the initial and final storage level have to be 
equal. Alternatively, a fixed initial state of charge can be defined.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/gtes.rst

