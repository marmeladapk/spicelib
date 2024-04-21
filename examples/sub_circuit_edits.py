import os
from spicelib.editor import SpiceEditor

E = SpiceEditor('testfiles\\spice_edit_test.net')
print("Circuit Nodes", E.get_all_nodes())
E.add_library_search_paths([r"C:\SVN\Electronic_Libraries\LTSpice\lib"])
print(E.get_components())
print(E.get_components('R'))
print(E.get_subcircuit('XX1').get_components())
E.set_component_value("XX1:L1", 2e-6)
print(E.get_component_value('R1'))
print("Setting R1 to 10k")
E.set_component_value('R1', 10000)
print("Setting parameter I1 1.23k")
E.set_parameter("V1", "PULSE(0 1 1n 1n 1n {0.5/freq} {1/freq} 10)")
print(E.get_parameter('V1'))
print("Setting frequency to 1MHz")
E.set_parameters(freq=1E6)
print("Setting XX1:L1 to 1µH")
E.set_component_value("XX1:L1", '1µH')
print("Setting XX1:C1 to 22nF")
E.set_component_value("XX1:C1", 22e-9)
print("Setting XX1:C2 to 120nF")
E.set_component_value("XX1:C2", '120n')
print(E.get_component_floatvalue("XX1:C1"))
print(E.get_component_floatvalue("XX1:C2"))
print(E.get_component_floatvalue("XX1:L1"))
print(E.get_component_floatvalue("R2"))
E.set_parameters(
    test_exiting_param_set1=24,
    test_exiting_param_set2=25,
    test_exiting_param_set3=26,
    test_exiting_param_set4=27,
    test_add_parameter=34.45, )
E.save_netlist("testfiles\\spice_edit_test_edit.net")