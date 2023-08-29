import pywincalc
import matplotlib.pyplot as plt
import numpy as np
inside_air_temperature = 294.15
inside_air_pressure = 101325.0
inside_convection_coefficient = 0.0
inside_coefficient_model = pywincalc.BoundaryConditionsCoefficientModelType.CALCULATED_H
inside_radiation_temperature = 294.15
inside_emissivity = 1.0
inside_air_speed = 0.0
inside_air_direction = pywincalc.AirHorizontalDirection.NONE
inside_direct_solar_radiation = 0.0

outside_air_temperature = 298.15 #Toronto Average Summer Temperature
outside_air_pressure = 101325.0
outside_convection_coefficient = 26.0
outside_coefficient_model = pywincalc.BoundaryConditionsCoefficientModelType.CALCULATED_H
outside_radiation_temperature = 255.15
outside_emissivity = 1.0
outside_air_speed = 5.0
outside_air_direction = pywincalc.AirHorizontalDirection.WINDWARD
outside_direct_solar_radiation = 0.0

inside_environment = pywincalc.Environment(air_temperature=inside_air_temperature, pressure=inside_air_pressure,
                                           convection_coefficient=inside_convection_coefficient,
                                           coefficient_model=inside_coefficient_model,
                                           radiation_temperature=inside_radiation_temperature,
                                           emissivity=inside_emissivity, air_speed=inside_air_speed,
                                           air_direction=inside_air_direction,
                                           direct_solar_radiation=inside_direct_solar_radiation)

outside_environment = pywincalc.Environment(air_temperature=outside_air_temperature, pressure=outside_air_pressure,
                                           convection_coefficient=outside_convection_coefficient,
                                           coefficient_model=outside_coefficient_model,
                                           radiation_temperature=outside_radiation_temperature,
                                           emissivity=outside_emissivity, air_speed=outside_air_speed,
                                           air_direction=outside_air_direction,
                                           direct_solar_radiation=outside_direct_solar_radiation)



clear_3_path = "CLEAR_3.DAT"
clear_3 = pywincalc.parse_optics_file(clear_3_path)

ss_3_F_path = "SS-8966-Hastings.txt"
ss_3_F = pywincalc.parse_optics_file(ss_3_F_path)

ss_3_B_path = "SS-8966-Hastings_Back.txt"
ss_3_B = pywincalc.parse_optics_file(ss_3_B_path)

ds_3_F_path = "DS-8563-Hastings.txt"
ds_3_F = pywincalc.parse_optics_file(ds_3_F_path)

ds_3_B_path = "DS-8563-Hastings_Back.txt"
ds_3_B = pywincalc.parse_optics_file(ds_3_B_path)

PMMA_3_path = "PMMA-MR2.txt"
PMMA_3 = pywincalc.parse_optics_file(PMMA_3_path)

# Define the solid layers for each window construction
construction1_layers = [clear_3, PMMA_3, clear_3]
construction2_layers = [ss_3_B, PMMA_3, ss_3_F]
construction3_layers = [ds_3_B, PMMA_3, ds_3_F]
#Inserts 1C
construction4_layers = [clear_3, ss_3_B, clear_3]
construction5_layers = [clear_3, ss_3_F, clear_3]
construction6_layers = [clear_3, clear_3, ss_3_B]
construction7_layers = [clear_3, clear_3, ss_3_F]

construction8_layers = [clear_3, ds_3_B, clear_3]
construction9_layers = [clear_3, ds_3_F, clear_3]
construction10_layers = [clear_3, clear_3, ds_3_B]
construction11_layers = [clear_3, clear_3, ds_3_F]

#Inserts 2C
construction12_layers = [clear_3, ss_3_B, ss_3_B]
construction13_layers = [clear_3, ss_3_F, ss_3_F]
construction14_layers = [clear_3, ss_3_F, ss_3_B]
construction15_layers = [clear_3, ss_3_B, ss_3_F]

construction16_layers = [clear_3, ds_3_B, ds_3_B]
construction17_layers = [clear_3, ds_3_F, ds_3_F]
construction18_layers = [clear_3, ds_3_F, ds_3_B]
construction19_layers = [clear_3, ds_3_B, ds_3_F]


construction20_layers = [clear_3, ss_3_B, ds_3_B]
construction21_layers = [clear_3, ss_3_F, ds_3_B]
construction22_layers = [clear_3, ss_3_B, ds_3_F]
construction23_layers = [clear_3, ss_3_F, ds_3_F]


construction24_layers = [clear_3, ds_3_B, ss_3_B]
construction25_layers = [clear_3, ds_3_F, ss_3_B]
construction26_layers = [clear_3, ds_3_B, ss_3_F]
construction27_layers = [clear_3, ds_3_F, ss_3_F]

# Define the gap thickness range
t = 0.030
x_values = np.linspace(-t/2, t/2, 20)

gas_Kr = pywincalc.create_gas([[0.90, pywincalc.PredefinedGasType.KRYPTON], [0.1, pywincalc.PredefinedGasType.AIR]])
gas_Ar = pywincalc.create_gas([[0.90, pywincalc.PredefinedGasType.ARGON], [0.1, pywincalc.PredefinedGasType.AIR]])

def simulate_middle_layer_temperature(layers):
    solid_layer_index1 = 2  # Middle Layer Index
    solid_layer_index2 = 3 # Middle Layer Index
    LT_results = []
    for x in x_values:
        gap_1 = pywincalc.Layers.gap(thickness=x+t/2+0.00001)
        gap_2 = pywincalc.Layers.gap(thickness=-x+t/2+0.00001, gas = gas_Kr)
        environmental_conditions = pywincalc.Environments(outside_environment, inside_environment)

        glazing_system = pywincalc.GlazingSystem(solid_layers=layers, gap_layers=[gap_1, gap_2],environment=environmental_conditions)
        layer_temperatures = glazing_system.layer_temperatures(pywincalc.TarcogSystemType.U, theta=0, phi=0)
        specific_layer_temperature = ((layer_temperatures[solid_layer_index1]+layer_temperatures[solid_layer_index2])/2) - 273.15  # Convert to Celsius
        LT_results.append(specific_layer_temperature)

    return LT_results

# Simulate middle layer temperature for each construction by calling on the simulate_middle_layer_temperature function
'''

construction4_LT = simulate_middle_layer_temperature(construction4_layers)
construction5_LT = simulate_middle_layer_temperature(construction5_layers)
construction6_LT = simulate_middle_layer_temperature(construction6_layers)
construction7_LT = simulate_middle_layer_temperature(construction7_layers)
construction8_LT = simulate_middle_layer_temperature(construction8_layers)
construction9_LT = simulate_middle_layer_temperature(construction9_layers)
construction10_LT = simulate_middle_layer_temperature(construction10_layers)
construction11_LT = simulate_middle_layer_temperature(construction11_layers)
construction12_LT = simulate_middle_layer_temperature(construction12_layers)
construction13_LT = simulate_middle_layer_temperature(construction13_layers)
construction14_LT = simulate_middle_layer_temperature(construction14_layers)
construction15_LT = simulate_middle_layer_temperature(construction15_layers)
construction16_LT = simulate_middle_layer_temperature(construction16_layers)
construction17_LT = simulate_middle_layer_temperature(construction17_layers)
construction18_LT = simulate_middle_layer_temperature(construction18_layers)
construction19_LT = simulate_middle_layer_temperature(construction19_layers)
construction20_LT = simulate_middle_layer_temperature(construction20_layers)
construction21_LT = simulate_middle_layer_temperature(construction21_layers)
construction22_LT = simulate_middle_layer_temperature(construction22_layers)
construction23_LT = simulate_middle_layer_temperature(construction23_layers)
construction24_LT = simulate_middle_layer_temperature(construction24_layers)
construction25_LT = simulate_middle_layer_temperature(construction25_layers)
construction26_LT = simulate_middle_layer_temperature(construction26_layers)
construction27_LT = simulate_middle_layer_temperature(construction27_layers)


'''
construction24_LT = simulate_middle_layer_temperature(construction24_layers)
construction25_LT = simulate_middle_layer_temperature(construction25_layers)
construction26_LT = simulate_middle_layer_temperature(construction26_layers)
construction27_LT = simulate_middle_layer_temperature(construction27_layers)
# Plot the middle layer temperature for all constructions



'''



plt.plot(x_values, construction12_LT, label='Clear_3 - ss_3_B - ss_3_B')
plt.plot(x_values, construction13_LT, label='Clear_3 - ss_3_F - ss_3_F')
plt.plot(x_values, construction14_LT, label='Clear_3 - ss_3_F - ss_3_B')
plt.plot(x_values, construction15_LT, label='Clear_3 - ss_3_B - ss_3_F')
plt.plot(x_values, construction16_LT, label='Clear_3 - ds_3_B - ds_3_B')
plt.plot(x_values, construction17_LT, label='Clear_3 - ds_3_F - ds_3_F')
plt.plot(x_values, construction18_LT, label='Clear_3 - ds_3_F - ds_3_B')
plt.plot(x_values, construction19_LT, label='Clear_3 - ds_3_B - ds_3_F')
plt.plot(x_values, construction20_LT, label='Clear_3 - ss_3_B - ds_3_B')
plt.plot(x_values, construction21_LT, label='Clear_3 - ss_3_F - ds_3_B')
plt.plot(x_values, construction22_LT, label='Clear_3 - ss_3_B - ds_3_F')
plt.plot(x_values, construction23_LT, label='Clear_3 - ss_3_F - ds_3_F')
plt.plot(x_values, construction24_LT, label='Clear_3 - ds_3_B - ss_3_B')
plt.plot(x_values, construction25_LT, label='Clear_3 - ds_3_F - ss_3_B')
plt.plot(x_values, construction26_LT, label='Clear_3 - ds_3_B - ss_3_F')
plt.plot(x_values, construction27_LT, label='Clear_3 - ds_3_F - ss_3_F')



'''
plt.plot(x_values, construction24_LT, label='Clear_3 - ds_3_B - ss_3_B')
plt.plot(x_values, construction25_LT, label='Clear_3 - ds_3_F - ss_3_B')
plt.plot(x_values, construction26_LT, label='Clear_3 - ds_3_B - ss_3_F')
plt.plot(x_values, construction27_LT, label='Clear_3 - ds_3_F - ss_3_F')

plt.xlabel('Gap Thickness (x) [m]')
plt.ylabel('Middle Layer Temperature [°C]')
plt.title('30mm: Double Coated Surface Insert Middle Layer Temperature vs Gap Thickness - Gap 2 Krypton (4)')
plt.legend()
plt.grid(True)
plt.show()

