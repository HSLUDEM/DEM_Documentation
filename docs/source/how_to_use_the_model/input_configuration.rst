Model Input - Configuration Files
=================================

Configuration files are provided to the model in YAML format and must be located in the ``config/input_files`` directory. The only file required is ``simluation.yaml``. For the other files, only parameters that deviate from the default values need to be specified. If no configuration files are provided other than ``simluation.yaml``, the model will run entirely using its built-in standard values.

Required configuration file:

- ``simulation.yaml``


Optional configuration files:

- ``meta_data.yaml``

- ``scenarios.yaml``

- ``optimisation.yaml``

- ``demand_side.yaml``

- ``supply.yaml``

- ``technologies.yaml``

All files define parameter names as top-level keys. The exception is technologies.yaml, where technologies appear as the top-level keys and their respective parameters are listed as sub-keys.

Below are example excerpts from two configuration files:

.. image:: images/scenarios_yaml.png
   :scale: 50%

----

.. image:: images/technologies_yaml.png
   :scale: 50%


Simulation
---------
Configuration file: ``simulation.yaml``

.. csv-table::
			:file: input_csv/simulation.csv
			:widths: auto
			:header-rows: 1


Meta Data
---------
Configuration file: ``meta_data.yaml``

.. csv-table::
	      :file: input_csv/meta_data.csv
	      :widths: auto
	      :header-rows: 1

Scenarios
---------
Configuration file: ``scenarios.yaml``

.. csv-table::
			:file: input_csv/scenarios.csv
			:widths: auto
			:header-rows: 1


Optimisation
---------
Configuration file: ``optimisation.yaml``

.. csv-table::
			:file: input_csv/optimisation.csv
			:widths: auto
			:header-rows: 1


Demand Side
---------
Configuration file: ``demand_side.yaml``

.. csv-table::
			:file: input_csv/demand_side.csv
			:widths: auto
			:header-rows: 1


Supply
---------
Configuration file: ``supply.yaml``

.. csv-table::
			:file: input_csv/supply.csv
			:widths: auto
			:header-rows: 1
		  

Technologies
---------

Configuration file: ``technologies.yaml``

Heat Pump
^^^^^^^^^^
Top key: heat_pump

.. csv-table::
			:file: input_csv/heat_pump.csv
			:widths: auto
			:header-rows: 1
			
.. include:: ../how_to_use_the_model/input_csv_as_rst/heat_pump.rst

Electric Heater
^^^^^^^^^^
Top key: electric_heater

.. csv-table::
			:file: input_csv/electric_heater.csv
			:widths: auto
			:header-rows: 1
			
			
Oil Boiler
^^^^^^^^^^
Top key: oil_boiler

.. csv-table::
			:file: input_csv/oil_boiler.csv
			:widths: auto
			:header-rows: 1
			

Gas Boiler
^^^^^^^^^^
Top key: gas_boiler

.. csv-table::
			:file: input_csv/gas_boiler.csv
			:widths: auto
			:header-rows: 1


Wood Boiler
^^^^^^^^^^
Top key: wood_boiler

.. csv-table::
			:file: input_csv/wood_boiler.csv
			:widths: auto
			:header-rows: 1


District Heating
^^^^^^^^^^
Top key: district_heating

.. csv-table::
			:file: input_csv/district_heating.csv
			:widths: auto
			:header-rows: 1


Solar Thermal
^^^^^^^^^^
Top key: solar_thermal

.. csv-table::
			:file: input_csv/solar_thermal.csv
			:widths: auto
			:header-rows: 1


Solar Photovoltaic (PV)
^^^^^^^^^^
Top key: solar_pv

.. csv-table::
			:file: input_csv/solar_pv.csv
			:widths: auto
			:header-rows: 1


Wind Power
^^^^^^^^^^
Top key: wind_power

.. csv-table::
			:file: input_csv/wind_power.csv
			:widths: auto
			:header-rows: 1


Hydro Power
^^^^^^^^^^
Top key: hydro_power

.. csv-table::
			:file: input_csv/hydro_power.csv
			:widths: auto
			:header-rows: 1


Grid Supply
^^^^^^^^^^
Top key: grid_supply

.. csv-table::
			:file: input_csv/grid_supply.csv
			:widths: auto
			:header-rows: 1


Thermal Energy Storage (TES) - centralised
^^^^^^^^^^
Top key: tes

.. csv-table::
			:file: input_csv/tes.csv
			:widths: auto
			:header-rows: 1


Thermal Energy Storage (TES) - decentralised
^^^^^^^^^^
Top key: tes_decentralised

.. csv-table::
			:file: input_csv/tes_decentralised.csv
			:widths: auto
			:header-rows: 1


Battery Energy Storage (BES)
^^^^^^^^^^
Top key: bes

.. csv-table::
			:file: input_csv/bes.csv
			:widths: auto
			:header-rows: 1


Biomass
^^^^^^^^^^
Top key: biomass

.. csv-table::
			:file: input_csv/biomass.csv
			:widths: auto
			:header-rows: 1


Hydrothermal Gasification
^^^^^^^^^^
Top key: hydrothermal_gasification

.. csv-table::
			:file: input_csv/hydrothermal_gasification.csv
			:widths: auto
			:header-rows: 1


Anaerobic Digestion Upgrade
^^^^^^^^^^
Top key: anaerobic_digestion_upgrade

.. csv-table::
			:file: input_csv/anaerobic_digestion_upgrade.csv
			:widths: auto
			:header-rows: 1


Anaerobic Digestion Upgrade Hydrogen
^^^^^^^^^^
Top key: anaerobic_digestion_upgrade_hydrogen

.. csv-table::
			:file: input_csv/anaerobic_digestion_upgrade_hydrogen.csv
			:widths: auto
			:header-rows: 1


Anaerobic Digestion Combined Heat and Power (CHP)
^^^^^^^^^^
Top key: anaerobic_digestion_chp

.. csv-table::
			:file: input_csv/anaerobic_digestion_chp.csv
			:widths: auto
			:header-rows: 1


Wood Gasification Upgrade
^^^^^^^^^^
Top key: wood_gasification_upgrade

.. csv-table::
			:file: input_csv/wood_gasification_upgrade.csv
			:widths: auto
			:header-rows: 1


Wood Gasification Upgrade Hydrogen
^^^^^^^^^^
Top key: wood_gasification_upgrade_hydrogen

.. csv-table::
			:file: input_csv/wood_gasification_upgrade_hydrogen.csv
			:widths: auto
			:header-rows: 1


Wood Digestion Combined Heat and Power (CHP)
^^^^^^^^^^
Top key: wood_digestion_chp

.. csv-table::
			:file: input_csv/wood_digestion_chp.csv
			:widths: auto
			:header-rows: 1


Hydrogen Production
^^^^^^^^^^
Top key: hydrogen_production

.. csv-table::
			:file: input_csv/hydrogen_production.csv
			:widths: auto
			:header-rows: 1


Gas Turbine Combined Heat and Power (CHP) - small scale
^^^^^^^^^^
Top key: chp_gt

.. csv-table::
			:file: input_csv/chp_gt.csv
			:widths: auto
			:header-rows: 1


Gas Turbine - centralised plant (cp)
^^^^^^^^^^
Top key: gas_turbine_cp

.. csv-table::
			:file: input_csv/gas_turbine_cp.csv
			:widths: auto
			:header-rows: 1


Steam Turbine
^^^^^^^^^^
Top key: steam_turbine

.. csv-table::
			:file: input_csv/steam_turbine.csv
			:widths: auto
			:header-rows: 1


Wood Boiler - centralised plant (cp)
^^^^^^^^^^
Top key: wood_boiler_cp

.. csv-table::
			:file: input_csv/wood_boiler_cp.csv
			:widths: auto
			:header-rows: 1


Waste-to-Energy Combined Heat and Power
^^^^^^^^^^
Top key: waste_to_energy

.. csv-table::
			:file: input_csv/waste_to_energy.csv
			:widths: auto
			:header-rows: 1


Heat Pump - centralised plant (cp)
^^^^^^^^^^
Top key: heat_pump_cp

.. csv-table::
			:file: input_csv/heat_pump_cp.csv
			:widths: auto
			:header-rows: 1


Other
^^^^^^^^^^
Top key: other

.. csv-table::
			:file: input_csv/other.csv
			:widths: auto
			:header-rows: 1


References
-----------

Ben-Kiki, Oren, Clark, Clark Evans, and Ingy döt Net. *YAML Ain’t Markup Language (YAML™) Version 1.2 (3rd Edition)*. 2009.
