import pywincalc
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

clear_3_path = "CLEAR_3.DAT"
clear_3 = pywincalc.parse_optics_file(clear_3_path)
solid_layers = [clear_3] * 2
#DEFINING SULFUR HEXAFLOURIDE
sulfur_hexafluoride_conductivity_a = 0.013
sulfur_hexafluoride_conductivity_b = 0
sulfur_hexafluoride_conductivity_c = 0
sulfur_hexafluoride_conductivity_coefficients = pywincalc.GasCoefficients(sulfur_hexafluoride_conductivity_a,
                                                                          sulfur_hexafluoride_conductivity_b,
                                                                          sulfur_hexafluoride_conductivity_c)
sulfur_hexafluoride_viscosity_a = 7.214E-7
sulfur_hexafluoride_viscosity_b = 4.928E-8
sulfur_hexafluoride_viscosity_c = 0
sulfur_hexafluoride_viscosity_coefficients = pywincalc.GasCoefficients(sulfur_hexafluoride_viscosity_a,
                                                                       sulfur_hexafluoride_viscosity_b,
                                                                       sulfur_hexafluoride_viscosity_c)
sulfur_hexafluoride_Cp_a = 418.6
sulfur_hexafluoride_Cp_b = 0
sulfur_hexafluoride_Cp_c = 0
sulfur_hexafluoride_Cp_coefficients = pywincalc.GasCoefficients(sulfur_hexafluoride_Cp_a,
                                                                sulfur_hexafluoride_Cp_b,
                                                                sulfur_hexafluoride_Cp_c)
sulfur_hexafluoride_molecular_weight = 146.1
sulfur_hexafluoride_specific_heat_ratio = 1

sulfur_hexafluoride = pywincalc.GasData("sulfur_hexafluoride",
                                        molecular_weight=sulfur_hexafluoride_molecular_weight,
                                        specific_heat_ratio=sulfur_hexafluoride_specific_heat_ratio,
                                        Cp=sulfur_hexafluoride_Cp_coefficients,
                                        thermal_conductivity=sulfur_hexafluoride_conductivity_coefficients,
                                        viscosity=sulfur_hexafluoride_viscosity_coefficients)



#DEFINING CO2
carbon_dioxide_conductivity_a= 0.00037000
carbon_dioxide_conductivity_b= 0.00002954
carbon_dioxide_conductivity_c= 0.00000008
carbon_dioxide_conductivity_coefficient =  pywincalc.GasCoefficients(carbon_dioxide_conductivity_a,carbon_dioxide_conductivity_b,carbon_dioxide_conductivity_c)

carbon_dioxide_viscosity_a= -0.00000116
carbon_dioxide_viscosity_b= 0.00000006
carbon_dioxide_viscosity_c= 0.00000000
carbon_dioxide_viscosity_coefficient = pywincalc.GasCoefficients(carbon_dioxide_viscosity_a,carbon_dioxide_viscosity_b,carbon_dioxide_viscosity_c)

carbon_dioxide_Cp_a = 558.84997559
carbon_dioxide_Cp_b = 1.04960001
carbon_dioxide_Cp_c = -0.00023876
carbon_dioxide_Cp_coefficient = pywincalc.GasCoefficients(carbon_dioxide_Cp_a,carbon_dioxide_Cp_b,carbon_dioxide_Cp_c)
 
carbon_dioxide_molecular_weight = 44.010
carbon_dioxide_specifc_heat_ratio = 1.289


carbon_dioxide = pywincalc.GasData("carbon_dioxide",
                                        molecular_weight=carbon_dioxide_molecular_weight,
                                        specific_heat_ratio=carbon_dioxide_specifc_heat_ratio,
                                        Cp=carbon_dioxide_Cp_coefficient,
                                        thermal_conductivity=carbon_dioxide_conductivity_coefficient,
                                        viscosity=carbon_dioxide_viscosity_coefficient)

import pywincalc
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# Define the gases and their properties

# ... (Rest of the gases' definitions)

# Create a list of thickness values ranging from 0 mm to 40 mm with 2000 points in the middle
num_points = 50
thickness_values = np.linspace(0.001, 0.04, num_points)

# Define the gases and their properties
gas_Ar = pywincalc.create_gas([[0.90, pywincalc.PredefinedGasType.ARGON], [0.1, pywincalc.PredefinedGasType.AIR]])
gas_Kr = pywincalc.create_gas([[0.90, pywincalc.PredefinedGasType.KRYPTON], [0.1, pywincalc.PredefinedGasType.AIR]])
gas_Xe = pywincalc.create_gas([[0.90, pywincalc.PredefinedGasType.XENON], [0.1, pywincalc.PredefinedGasType.AIR]])

# Define the new gases
gas_SF6 = pywincalc.create_gas([[0.90, sulfur_hexafluoride], [0.1, pywincalc.PredefinedGasType.AIR]])
gas_CO2 = pywincalc.create_gas([[0.90, carbon_dioxide], [0.1, pywincalc.PredefinedGasType.AIR]])

# List of all gases and their labels for the plot
gases = [gas_Ar, gas_Kr, gas_Xe, gas_SF6, gas_CO2]
gas_labels = ["Argon", "Krypton", "Xenon", "Sulfur Hexaflouride", "Carbon Dioxide"]
gas_colors = ["blue", "orange", "green", "purple", "red"]

# Dictionaries to store the U-value results for different gases and thicknesses
u_value_results = {label: {} for label in gas_labels}

# Perform simulations for each gas and store the results
for gas, label in zip(gases, gas_labels):
    for gap_thickness in thickness_values:
        # Create the air gap layer with the specified gas
        gap_layer = pywincalc.Layers.gap(thickness=gap_thickness, gas=gas)

        # Combine the layers to form the glazing system
        glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, gap_layers=[gap_layer])

        # Calculate the U-value for the glazing system
        u_value = glazing_system.u()

        # Store the U-value result for this gas and thickness in the dictionary
        u_value_results[label][gap_thickness] = u_value

# Plot the U-value vs. thickness graph for all gases on the same plot
plt.figure(figsize=(10, 6))

# Set the x-axis ticks to a more exact format
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(base=0.002))  # Ticks every 1 mm
ax.xaxis.set_major_formatter(FormatStrFormatter('%.3f'))  # Format to 3 decimal places
ax.yaxis.set_major_locator(MultipleLocator(base=0.1))  # Ticks every 0.1
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))  # Format to 1 decimal places

# Plot the U-values for each gas on the same graph with different colors and legends
for label, color in zip(gas_labels, gas_colors):
    u_values = list(u_value_results[label].values())
    thickness_list = list(u_value_results[label].keys())
    plt.plot(thickness_list, u_values, label=f"{label} Gas", color=color)

plt.xlabel('Thickness (m)')
plt.ylabel('U-value')
plt.title('U-value vs. Gap Thickness for Glazing System')
plt.grid(True)
plt.legend()

legend_text = []  # Collect the legend text for the custom legend
for label, color in zip(gas_labels, gas_colors):
    gas_min_index = np.argmin(list(u_value_results[label].values()))
    gas_min_u_value = list(u_value_results[label].values())[gas_min_index]
    gas_min_thickness = list(u_value_results[label].keys())[gas_min_index]
    legend_text.append(f"Min U-value ({label}): {gas_min_u_value:.5f} | Thickness: {gas_min_thickness:.5f} m")
    # Highlight the optimal point with red
    plt.scatter(gas_min_thickness, gas_min_u_value, color='red')

# Display the custom legend at the top-left corner
plt.legend(legend_text, loc='upper right')

plt.grid(False)
plt.show()

