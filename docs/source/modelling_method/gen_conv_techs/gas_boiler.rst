Gas Boiler
=======================================

The gas boiler represent a device that burns 
gas to produce heat for space heating
and domestic hot water. It is situated in individual 
buildings and therefore contributes a constant share
to the overal heat production. It has a constant
efficiency and constant carbon emissions per kWh
of energy converted.

For Swiss municipalities, the gas boiler is usually
already deployed in some buildings, since it is an often
encountered technology. Therefore, an additional 
replacement capex can be defined. If gas boilers reach
the end of their life, this replacement capex defines
how much it costs to replace it with a new boiler, without
redoing any of the ancillary installations.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/gas_boiler.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_h\_gb} = \mathtt{eta} \cdot \mathtt{u\_gas\_gb}

The symbols and names of the flows are

.. include:: ../../../how_to_use_the_model/flows_tables/gb.rst
