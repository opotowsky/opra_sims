SIMULATION = {'simulation': {'control': {'duration': 1200, 'startmonth': 1, 'startyear': 2022, 'dt': 86400}, 'archetypes': {'spec': [{'lib': 'cycamore', 'name': 'Source'}, {'lib': 'cycamore', 'name': 'Enrichment'}, {'lib': 'cycamore', 'name': 'Mixer'}, {'lib': 'cycamore', 'name': 'Reactor'}, {'lib': 'cycamore', 'name': 'Storage'}, {'lib': 'cycamore', 'name': 'Separations'}, {'lib': 'cycamore', 'name': 'Sink'}, {'lib': 'cycamore', 'name': 'DeployInst'}, {'lib': 'cycamore', 'name': 'ManagerInst'}, {'lib': 'cycamore', 'name': 'GrowthRegion'}]}, 'region': {'name': 'GrowthRegion', 'config': {'GrowthRegion': {'growth': {'item': [{'commod': 'PowerLWR', 'piecewise_function': {'piece': [{'start': 18, 'function': {'type': 'linear', 'params': '0 100000'}}, {'start': 180, 'function': {'type': 'linear', 'params': '-105 0'}}]}}, {'commod': 'PowerSFR', 'piecewise_function': {'piece': [{'start': 180, 'function': {'type': 'linear', 'params': '105 0'}}]}}]}}}, 'institution': [{'name': 'InitFleet', 'config': {'DeployInst': {'prototypes': {'val': ['LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR', 'LWR']}, 'n_build': {'val': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, 'build_times': {'val': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17]}, 'lifetimes': {'val': [18, 23, 28, 33, 38, 43, 48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98, 103, 108, 113, 118, 123, 128, 133, 138, 143, 148, 153, 158, 163, 168, 173, 178, 183, 188, 193, 198, 203, 208, 213, 218, 223, 228, 233, 238, 243, 248, 253, 258, 263, 268, 273, 278, 283, 288, 293, 298, 303, 308, 313, 318, 323, 328, 333, 338, 343, 348, 353, 358, 363, 368, 373, 378, 383, 388, 393, 398, 403, 408, 413, 418, 423, 428, 433, 438, 443, 448, 453, 458, 463, 468, 473, 478, 483, 488, 493, 498, 503, 508, 513]}}}}, {'name': 'FCInstEG01-23', 'initialfacilitylist': {'entry': [{'number': 1, 'prototype': 'SourceInitUOX'}, {'number': 1, 'prototype': 'SourceNatU'}, {'number': 1, 'prototype': 'SourceNonIsos'}, {'number': 1, 'prototype': 'SourceAddIsos'}, {'number': 1, 'prototype': 'Enrichment'}, {'number': 1, 'prototype': 'StorageDepU'}, {'number': 1, 'prototype': 'UOXStrNon'}, {'number': 1, 'prototype': 'UOXMixNon'}, {'number': 1, 'prototype': 'UOXStrAdd'}, {'number': 1, 'prototype': 'UOXMixAdd'}, {'number': 1, 'prototype': 'UOXCoolNon'}, {'number': 1, 'prototype': 'UOXCoolAdd'}, {'number': 1, 'prototype': 'Waste'}]}, 'config': {'ManagerInst': {'prototypes': {'val': ['SourceNatU', 'SourceNonIsos', 'SourceAddIsos', 'Enrichment', 'StorageDepU', 'UOXStrNon', 'UOXMixNon', 'UOXStrAdd', 'UOXMixAdd', 'LWR', 'UOXCoolNon', 'UOXCoolAdd', 'Waste', 'SFR']}}}}, {'name': 'EG23Deploy', 'config': {'DeployInst': {'prototypes': {'val': ['UOXSep', 'FFMixNon', 'FFMixAdd', 'FFCoolNon', 'FFCoolAdd', 'FFSep']}, 'n_build': {'val': [1, 1, 1, 1, 1, 1]}, 'build_times': {'val': [180, 180, 180, 180, 180, 180]}}}}]}, 'facility': [{'name': 'SourceInitUOX', 'config': {'Source': {'outcommod': 'InitUOX', 'outrecipe': 'UOX_no232', 'inventory_size': 8869500}}}, {'name': 'SourceNatU', 'config': {'Source': {'outcommod': 'NatU', 'outrecipe': 'NU', 'throughput': 210000000000.0}}}, {'name': 'SourceNonIsos', 'config': {'Source': {'outcommod': 'NonIsos', 'outrecipe': 'NoAdditive_234', 'throughput': 1000000.0}}}, {'name': 'SourceAddIsos', 'config': {'Source': {'outcommod': 'AddIsos', 'outrecipe': 'Additive_232_233_234', 'throughput': 1000000.0}}}, {'name': 'Enrichment', 'config': {'Enrichment': {'feed_commod': 'NatU', 'feed_recipe': 'NU', 'product_commod': 'AlmostUOX', 'tails_commod': 'DepU', 'tails_assay': 0.0025, 'swu_capacity': 1e+100, 'initial_feed': 1e+100}}}, {'name': 'StorageDepU', 'config': {'Storage': {'in_commods': {'val': 'DepU'}, 'in_recipe': 'DU', 'out_commods': {'val': 'StoredDepU'}, 'residence_time': 0}}}, {'name': 'UOXStrNon', 'config': {'Storage': {'in_commods': {'val': 'AlmostUOX'}, 'in_recipe': 'AlmostUOX_no232', 'out_commods': {'val': 'AlmostUOX_Non'}, 'residence_time': 0, 'throughput': 100000000.0, 'max_inv_size': 10000000000.0}}}, {'name': 'UOXMixNon', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.0004631049477, 'buf_size': 1000000.0}, 'commodities': {'item': {'commodity': 'NonIsos', 'pref': 1.0}}}, {'info': {'mixing_ratio': 0.9995368950523, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'AlmostUOX_Non', 'pref': 1.0}}}]}, 'out_commod': 'UOX_Non', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'UOXStrAdd', 'config': {'Storage': {'in_commods': {'val': 'AlmostUOX'}, 'in_recipe': 'AlmostUOX_232', 'out_commods': {'val': 'AlmostUOX_Add'}, 'residence_time': 0, 'throughput': 100000000.0, 'max_inv_size': 10000000000.0}}}, {'name': 'UOXMixAdd', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.0004631072127, 'buf_size': 1000000.0}, 'commodities': {'item': {'commodity': 'AddIsos', 'pref': 1.0}}}, {'info': {'mixing_ratio': 0.9995368927873, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'AlmostUOX_Add', 'pref': 1.0}}}]}, 'out_commod': 'UOX_Add', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'LWR', 'lifetime': 720, 'config': {'Reactor': {'fuel_incommods': {'val': ['UOX_Add', 'UOX_Non', 'InitUOX']}, 'fuel_outcommods': {'val': ['SpentUOX_Add', 'SpentUOX_Non', 'SpentUOX_Non']}, 'fuel_inrecipes': {'val': ['UOX_232', 'UOX_no232', 'UOX_no232']}, 'fuel_outrecipes': {'val': ['SpentUOX_232', 'SpentUOX_no232', 'SpentUOX_no232']}, 'fuel_prefs': {'val': [1, 2, 2.5]}, 'pref_change_times': {'val': 60}, 'pref_change_commods': {'val': 'UOX_Add'}, 'pref_change_values': {'val': 3}, 'cycle_time': 18, 'refuel_time': 0, 'assem_size': 29565, 'n_assem_core': 3, 'n_assem_batch': 1, 'power_name': 'PowerLWR', 'power_cap': 1000}}}, {'name': 'UOXCoolNon', 'config': {'Storage': {'in_commods': {'val': 'SpentUOX_Non'}, 'out_commods': {'val': 'CooledSpentUOX_Non'}, 'in_recipe': 'SpentUOX_no232', 'residence_time': 81}}}, {'name': 'UOXCoolAdd', 'config': {'Storage': {'in_commods': {'val': 'SpentUOX_Add'}, 'out_commods': {'val': 'CooledSpentUOX_Add'}, 'in_recipe': 'SpentUOX_232', 'residence_time': 81}}}, {'name': 'UOXSep', 'config': {'Separations': {'leftover_commod': 'Waste', 'throughput': 83333.3333, 'feedbuf_size': 107537, 'feed_commods': {'val': ['CooledSpentUOX_Non', 'CooledSpentUOX_Add']}, 'feed_commod_prefs': {'val': [1, 2]}, 'streams': {'item': [{'commod': 'UOX_Pu', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': {'comp': 'Pu239', 'eff': 0.99}}}}, {'commod': 'UOX_RU', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': {'comp': 'U238', 'eff': 0.99}}}}]}}}}, {'name': 'FFMixNon', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.09, 'buf_size': 100000000.0}, 'commodities': {'item': [{'commodity': 'UOX_Pu', 'pref': 1}, {'commodity': 'FF_Pu', 'pref': 1}]}}, {'info': {'mixing_ratio': 0.71, 'buf_size': 100000000.0}, 'commodities': {'item': [{'commodity': 'UOX_RU', 'pref': 1}, {'commodity': 'FF_RU', 'pref': 1}]}}, {'info': {'mixing_ratio': 0.1995, 'buf_size': 100000000.0}, 'commodities': {'item': [{'commodity': 'StoredDepU', 'pref': 2}, {'commodity': 'NatU', 'pref': 1}]}}, {'info': {'mixing_ratio': 0.0005, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'NonIsos', 'pref': 1}}}]}, 'out_commod': 'FF_Non', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'FFMixAdd', 'config': {'Mixer': {'in_streams': {'stream': [{'info': {'mixing_ratio': 0.09, 'buf_size': 100000000.0}, 'commodities': {'item': [{'commodity': 'UOX_Pu', 'pref': 1}, {'commodity': 'FF_Pu', 'pref': 1}]}}, {'info': {'mixing_ratio': 0.71, 'buf_size': 100000000.0}, 'commodities': {'item': [{'commodity': 'UOX_RU', 'pref': 1}, {'commodity': 'FF_RU', 'pref': 1}]}}, {'info': {'mixing_ratio': 0.1995, 'buf_size': 100000000.0}, 'commodities': {'item': [{'commodity': 'StoredDepU', 'pref': 2}, {'commodity': 'NatU', 'pref': 1}]}}, {'info': {'mixing_ratio': 0.0005, 'buf_size': 100000000.0}, 'commodities': {'item': {'commodity': 'AddIsos', 'pref': 1}}}]}, 'out_commod': 'FF_Add', 'throughput': 10000000000.0, 'out_buf_size': 1e+20}}}, {'name': 'SFR', 'lifetime': 720, 'config': {'Reactor': {'fuel_incommods': {'val': ['FF_Non', 'FF_Add']}, 'fuel_outcommods': {'val': ['SpentFF_Non', 'SpentFF_Add']}, 'fuel_inrecipes': {'val': ['FF_no232', 'FF_232']}, 'fuel_outrecipes': {'val': ['SpentFF_no232', 'SpentFF_232']}, 'fuel_prefs': {'val': [1, 2]}, 'cycle_time': 14, 'refuel_time': 0, 'assem_size': 7490, 'n_assem_core': 5, 'n_assem_batch': 1, 'power_name': 'PowerSFR', 'power_cap': 400}}}, {'name': 'FFSep', 'config': {'Separations': {'leftover_commod': 'Waste', 'throughput': 83333.3333, 'feedbuf_size': 107537, 'feed_commods': {'val': ['CooledSpentFF_Non', 'CooledSpentFF_Add']}, 'feed_commod_prefs': {'val': [1, 2]}, 'streams': {'item': [{'commod': 'FF_Pu', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': {'comp': 'Pu239', 'eff': 0.99}}}}, {'commod': 'FF_RU', 'info': {'buf_size': 1e+100, 'efficiencies': {'item': {'comp': 'U238', 'eff': 0.99}}}}]}}}}, {'name': 'FFCoolNon', 'config': {'Storage': {'in_commods': {'val': 'SpentFF_Non'}, 'out_commods': {'val': 'CooledSpentFF_Non'}, 'in_recipe': 'SpentFF_no232', 'residence_time': 81}}}, {'name': 'FFCoolAdd', 'config': {'Storage': {'in_commods': {'val': 'SpentFF_Add'}, 'out_commods': {'val': 'CooledSpentFF_Add'}, 'in_recipe': 'SpentFF_232', 'residence_time': 81}}}, {'name': 'Waste', 'config': {'Sink': {'in_commods': {'val': 'Waste'}}}}], 'recipe': [{'name': 'DU', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.0025}, {'id': 'U238', 'comp': 0.9975}]}, {'name': 'NU', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.00711}, {'id': 'U238', 'comp': 0.99289}]}, {'name': 'NoAdditive_234', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 1.0}]}, {'name': 'Additive_232_233_234', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1.0434e-09}, {'id': 'U233', 'comp': 1.2228e-09}, {'id': 'U234', 'comp': 0.0004631049466}]}, {'name': 'AlmostUOX_no232', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.049906230293}, {'id': 'U238', 'comp': 0.9496306647594}]}, {'name': 'AlmostUOX_232', 'basis': 'mass', 'nuclide': [{'id': 'U235', 'comp': 0.0499062301796}, {'id': 'U238', 'comp': 0.9496306626077}]}, {'name': 'UOX_no232', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 0.0004631049477}, {'id': 'U235', 'comp': 0.049906230293}, {'id': 'U238', 'comp': 0.9496306647594}]}, {'name': 'UOX_232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1.0434e-09}, {'id': 'U233', 'comp': 1.2228e-09}, {'id': 'U234', 'comp': 0.0004631049466}, {'id': 'U235', 'comp': 0.0499062301796}, {'id': 'U238', 'comp': 0.9496306626077}]}, {'name': 'SpentUOX_no232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 2.838e-10}, {'id': 'U233', 'comp': 5.8245e-09}, {'id': 'U234', 'comp': 0.0002961396326}, {'id': 'U235', 'comp': 0.0174611824759}, {'id': 'U236', 'comp': 0.006185388998}, {'id': 'U238', 'comp': 0.9250572827708}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}, {'name': 'SpentUOX_232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 9.065e-10}, {'id': 'U233', 'comp': 6.2943e-09}, {'id': 'U234', 'comp': 0.0002327879338}, {'id': 'U235', 'comp': 0.0175266370423}, {'id': 'U236', 'comp': 0.0062071106222}, {'id': 'U238', 'comp': 0.9250334572009}, {'id': 'Pu239', 'comp': 0.01}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.04}]}, {'name': 'FF_no232', 'basis': 'mass', 'nuclide': [{'id': 'U234', 'comp': 0.0004}, {'id': 'U235', 'comp': 0.004}, {'id': 'U238', 'comp': 0.9056}, {'id': 'Pu239', 'comp': 0.09}]}, {'name': 'FF_232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 1e-09}, {'id': 'U233', 'comp': 1e-09}, {'id': 'U234', 'comp': 0.0004}, {'id': 'U235', 'comp': 0.004}, {'id': 'U238', 'comp': 0.905599998}, {'id': 'Pu239', 'comp': 0.09}]}, {'name': 'SpentFF_no232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 3e-10}, {'id': 'U233', 'comp': 1e-08}, {'id': 'U234', 'comp': 0.0001}, {'id': 'U235', 'comp': 0.0001}, {'id': 'U236', 'comp': 0.0001}, {'id': 'U238', 'comp': 0.8476999897}, {'id': 'Pu239', 'comp': 0.15}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.001}]}, {'name': 'SpentFF_232', 'basis': 'mass', 'nuclide': [{'id': 'U232', 'comp': 9e-10}, {'id': 'U233', 'comp': 1e-08}, {'id': 'U234', 'comp': 0.0001}, {'id': 'U235', 'comp': 0.0001}, {'id': 'U236', 'comp': 0.0001}, {'id': 'U238', 'comp': 0.8476999891}, {'id': 'Pu239', 'comp': 0.15}, {'id': 'Am241', 'comp': 0.001}, {'id': 'Cs137', 'comp': 0.001}]}]}}