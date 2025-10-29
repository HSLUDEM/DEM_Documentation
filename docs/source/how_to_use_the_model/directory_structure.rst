Directory Structure
====================

.. code-block:: text

    District_Energy_Model/
    ├── config/
    │   ├── input_files/
    │   │   ├── demand_side.yaml
    │   │   ├── meta_data.yaml
    │   │   ├── optimisation.yaml
    │   │   ├── scenarios.yaml
    │   │   ├── simulation.yaml
    │   │   ├── supply.yaml
    │   │   └── technologies.yaml
    │   └── dem_conda_environment.yml
    ├── data/
    │   ├── community_data/
    │   │   └── ...
    │   ├── electricity_demand/
    │   │   └── ...
    │   ├── electricity_mix_national/
    │   │   └── electricity_mix.feather
    │   ├── heat_demand/
    │   │   └── DHW_Profile.feather
    │   ├── master_data/
    │   │   ├── HDD_and_HDH_profiles/
    │   │   │   ├── HDD_Municipality_2023.feather
    │   │   │   ├── HDD_Municipality_2030.feather
    │   │   │   ├── HDD_Municipality_2040.feather
    │   │   │   ├── HDD_Municipality_2050.feather
    │   │   │   └── ...
    │   │   └── simulation_data/
    │   │       ├── df_master_sim.feather
    │   │       ├── meta_file_2.feather
    │   │       ├── simulation_profiles_file.feather
    │   │       └── ...
    │   ├── tech_wind_power/
    │   │   ├── profiles/
    │   │   │   └── ...
    │   │   └── p_installed_kW_wind_power.feather
    │   └── weather_data/
    │       └── com_files/
    │           └── ...
    ├── doc/
    │   ├── ...
    │   └── ...
    ├── src/
    │   ├── input_files/
    │   │       └── inputs.py
    │   ├── techs/
    │   │       ├── dem_tech_battery_energy_storage.py
    │   │       ├── dem_tech_biomass.py
    │   │       ├── dem_tech_chp_gt.py
    │   │       ├── dem_tech_core.py
    │   │       ├── dem_tech_district_heating.py
    │   │       ├── dem_tech_electric_heater.py
    │   │       ├── dem_tech_gas_boiler.py
    │   │       ├── dem_tech_gas_boiler_cp.py
    │   │       ├── dem_tech_gas_tank_energy_storage.py
    │   │       ├── dem_tech_gas_turbine_cp.py
    │   │       ├── dem_tech_grid_supply.py
    │   │       ├── dem_tech_heat_exchanger.py
    │   │       ├── dem_tech_heat_pump.py
    │   │       ├── dem_tech_heat_pump_core.py
    │   │       ├── dem_tech_heat_pump_cp.py
    │   │       ├── dem_tech_heat_pump_cp_lt.py
    │   │       ├── dem_tech_hydro_power.py
    │   │       ├── dem_tech_hydrogen.py
    │   │       ├── dem_tech_hydrogen_energy_storage.py
    │   │       ├── dem_tech_oil_boiler.py
    │   │       ├── dem_tech_oil_boiler_cp.py
    │   │       ├── dem_tech_other.py
    │   │       ├── dem_tech_pile_of_berries.py
    │   │       ├── dem_tech_solar_pv.py
    │   │       ├── dem_tech_solar_thermal.py
    │   │       ├── dem_tech_steam_turbine.py
    │   │       ├── dem_tech_thermal_energy_storage.py
    │   │       ├── dem_tech_thermal_energy_storage_dc.py
    │   │       ├── dem_tech_waste_heat.py
    │   │       ├── dem_tech_waste_heat_low_temperature.py
    │   │       ├── dem_tech_waste_to_energy.py
    │   │       ├── dem_tech_wind_power.py
    │   │       ├── dem_tech_wood_boiler.py
    │   │       ├── dem_tech_wood_boiler_cp.py
    │   │       └── dem_tech_wood_boiler_sg.py
    │   ├── dem.py
    │   ├── dem_calliope.py
    │   ├── dem_calliope_cc.py
    │   ├── dem_calliope_clustering.py
    │   ├── dem_clustering.py
    │   ├── dem_constants.py
    │   ├── dem_costs.py
    │   ├── dem_create_custom_district.py
    │   ├── dem_demand.py
    │   ├── dem_emissions.py
    │   ├── dem_energy_balance.py
    │   ├── dem_helper.py
    │   ├── dem_hp_cop_calculation.py
    │   ├── dem_output.py
    │   ├── dem_scenarios.py
    │   ├── dem_supply.py
    │   ├── dem_techs.py
    │   ├── paths.py
    │   └── run_dem.py
    ├── LICENSE.txt
    └── README.md


