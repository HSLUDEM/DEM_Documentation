Wood Boiler
=======================================

The wood boiler represent a device that burns 
wood to produce heat for space heating
and domestic hot water. It is situated in individual 
buildings and therefore contributes a constant share
to the overal heat production. It has a constant
efficiency and constant carbon emissions per kWh
of energy converted.

For Swiss municipalities, the wood boiler is usually
already deployed in some buildings, since it is an often
encountered technology. Therefore, an additional 
replacement capex can be defined. If wood boilers reach
the end of their life, this replacement capex defines
how much it costs to replace it with a new boiler, without
redoing any of the ancillary installations.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/wood_boiler.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_h\_wb} = \mathtt{eta} \cdot \mathtt{u\_wd\_wb}
