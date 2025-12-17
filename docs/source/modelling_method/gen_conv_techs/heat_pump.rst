Heat Pump
=======================================

A heat pump is a device that uses work to transport environmental heat into heat at a useful 
temperature level. In our model, we have electric heat pumps available as a technology.

The heat pump technology models a small to medium size heat pump located in a building.

The power available to the heating system is given by the electric input power multiplied
with the coefficient of performance (COP).
.. math:: P_\\text{out} = \\text{COP} \\cdot P_\\text{elec}

Our model contains a module for the detailed modeling of the COP based on properties 
of the building and the heat pumps. For this, there are plenty of parameters in the input 
file.

For Swiss municipalities, the heat pump is usually
already deployed in some buildings, since it is an often
encountered technology. Therefore, an additional 
replacement capex can be defined. If heat pumps reach
the end of their life, this replacement capex defines
how much it costs to replace it with a new heat pump, without
redoing any of the ancillary installations.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/heat_pump.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_h\_hp} = \mathtt{COP} \cdot \mathtt{u\_e\_hp} 

The symbols and names of the flows are

.. include:: ../../how_to_use_the_model/flows_tables/hp.rst


COP modes
-----------------------------------------------------------
There are several ways to set the COP of the heat pumps.

In the mode "constant", a constant, user-defined COP is used.

In the mode "from_file", a timeseries provided by the user as
file is used.

In the mode "from_file_adjusted_to_spf", a timeseries provided by
the user is used but using the demand profile, it is scaled
such that the SPF reaches a user-defined value.

In the mode "location_based", a COP model taking into account
many properties of the building stock and location is used. This
model is described further below.

"location_based" COP mode
++++++++++++++++++++++++++++++++++++++++++++

The "location_based" COP mode is the standard COP mode.
It calculates a COP timeseries based on the properties of the
individual buildings, the quality_factors specified in the 
input file, the local weather and internal parameters defined
in the corresponding code file.

For each building, the algorithm assign probabilities for 
several properties for space heating

1. Is the heat dissipator radiator- or underfloor-heating-based
2. Is the heat pump air-source or ground-source.
3. Does the heat pump already exist or is it a new device to be installed by the optimizer.
4. Which heating curve construction period is used.

and for domestic hot water-heating

1. Is the heat pump air-source or ground-source.
2. Does the heat pump already exist or is it a new device to be installed by the optimizer.

For each building, we assign a construction year. This year is the GBAUJ from the RBD if
it is defined. Otherwise, the construction period (GBAUP) is used and the central year
of the construction period is assigned as construction year.

The share of radiators is assumed to be 100\% until 1970. From then on, it rises by 1.66\% per year
until reaching 100\% in 2030. The year here is the construction year of the building.

The share of ASHPs is assumed to be 66\% for existing installations (34\% GSHP), 
while for new installations, 72\% ASHPs and 28\% GSHPs is assumed. These percentages
are based on the statistics for sold heat pumps by the FWS (FWS, 2025).
For existing installations, this is only used if the heat source is not specified
in the RBD.

Whether the heat pump already exists is based on the RBD-information (FSO, 2025).

For the definition of the heating curve construction period, we rely on the 
information sheet "Heizkurve richtig einstellen" by the Swiss Federal Office of Energy 
(SwissEnergy, 2022).

For air-source heat pumps, the outdoor temperature is used as source temperature.
For ground-source heat pumps, a simple harmonic function is used as source temperature, 
with a mean value of 5°C and an amplitude of 3°C, where the lowest point is reached at
the end of February.

For the domestic hot water, a constant temperature of 55°C is assumed.

The COP is then calculated based on the Carnot efficiency of a perfect 
heat pump, capping the efficiency at 20. This value is then corrected
by the quality_factor provided by the user.

.. math::
   COP_{Carnot} = \\frac{T_{cond}}{T_{cond} - T_{evap}}

where temperatures are in kelvin and refer to the condenser (output) and
evaporator (source) sides of the heat pump.

This efficiency is then different for newly installed HPs than for the 
existing ones. Usually the existing HPs profit from being in more modern
buildings, which yields lower heating water temperatures and thereby
higher efficiencies, but their efficiency is reduced by the age of the 
existing heat pumps, which have lower device-level efficiencies, and by 
the fact that new buildings have a higher share of DHW, which is hotter than
heating water.

References
^^^^^^^^^^^

.. alphabetized by first author surname

SwissEnergy (2022, August 29). *Set the heating curve correctly* Federal Office of Energy. https://pubdb.bfe.admin.ch/en/publication/download/9982

FWS (2025). *Jahres-Statistiken & Marktzahlen* FWS Fachvereinigung Wärmepumpen Schweiz. https://www.fws.ch/statistiken/

Federal Statistical Office (FSO). (2025). *Federal register of buildings and dwellings (RBD)*. https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html
