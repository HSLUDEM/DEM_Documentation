Electricity Demand
========================

Residential Buildings
------------------

The electricity demand from building appliances, excluding heating and transport, is referred to as *Household Demand*. It is modeled using a bottom-up approach for each individual building.
For residential buildings, annual demand is estimated based on the number of inhabitants. The number of inhabitants per building is derived from building size data provided in the Federal Register of Buildings and Dwellings (RBD) (Federal Statistical Office, 2025).
Annual electricity demand per inhabitant is taken from a report by the Swiss Federal Office of Energy (SFOE) on typical household electricity consumption in Switzerland (Nipkow, 2013). This annual demand per building is then distributed according to standard hourly load profiles (Rinaldi et al., 2022), with separate profiles applied for single-family and multi-family homes. Finally, the hourly demand of a district or municipality is obtained by aggregating the individual building demands.

The total annual electricity demand for each municipality is derived from an electricity demand model that distributes the measured national consumption across all Swiss municipalities (geoimpact AG, 2025).

Industry and Services
------------------
The electricity for industry and services is computed in a top-down approach as the difference between total demand in the municipality
and Household Demand. Load profiles are generated using measured consumption data on cantonal level from the grid operator SwissGrid (Swissgrid Ltd, 2025).


Electric Vehicles
--------------------

The electric load profiles for electric vehicle (EV) charging are added to the total electricity demand. These profiles are based on the study by `Herrera and Hug (2025) <https://arxiv.org/abs/2504.03633>`_. The hourly data are aggregated spatially to the municipality level. The original dataset assumes 100% electrification of the private transport sector; in the District Energy Model, partial electrification (e.g., 50%) is represented through linear scaling of the original data.

In the non-optimized simulations, fixed EV load profiles are applied. In the optimization scenarios, however, EV charging flexibility can be activated in the demand side scenario (see :ref:`demand-side-scenario`). This flexibility, as defined by Herrera and Hug (2025), includes lower and upper charging power limits as well as the daily available flexible energy.


References
^^^^^^^^^^^

Arthur Rinaldi, Héctor Ramirez, Benjamin Schroeteler, & Marco Meier. (2022). *The role of energy storage technologies in the context of the Swiss energy transition (SwissStore)* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6782179

Federal Statistical Office (FSO). (2025). *Federal register of buildings and dwellings (RBD)*. https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html

geoimpact AG, Energiereporter, 2025. [Online]. Available: https://energiereporter.energyapps.ch/methodology.

Nipkow, J. (2013). *Typischer Haushalt-Stromverbrauch* [Schlussbericht]. Zürich/Bern: Bundesamt für Energie (BFE).

Parajeles Herrera, M., & Hug, G. (2025). *Modeling Charging Demand and Quantifying Flexibility Bounds for Large-Scale BEV Fleets*. arXiv e-prints, arXiv-2504.

Swissgrid Ltd, Grid data, production and consumption, 2025. [Online]. Available: https://www.swissgrid.ch/en/
home/operation/grid-data/generation.html.