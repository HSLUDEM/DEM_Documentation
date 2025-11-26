Heat Pump Central Plant - From Low Temperature
=======================================

The heat pump central plant represents a large scale heat pump
connected to the district heating network. It supplies directly
useful heat. The heat pump is fed by *low-temperature heat*, which 
is currently just available from the technology *waste heat (low 
temperature)*. It converts low-temperature heat into useful heat.
Its COP is a constant. 

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/heat_pump_cp_lt.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_h\_hpcplt} = \mathtt{COP} \cdot \mathtt{u\_e\_hpcplt} = \mathtt{u\_e\_hpcplt} + \mathtt{u\_hlt\_hpcplt}
