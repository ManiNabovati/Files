import pywincalc
import matplotlib.pyplot as plt
import numpy as np

clear_3_path = "CLEAR_3.DAT"
clear_3 = pywincalc.parse_optics_file(clear_3_path)
solid_layers = [clear_3]

inside_air_pressure = 101325.0 
inside_convection_coefficient = 0.0
inside_coefficient_model = pywincalc.BoundaryConditionsCoefficientModelType.CALCULATED_H
inside_radiation_temperature = 294.15
inside_emissivity = 1.0
inside_air_speed = 0.0 
inside_air_direction = pywincalc.AirHorizontalDirection.NONE
inside_direct_solar_radiation = 0.0
inside_air_temperature = 294.15

outside_air_pressure = 101325.0 
outside_convection_coefficient = 26.0
outside_coefficient_model = pywincalc.BoundaryConditionsCoefficientModelType.CALCULATED_H
outside_radiation_temperature = 255.15
outside_emissivity = 1.0
outside_air_direction = pywincalc.AirHorizontalDirection.WINDWARD
outside_direct_solar_radiation = 0.0

# Outside Air+Temp
outside_temp_l = []
u_value_l = []
u_value_l2 = []

for i in range(265, 335):
    outside_air_temperature = i
    outside_temp_l = outside_temp_l + [i]
    outside_air_1 = [] 
    u_value_l = []
    for j in range(0, 23):
        outside_air_speed = j
        outside_air_1 = [j] + outside_air_1

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
        u_value_l = u_value_l + [u_value]
    u_value_l2 = u_value_l2 + [u_value_l]

print("U-value for a glazing system with user-defined environmental conditions: {v}".format(v=u_value))
print(len(outside_air_1), len(outside_temp_l), len(u_value_l2))

contour = plt.contourf(outside_air_1,outside_temp_l , u_value_l2)
cbar = plt.colorbar(contour)
cbar.set_label('U-Value')
plt.xlabel('Outdoor Air Speed [m/s]')
plt.ylabel('Outdoor Temperature [K]')
plt.title('U-Value as a Function of Outdoor Temperature and Air Speed')
plt.show()


         
