
.. _hydro_power:

Hydro Power
=======================================

Hydro power represents local small scale hydro power
plants that contribute mostly to the local electricity mix.
An approach by Wild et al. (2024) is used
to define which hydro power plants are regarded as being
local hydro power plants and which ones are assumed to contribute
directly to the national grid.

For hydro power, there is a defined production profile. 
For Swiss municipalities, local hydro availability is determined
using the data about electricity production plants obtained from 
the Swiss Federal Office of Energy (2022).

.. include:: ../../how_to_use_the_model/input_csv_as_rst/hydro_power.rst

The symbols and names of the flows are

.. include:: ../../how_to_use_the_model/flows_tables/hydro.rst

Wild, M., Stocker, N., & Rohrer, J. (2024, May). *Techno-economic realization of energy balancing with batteries, power-to-X, and demand-side management* (SWEET Call 1-2020: EDGE, Deliverable Report 2.4). Zurich University of Applied Sciences (ZHAW). |zhaw_hydro_link|.

.. |zhaw_hydro_link| raw:: html

   <a href="https://www.aramis.admin.ch/Texte/?ProjectID=49138" target="_blank">https://www.aramis.admin.ch/Texte/?ProjectID=49138</a>
   
Swiss Federal Office of Energy (SFOE). (2022). *Dokumentation «minimales Geodatenmodell»: Elektrizitätsproduktionsanlagen* (Version 1.0rev, Geobasisdatensatz Nr. 221.1). Eidgenössisches Departement für Umwelt, Verkehr, Energie und Kommunikation. |e_prod_plants_link|

.. |e_prod_plants_link| raw:: html

   <a href="https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/production-plants/electricity-production-plants.html" target="_blank">https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/production-plants/electricity-production-plants.html</a>