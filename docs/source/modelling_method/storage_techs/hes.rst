Hydrogen Energy Storage (HES)
=======================================

The HES technology represents a simple
hydrogen storage device
connected to the hydrogen producers and consumers. 
The consumers available in the current model are biomass technologies.
It can be charged by 
the elctrolyser.
The hydrogen tank is modelled like a battery. 
It has a given maximum capacity that can be set
by the optimizer if optimization is activated. When charging and
discharging, a fixed loss rate is applied. Furthermore, the storage
loses energy at a constant rate.

Using the parameter force_asynchronous_prod_con, the optimizer can be 
forced to never charge and discharge the storage at the same time.
This can be useful to prevent the energy system from disposing of 
hydrogen using the charging and discharging losses of the 
storage.

The initial charge of the storage is usually set to be optimized. Then,
the constraint is that the initial and final storage level have to be 
equal. Alternatively, a fixed initial state of charge can be defined.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/hes.rst

The symbols and names of the flows are

.. include:: ../../../how_to_use_the_model/flows_tables/hes.rst
