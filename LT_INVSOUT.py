import pywincalc
import matplotlib.pyplot as plt
import numpy as np



clear_3_path = "CLEAR_3.DAT"
clear_3 = pywincalc.parse_optics_file(clear_3_path)

solid_layers = [clear_3] * 3

theta = 0  # Incident angle (vertical)
phi = 0    # Azimuth angle (0 degrees for South-facing)
solid_layer_index = 4 #Layer 1: 0 
inside_air_pressure = 101325.0 
inside_convection_coefficient = 0.0
inside_coefficient_model = pywincalc.BoundaryConditionsCoefficientModelType.CALCULATED_H
inside_radiation_temperature = 294.15
inside_emissivity = 1.0
inside_air_speed = 0.0 
inside_air_direction = pywincalc.AirHorizontalDirection.NONE
inside_direct_solar_radiation = 0.0


outside_air_pressure = 101325.0 
outside_convection_coefficient = 26.0
outside_coefficient_model = pywincalc.BoundaryConditionsCoefficientModelType.CALCULATED_H
outside_radiation_temperature = 255.15
outside_emissivity = 1.0
outside_air_speed = 0 
outside_air_direction = pywincalc.AirHorizontalDirection.WINDWARD
outside_direct_solar_radiation = 0.0
inside_temp_l=[]
LT_l = []
LT_l2=[]



for i in range(275,335):
    inside_air_temperature = i
    inside_temp_l = inside_temp_l + [i]
    outside_temp_l = []
    LT_l=[]
    for j in range(275,335):
        outside_air_temperature = j
        outside_temp_l = outside_temp_l+[j]

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

        environmental_conditions = pywincalc.Environments(outside_environment, inside_environment)
        glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, environment=environmental_conditions)
        u_value = glazing_system.u()
        layer_temperatures = glazing_system.layer_temperatures(pywincalc.TarcogSystemType.U, theta=theta, phi=phi)
        # Accessing the temperature of a specific layer (e.g., first solid layer)
        specific_layer_temperature = layer_temperatures[solid_layer_index]
        LT_l = LT_l + [specific_layer_temperature]
    LT_l2 = LT_l2 + [LT_l]
print("U-value for a glazing system with user-defined environmental conditions: {v}".format(v=u_value))
print(len(inside_temp_l),len(outside_temp_l),len(LT_l2))


LT_l2_celsius = [[temp - 273.15 for temp in row] for row in LT_l2]
inside_temp_l_celsius = [temp - 273.15 for temp in inside_temp_l]
outside_temp_l_celsius = [temp - 273.15 for temp in outside_temp_l]

contour = plt.contourf(outside_temp_l_celsius, inside_temp_l_celsius, LT_l2_celsius)
cbar = plt.colorbar(contour)
cbar.set_label('Layer 2 Temperture [°C]')
plt.xlabel('Indoor Temperature [°C]')
plt.ylabel('Outdoor Temperature [°C]')
plt.title('Layer 2 Temperture as a Function of Indoor and Outdoor Temperture')
plt.show()


# clear_3_path = "CLEAR_3.DAT"
# clear_3 = pywincalc.parse_optics_file(clear_3_path)
#
# solid_layers = [clear_3]
#
# glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers)
# print("Single Layer U-value: {u}".format(u=glazing_system.u()))

##Yaxis outside temp, x-axis inside temp = uvalue colour
#Outside air speed and temperure vs u 
##Deflection -18 outside 24 inside 
