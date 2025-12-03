from generate_table import *


def generate_flow_tables():
    # print(df_plot.index.values)

    #In- Out- Flows into or out of devices
    flows_to_consider = ['u_e_bes','u_gas_gtes','v_gas_gtes',
                         'u_hyd_hes','v_hyd_hes',
                         'u_e_eh','u_e_hp','u_e_hpcp','u_e_hpcplt','u_e_hydp',
                         'u_e_wguh','u_gas_chpgt','u_gas_gb','u_gas_gtcp',
                         'u_oil_obcp', 'u_gas_gbcp','u_e_ehcp', 
                         'u_wd_wbcp',
                         'u_h_tes','u_h_tesdc',
                         'u_msw_wte','u_oil_ob','u_steam_st',
                         'u_wd_wb', 
                         'v_h_eh', 'v_h_gb', 'v_h_hp', 
                         'v_h_hpcp', 
                         'v_h_hpcplt', 
                         'u_hlt_hpcplt', 'v_h_ob', 'v_h_solar', 'v_h_tes', 
                         'v_h_tesdc', 'v_h_wb',  'v_h_obcp', 'v_h_ehcp',
                         'v_h_wbcp',
                         'v_h_gbcp',
                         'v_h_wguh', 'v_h_wte', 'v_e_bes',  
                         'v_e_chpgt', 'v_e_gtcp', 'v_e_hydro', 
                         'v_e_pv', 'v_e_st', 
                         'v_e_wp', 'v_e_wte', 'v_hyd_hydp', 'v_steam_gtcp',
                         'v_e_wguc','u_hyd_wguh',
                         'u_e_wgu','u_e_aguh','u_hyd_aguh',
                         'v_gas_agu','v_h_aguc', 
                         'v_h_aguh', 'v_gas_aguh', 'v_e_aguc',
                         'u_wd_wgu','u_wd_wguc','u_wd_wguh',
                         'v_gas_wgu', 'v_gas_wguh',
                         'v_h_wgu', 'v_h_wguc','v_gas_hg',
                         'v_steam_wbsg', 'u_wd_wbsg', 'v_h_other', 'v_h_wh',
                         'v_h_chpgt', 
                         'v_h_st', #'v_h_chpgt_waste', 'v_h_chpgt', 
                         'v_hlt_whlt',
                         ]

    env_heat_flows = ['u_h_hp', 'u_h_hpcp']

    flows_to_consider_two_word_carrier = ['u_wet_bm_agu', 'u_wet_bm_aguc' ,
                                          'u_wet_bm_aguh', 'u_wet_bm_hg'] #'u_h_hpcp',

    link_nodes_to_consider = ['hp', 'aguh', 'bes', 'eh', 'hpcp', 'hpcplt',
                              'hydp', 'wgu', 'wguh', 'chpgt', 'gb', 
                              'gtcp', 'tes', 'tesdc', 'wte', 'ob', 
                              'st', 'wb', 'wguc', 'agu', 'hg', 'aguc', 
                              'bm', 'dh', 'solar', 'hydro', 'pv', 'wp',
                              'obcp', 'gbcp', 'gtes', 'hes', 'wbsg', 
                              'wbcp', 'ehcp', 
                              'other',
                              'wh', 'whlt']
    
    carriers = ['e', 'h', 'gas', 'oil', 'wd', 'msw', 'hyd', 'steam', 'wet_bm', 'loss', 'hlt']

    exports = ['exp_'+c for c in carriers]

    carriercolors = ["#92D505", "#F00000", "#bd9200", "#663300", "#663300", "#000000", "#00b0f0", "#f7a315", "#663300", "#636363", "#ff00ff"]

    inputs = ['m_e_cbimport', 
              'm_gas', 'm_h_dh']+['m_e_ch_biomass','m_e_ch_hydro','m_e_ch_nuclear','m_e_ch_other','m_e_ch_wind']

    outputs = ['d_e_ev', 'd_e_hh', 'd_h_hw', 'd_h_s']

    outputs_inverted = ['d_e_unmet', 'd_h_unmet']

    export_streams = ['v_e_aguc_exp', 'v_e_bm_exp', 'v_e_hydro_exp', 'v_e_pv_exp', 'v_e_wguc_exp', 'v_e_wp_exp', 
                      'v_h_chpgt_waste', 'v_h_st_wbsg_waste', 'v_h_st_gtcp_waste']

    listOfAllNodes = link_nodes_to_consider + carriers + inputs + outputs + outputs_inverted + ["env_heat"] + exports
        
    nodeNames = {'tes': 'TES', 'pv': 'PV', 'hyd': 'H₂', 'm_gas': 'Import Gas', 
                 'm_h_dh': 'Import District Heat', 'tesdc': 'TES decentralized', 
                 'm_e_ch': 'Electricity Import CH', 'm_e_cbimport': 'Electricity Import internat.', 
                 'hydro': 'Hydropower (local)', 'bes': 'Battery storage', 'exp_e': 'Export electricity', 
                 'exp_h': 'Export heat', 
                 'd_e_ev': 'Electric mobility', 'd_e_hh': 'Households', 
                 'd_h_s': 'Heat for space heating', 'd_h_hw': 'Heat for DHW', 'h': 'Heat', 
                 'oil': 'Oil', 'solar': 'Solar thermal', 'ob': 'Oil boiler', 'wb': 'Wood boiler',
                 'gas': 'Gas', 'gb': 'Gas boiler', 'wte': 'Waste-to-Energy', 'wd': 'Wood',
                 'bm': 'Biomass', 'wet_bm': 'Wet biomass', 'wp': 'Wind power',
                 'gtcp': 'Gas turbine', 'msw': 'Municipal solid waste', 'hydp': 'Electrolyser',
                 'steam': 'Steam', 'st': 'Steam turbine', 'e': 'Electricity', 
                 'hp': 'Heat pump', 'eh': 'Electric heater', 'hpcp': 'Heat pump (centralized)',
                 'hpcplt': 'Heat pump (centralized, from low-T heat)',
                 'chpgt': 'CHP Gas turbine', 'wgu': 'Wood gasification', 'wguc': 'Wood Gasification CHP', 
                 'aguc': 'Anaerobic digestion CHP', 'agu': 'Anaerobic digestion',
                 'hg': 'Hydrothermal gasification', 'wguh': 'Wood gasification H₂ upgrade', 
                 'aguh': 'Anaerobic digestion H₂ upgrade',
                 'bmc': 'Biomass conversion', 'obcp': 'Oil boiler (centralized)', 
                 'ehcp': 'Electric heater (centralized)', 
                 'gbcp': 'Gas boiler (centralized)', 'gtes': 'Gas tank', 'hes': 'Hydrogen storage', 
                 'm_e_ch_biomass': "Biomass electricity CH",'m_e_ch_hydro': 'Hydro power CH',
                 'm_e_ch_nuclear': "Nuclear power CH",
                 'm_e_ch_other': 'Other domestic electricity generation',
                 'm_e_ch_wind': "Wind power CH", 'd_e_unmet': 'Unmet electricity demand',
                 'd_h_unmet': 'Unmet heat demand', "env_heat": "Environmental heat", 'other': 'Other',
                 'wh': 'Waste heat', 'whlt': 'Waste heat (low temperature)', 'wbsg': 'Wood boiler (steam generator)', 
                 'wbcp': 'Wood boiler (central plant)', 'hlt': 'Heat (Low Temperature)'}

    specialColornames = {'d_e_hh': carriercolors[carriers.index('e')], 'd_e_ev': carriercolors[carriers.index('e')],
                         'd_h_s': carriercolors[carriers.index('h')], 'd_h_hw': carriercolors[carriers.index('h')], 
                         'm_gas': carriercolors[carriers.index('gas')], 'm_wd': carriercolors[carriers.index('wd')], 
                         'pv': '#f7b201', 'm_h_dh': carriercolors[carriers.index('h')], 'solar': '#f7b201',
                         'm_e_ch': carriercolors[carriers.index('e')], 'm_e_cbimport': carriercolors[carriers.index('e')],
                         'd_e_unmet': '#1f1f1f', 'd_h_unmet': '#1f1f1f',
                         }
    
    nodeNameMapped = []
    colorsNodeNames = []


    for k in range(len(listOfAllNodes)):
        nodename = listOfAllNodes[k]
        if nodename in nodeNames.keys():
            nodeNameMapped.append(nodeNames[nodename])
        else:
            nodeNameMapped.append(nodename)

        if nodename in carriers:
            colorsNodeNames.append(carriercolors[carriers.index(nodename)])
        elif nodename in specialColornames.keys():
            colorsNodeNames.append(specialColornames[nodename])
        else:
            colorsNodeNames.append('#77c5d8')

    sources = []
    targets = []
    values = []
    colors = []


    dict_for_tables = {}


    for keyword in export_streams:
        carrier = keyword.split('_')[1]
        s = keyword.split('_')
        if len(s) == 4:
            device = s[2]
        elif len(s) == 5:
            device = s[3]
        type = s[-1]

        if not device in dict_for_tables.keys():
            dict_for_tables[device] = []

        if type == "exp":
            dict_for_tables[device].append([keyword, "Exported "+nodeNames[carrier]])
        elif type == "waste":
            if not len(s) == 5:
                dict_for_tables[device].append([keyword, "Waste "+nodeNames[carrier]])
            else:
                dict_for_tables[device].append([keyword, "Waste "+nodeNames[carrier] + " (via steam turbine)"])

    #calculate useful output streams
    for keyword in outputs:

        carrier = keyword.split('_')[1]
        outputIndex = listOfAllNodes.index(keyword)
        carrierIndex = listOfAllNodes.index(carrier)

        device = keyword.split('_')[0]+"_"+keyword.split('_')[1]

        if not device in dict_for_tables.keys():
            dict_for_tables[device] = []

        if carrier == "e":
            dict_for_tables[device].append([keyword, "Demand "+nodeNames[carrier] + " " + nodeNames[keyword]])
        else:
            dict_for_tables[device].append([keyword, "Demand " + nodeNames[keyword]])


    for keyword in outputs_inverted:

        carrier = keyword.split('_')[1]
        outputIndex = listOfAllNodes.index(keyword)
        carrierIndex = listOfAllNodes.index(carrier)

        device = keyword.split('_')[0]+"_"+keyword.split('_')[1]

        if not device in dict_for_tables.keys():
            dict_for_tables[device] = []

        if carrier == "e":
            dict_for_tables[device].append([keyword, nodeNames[keyword]])
        else:
            dict_for_tables[device].append([keyword, nodeNames[keyword]])

    for keyword in inputs:
        carrier = keyword.split('_')[1]

        inputIndex = listOfAllNodes.index(keyword)
        carrierIndex = listOfAllNodes.index(carrier)

        if carrier == "e":
            device = "m_e"
        elif carrier == "gas":
            device = "m_gas"
        elif carrier == "h":
            device = "dhn"

        if not device in dict_for_tables.keys():
            dict_for_tables[device] = []

        dict_for_tables[device].append([keyword, nodeNames[keyword]])

    for keyword in env_heat_flows: #"u_h_hp", "u_h_hpcp"

        

        carrier = keyword.split('_')[1]
        device = keyword.split('_')[2]

        print(keyword, carrier, device)

        if not device in dict_for_tables.keys():
            dict_for_tables[device] = []

        dict_for_tables[device].append([keyword, "Environmental Heat Inflow "+nodeNames[device]])

    #calculate internal flows
    for keyword in flows_to_consider:

        device = keyword.split('_')[2]
        carrier = keyword.split('_')[1]
        isIn = keyword.split('_')[0] == 'u'

        if not device in dict_for_tables.keys():
            dict_for_tables[device] = []

        if isIn:
            dict_for_tables[device].append([keyword, "Inflow "+ nodeNames[carrier] ])
        else:
            dict_for_tables[device].append([keyword, "Outflow "+ nodeNames[carrier] ])

    for keyword in flows_to_consider_two_word_carrier:
        device = keyword.split('_')[3]
        carrier = keyword.split('_')[1]+"_"+keyword.split('_')[2]
        isIn = keyword.split('_')[0] == 'u'

        if not device in dict_for_tables.keys():
            dict_for_tables[device] = []

        if isIn:
            dict_for_tables[device].append([keyword, "Inflow "+ nodeNames[carrier] ])
        else:
            dict_for_tables[device].append([keyword, "Outflow "+ nodeNames[carrier] ])
    return dict_for_tables

def main():
    dict_for_tables = generate_flow_tables()

    containing_folder = "how_to_use_the_model"

    for k in dict_for_tables.keys():
        ...
        with open(containing_folder + "/" + "flows_tables" +"/" + k + ".rst", "w", encoding="utf-8") as f:

            table = dict_for_tables[k]

            for i in range(len(table)):
                table[i][0] = '``'+table[i][0]+'``'

            multiline_rows = split_multiline_cells(table)
            max_length_cells = split_too_long_cells(multiline_rows, maxlen = 40)
            f.write(get_grid_table(max_length_cells, notitleline = True))

if __name__ == "__main__":
    main()
