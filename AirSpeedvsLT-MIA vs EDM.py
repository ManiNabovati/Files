import pywincalc
import matplotlib.pyplot as plt
import numpy as np



clear_3_path = "CLEAR_3.DAT"
clear_3 = pywincalc.parse_optics_file(clear_3_path)

solid_layers = [clear_3]*3

theta = 0  # Incident angle (vertical)
phi = 0    # Azimuth angle (0 degrees for South-facing)
solid_layer_index = 3 #Layer 1

##Weather data from: https://www.currentresults.com/Weather/Canada/Alberta/Places/edmonton-temperatures-by-month-average.php

inside_air_pressure = 101325.0
inside_temp = 294.15
inside_convection_coefficient = 0.0
inside_coefficient_model = pywincalc.BoundaryConditionsCoefficientModelType.CALCULATED_H
inside_radiation_temperature = 294.15
inside_emissivity = 1.0
inside_air_speed = 0.0 
inside_air_direction = pywincalc.AirHorizontalDirection.NONE
inside_direct_solar_radiation = 0.0


outside_air_pressure = 101325.0
outside_temp_H_MIA = 306.15
outside_temp_L_MIA = 289.15
outside_temp_H_EDM = 297.15
outside_temp_L_EDM = 259.15

outside_convection_coefficient = 26.0
outside_coefficient_model = pywincalc.BoundaryConditionsCoefficientModelType.CALCULATED_H
outside_radiation_temperature = 255.15
outside_emissivity = 1.0
outside_air_direction = pywincalc.AirHorizontalDirection.WINDWARD
outside_direct_solar_radiation = 0.0


num_points = 1600
outside_air_speed_values = np.linspace(0, 23, num_points)

LT_results = {} #dictionary to hold layer temperture results results


for outside_air_speed in outside_air_speed_values:
    inside_environment = pywincalc.Environment(air_temperature=inside_temp, pressure=inside_air_pressure,
                                           convection_coefficient=inside_convection_coefficient,
                                           coefficient_model=inside_coefficient_model,
                                           radiation_temperature=inside_radiation_temperature,
                                           emissivity=inside_emissivity, air_speed=inside_air_speed,
                                           air_direction=inside_air_direction,
                                           direct_solar_radiation=inside_direct_solar_radiation)

    outside_environment = pywincalc.Environment(air_temperature=outside_temp_L_MIA,
                                                pressure=outside_air_pressure,
                                                convection_coefficient=outside_convection_coefficient,
                                                coefficient_model=outside_coefficient_model,
                                                radiation_temperature=outside_radiation_temperature,
                                                emissivity=outside_emissivity,
                                                air_speed=outside_air_speed, 
                                                air_direction=outside_air_direction,
                                                direct_solar_radiation=outside_direct_solar_radiation)

    environmental_conditions = pywincalc.Environments(outside_environment, inside_environment)
    glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, environment=environmental_conditions)
    u_value = glazing_system.u()
    layer_temperatures = glazing_system.layer_temperatures(pywincalc.TarcogSystemType.U, theta=theta, phi=phi)
    specific_layer_temperature = layer_temperatures[solid_layer_index]
    LT_results[outside_air_speed] = specific_layer_temperature

outside_air_speed_values_plot = []
layer_temperature_values = []



for outside_air_speed, specific_layer_temperature in LT_results.items():
    outside_air_speed_values_plot.append(outside_air_speed)
    layer_temperature_values.append(specific_layer_temperature)

layer_temperature_values_celsius = [temp - 273.15 for temp in layer_temperature_values]

# Perform quadratic regression (2nd-degree polynomial)
coefficients = np.polyfit(outside_air_speed_values_plot, layer_temperature_values_celsius, deg=2)
slope = coefficients[0]  # Coefficient of the linear term (1st-degree coefficient)
slope_label = f'Slope: {slope:.2f} °C/m/s'  # Format the slope value for labeling

# Create the plot
plt.plot(outside_air_speed_values_plot, layer_temperature_values_celsius, marker='o')
plt.xlabel('Outside Air Speed (m/s)')
plt.ylabel('Layer Temperature (°C)')
plt.title('Layer Temperature vs. Outside Air Speed: Miami Low')
plt.grid(True)

# Add the slope as text to the graph
plt.text(0.3, 0.9, slope_label, transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
