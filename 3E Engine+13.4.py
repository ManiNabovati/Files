'''
Developed By Mani Nabovati Khormazard
This program is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/.

You are free to:

- Share: Copy and redistribute the material in any medium or format.
- Adapt: Remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:

- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

No additional restrictions: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Note: This is a summary of the CC BY-SA 4.0 license. For the full license terms, please refer to the provided URL or visit https://creativecommons.org/licenses/by-sa/4.0/legalcode.
'''


import pywincalc
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import os 
import datetime

print("Developed By Mani Nabovati Khormazard\nThis program is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/.\nYou are free to:\n- Share: Copy and redistribute the material in any medium or format.\n- Adapt: Remix, transform, and build upon the material for any purpose, even commercially.\nUnder the following terms:\n- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.\n- ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.\nNo additional restrictions: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.\nNote: This is a summary of the CC BY-SA 4.0 license. For the full license terms, please refer to the provided URL or visit https://creativecommons.org/licenses/by-sa/4.0/legalcode.")



paneB_3 = None

pane = 4

#Substrates 
clear_6_path = "CLEAR_6.DAT"
clear_6 = pywincalc.parse_optics_file(clear_6_path)

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




solid_layers = [clear_3] * pane


temp_MAX_Kuwait = 50
temp_MIN_Kuwait = 45
temp_MAX_Russia = -35
temp_MIN_Russia = -40


current_gas_type = None


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
outside_air_speed = 5.0
outside_air_direction = pywincalc.AirHorizontalDirection.WINDWARD
outside_direct_solar_radiation = 0.0


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



#Gas mixture definitions
gas_Ar = pywincalc.create_gas([[0.90, pywincalc.PredefinedGasType.ARGON],[0.1, pywincalc.PredefinedGasType.AIR]])
gas_Kr = pywincalc.create_gas([[0.90, pywincalc.PredefinedGasType.KRYPTON],[0.1, pywincalc.PredefinedGasType.AIR]])
gas_Xe = pywincalc.create_gas([[0.90, pywincalc.PredefinedGasType.XENON],[0.1, pywincalc.PredefinedGasType.AIR]])
gas_SF6 = pywincalc.create_gas([[0.90, sulfur_hexafluoride],[0.1, pywincalc.PredefinedGasType.AIR]])
gas_CO2 = pywincalc.create_gas([[0.90, carbon_dioxide],[0.1, pywincalc.PredefinedGasType.AIR]])
gas_Air = pywincalc.create_gas([[1.0, pywincalc.PredefinedGasType.AIR]])
u_value_label = None
R_value_label = None
shgc_label = None
root = None



def calculate_u_value(gap_thickness1, gap_thickness2,gap_thickness3, gas, temp_I, temp_O, u_value_label,outside_air_speed):
    global current_gas_type
    if current_gas_type is None:
        # If no gas type is selected, return without calculating the u-value
        return
    if current_gas_type == "argon":
        gas = gas_Ar
    elif current_gas_type == "xenon":
        gas = gas_Xe
    elif current_gas_type == "krypton":
        gas = gas_Kr
    elif current_gas_type =="air":
        gas = gas_Air

    #Kelvin to Celcius 
    temp_I += 273.15
    temp_O += 273.15

    inside_environment = pywincalc.Environment(air_temperature=temp_I, pressure=inside_air_pressure,
                                           convection_coefficient=inside_convection_coefficient,
                                           coefficient_model=inside_coefficient_model,
                                           radiation_temperature=inside_radiation_temperature,
                                           emissivity=inside_emissivity, air_speed=inside_air_speed,
                                           air_direction=inside_air_direction,
                                           direct_solar_radiation=inside_direct_solar_radiation)

    outside_environment = pywincalc.Environment(air_temperature=temp_O, pressure=outside_air_pressure,
                                           convection_coefficient=outside_convection_coefficient,
                                           coefficient_model=outside_coefficient_model,
                                           radiation_temperature=outside_radiation_temperature,
                                           emissivity=outside_emissivity, air_speed=outside_air_speed,
                                           air_direction=outside_air_direction,
                                           direct_solar_radiation=outside_direct_solar_radiation)

    if pane == 4:

        LT_label0.config(text="")
        LT_label1.config(text="")
        LT_label2.config(text="")
        LT_label3.config(text="")
        LT_label4.config(text="")
        LT_label5.config(text="")
        LT_label6.config(text="")
        LT_label7.config(text="")
        gap_layer1 = pywincalc.Layers.gap(thickness=float(gap_thickness1/1000), gas=gas)
        gap_layer2 = pywincalc.Layers.gap(thickness=float(gap_thickness2/1000), gas=gas)
        gap_layer3 = pywincalc.Layers.gap(thickness=float(gap_thickness3/1000), gas=gas)
        environmental_conditions = pywincalc.Environments(outside_environment, inside_environment)
        glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, gap_layers=[gap_layer1, gap_layer2,gap_layer3],environment=environmental_conditions)
        u_value = glazing_system.u()
        u_value_label.config(text=f"U-Value: {u_value:.3f} W/(m²·K)")
        R_value = (1/glazing_system.u()) * 5.678
        R_value_label.config(text=f"R-Value: {R_value:.3f}")
        layer_temperatures = glazing_system.layer_temperatures(pywincalc.TarcogSystemType.U, theta=0, phi=0)
        print(layer_temperatures)
        LT0 =layer_temperatures[0]
        LT1 =layer_temperatures[1]
        LT2 =layer_temperatures[2]
        LT3 =layer_temperatures[3]
        LT4 =layer_temperatures[4]
        LT5 =layer_temperatures[5]
        LT6 =layer_temperatures[6]
        LT7 =layer_temperatures[7] 
        LT_label0.config(text=f"{LT0-273.15 :.3f} °C")       
        LT_label1.config(text=f"{LT1-273.15 :.3f} °C")       
        LT_label2.config(text=f"{LT2-273.15 :.3f} °C")       
        LT_label3.config(text=f"{LT3-273.15 :.3f} °C")       
        LT_label4.config(text=f"{LT4-273.15 :.3f} °C")       
        LT_label5.config(text=f"{LT5-273.15 :.3f} °C")
        LT_label6.config(text=f"{LT6-273.15 :.3f} °C")
        LT_label7.config(text=f"{LT7-273.15 :.3f} °C")

    if pane == 3:

        LT_label0.config(text="")
        LT_label1.config(text="")
        LT_label2.config(text="")
        LT_label3.config(text="")
        LT_label4.config(text="")
        LT_label5.config(text="")
        LT_label6.config(text="")
        LT_label7.config(text="")
        gap_layer1 = pywincalc.Layers.gap(thickness=float(gap_thickness1/1000), gas=gas)
        gap_layer2 = pywincalc.Layers.gap(thickness=float(gap_thickness2/1000), gas=gas)
        environmental_conditions = pywincalc.Environments(outside_environment, inside_environment)
        glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, gap_layers=[gap_layer1, gap_layer2],environment=environmental_conditions)
        u_value = glazing_system.u()
        u_value_label.config(text=f"U-Value: {u_value:.3f} W/(m²·K)")
        R_value = (1/glazing_system.u()) * 5.678
        R_value_label.config(text=f"R-Value: {R_value:.3f}")
        layer_temperatures = glazing_system.layer_temperatures(pywincalc.TarcogSystemType.U, theta=0, phi=0)
        print(layer_temperatures)
        LT0 =layer_temperatures[0]
        LT1 =layer_temperatures[1]
        LT2 =layer_temperatures[2]
        LT3 =layer_temperatures[3]
        LT4 =layer_temperatures[4]
        LT5 =layer_temperatures[5]         
        LT_label0.config(text=f"{LT0-273.15 :.3f} °C")       
        LT_label1.config(text=f"{LT1-273.15 :.3f} °C")       
        LT_label2.config(text=f"{LT2-273.15 :.3f} °C")       
        LT_label3.config(text=f"{LT3-273.15 :.3f} °C")       
        LT_label4.config(text=f"{LT4-273.15 :.3f} °C")       
        LT_label5.config(text=f"{LT5-273.15 :.3f} °C")


    if pane == 2:
        LT_label0.config(text="")
        LT_label1.config(text="")
        LT_label2.config(text="")
        LT_label3.config(text="")
        LT_label4.config(text="")
        LT_label5.config(text="")
        LT_label6.config(text="")
        LT_label7.config(text="")
        gap_layer1 = pywincalc.Layers.gap(thickness=float(gap_thickness1/1000), gas=gas)
        environmental_conditions = pywincalc.Environments(outside_environment, inside_environment)
        glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, gap_layers=[gap_layer1],environment=environmental_conditions)
        u_value = glazing_system.u()
        u_value_label.config(text=f"U-Value: {u_value:.3f} W/(m²·K)")
        R_value = (1/glazing_system.u()) * 5.678
        R_value_label.config(text=f"R-Value: {R_value:.3f}")       
        layer_temperatures = glazing_system.layer_temperatures(pywincalc.TarcogSystemType.U, theta=0, phi=0)
        print(layer_temperatures)
        LT0 =layer_temperatures[0]
        LT1 =layer_temperatures[1]
        LT2 =layer_temperatures[2]
        LT3 =layer_temperatures[3]
        LT_label0.config(text=f"{LT0-273.15 :.3f} °C")       
        LT_label1.config(text=f"{LT1-273.15 :.3f} °C")       
        LT_label2.config(text=f"{LT2-273.15 :.3f} °C")       
        LT_label3.config(text=f"{LT3-273.15 :.3f} °C")


def click1():
    # Update labels' fonts
    LT_label0.config(font=bold_font)
    LT_label1.config(font=bold_font)
    LT_label2.config(font=("Helvetica", 8))
    LT_label3.config(font=("Helvetica", 8))
    LT_label4.config(font=("Helvetica", 8))
    LT_label5.config(font=("Helvetica", 8))
    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(), gap_thickness3.get(),gas_Ar, temp_I.get(), temp_O.get(), u_value_label,outside_air_speed.get())

def click2():
    # Update labels' fonts
    LT_label0.config(font=("Helvetica", 8))
    LT_label1.config(font=("Helvetica", 8))
    LT_label2.config(font=bold_font)
    LT_label3.config(font=bold_font)
    LT_label4.config(font=("Helvetica", 8))
    LT_label5.config(font=("Helvetica", 8))
    LT_label6.config(font=("Helvetica", 8))
    LT_label7.config(font=("Helvetica", 8))
    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(),gap_thickness3.get(), gas_Ar, temp_I.get(), temp_O.get(), u_value_label,outside_air_speed.get())

def click3():
    # Update labels' fonts
    LT_label0.config(font=("Helvetica", 8))
    LT_label1.config(font=("Helvetica", 8))
    LT_label2.config(font=("Helvetica", 8))
    LT_label3.config(font=("Helvetica", 8))
    LT_label4.config(font=bold_font)
    LT_label5.config(font=bold_font)
    LT_label6.config(font=("Helvetica", 8))
    LT_label7.config(font=("Helvetica", 8))
    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(), gap_thickness3.get(),gas_Ar, temp_I.get(), temp_O.get(), u_value_label,outside_air_speed.get())

def click4():
    # Update labels' fonts
    LT_label0.config(font=("Helvetica", 8))
    LT_label1.config(font=("Helvetica", 8))
    LT_label2.config(font=("Helvetica", 8))
    LT_label3.config(font=("Helvetica", 8))
    LT_label4.config(font=("Helvetica", 8))
    LT_label5.config(font=("Helvetica", 8))
    LT_label6.config(font=bold_font)  
    LT_label7.config(font=bold_font)  
    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(), gap_thickness3.get(), gas_Ar, temp_I.get(), temp_O.get(), u_value_label, outside_air_speed.get())

root = tk.Tk()
root.title("Glazing System Calculator")
font = ("Helvetica", 12)
bold_font = ("Helvetica", 9, "bold")


#OUTPUTS: 
window_width = 1400
window_height = 800
root.geometry(f"{window_width}x{window_height}")


#U-value
u_value_label = tk.Label(root, text="", font=("Helvetica", 15))
u_value_label.grid(row=12, column=0, columnspan=2)
#R-value
R_value_label = tk.Label(root, text="", font=("Helvetica", 15))
R_value_label.grid(row=13, column=0, columnspan=2)


column_diff = 3
spacing = 1  # Adjust this value to control the spacing

# File Download Path 
def get_user_input(): #Input the PATH ONLY in the format as shown in this example: C:/Users/Mani/Downloads/Python_Simulation 
    global user_input
    user_input = input_var.get()

input_var = tk.StringVar()
input_entry = tk.Entry(root, textvariable=input_var)
input_entry.grid(row=17, column=0, columnspan=1)
button = tk.Button(root, text="Save File Path", command=get_user_input)
button.grid(row=18, column=0, columnspan=1)


# Create labels for layer temperatures and substrate type
LT_label0 = tk.Label(root, text="", font=("Helvetica", 8))
LT_label0.grid(row=14, column=2, columnspan=3)

LT_label1 = tk.Label(root, text="", font=("Helvetica", 8))
LT_label1.grid(row=14, column=7, columnspan=3)

LT_label2 = tk.Label(root, text="", font=("Helvetica", 8))
LT_label2.grid(row=14, column=12, columnspan=3)

LT_label3 = tk.Label(root, text="", font=("Helvetica", 8))
LT_label3.grid(row=14, column=15, columnspan=3)

LT_label4 = tk.Label(root, text="", font=("Helvetica", 8))
LT_label4.grid(row=14, column=16, columnspan=3)

LT_label5 = tk.Label(root, text="", font=("Helvetica", 8))
LT_label5.grid(row=14, column=18, columnspan=3)

LT_label6 = tk.Label(root, text="", font=("Helvetica", 8))
LT_label6.grid(row=14, column=20, columnspan=2)

LT_label7 = tk.Label(root, text="", font=("Helvetica", 8))
LT_label7.grid(row=14, column=22, columnspan=2)

Graph_label = tk.Label(root, text="", font=("Helvetica", 13,"bold"))
Graph_label.config(text="Plot Generator")  # Set the label text
Graph_label.grid(row=14, column=0, columnspan=1)  # Place the label in the grid


# Calculate the total width needed for the labels and spacing
total_width = (5 + column_diff * 5) + (spacing * 4)

for i in range(total_width):
    root.grid_columnconfigure(i, weight=1)


InT_label  = tk.Label(root, text="Inside Temperature ", font=("Helvetica", 9, "bold"))
InT_label.grid(row=12, column=21, columnspan=2)

InT_label  = tk.Label(root, text="Outisde Temperature ", font=("Helvetica", 9, "bold"))
InT_label.grid(row=12, column=3, columnspan=2)

paneB_1 = tk.Button(root, text="", bg="light blue", command=click1)
paneB_1.place(x=500, y=600, width=23, height=87) 

paneB_2 = tk.Button(root, text="", bg="light blue", command=click2)
paneB_2.place(x=797, y=600, width=23, height=87) 

paneB_3 = tk.Button(root, text="", bg="light blue", command=click3)
paneB_3.place(x=1041, y=600, width=23, height=87) 

paneB_4 = tk.Button(root, text="", bg="light blue", command=click4)
paneB_4.place(x=1329, y=600, width=23, height=87) 




# Gap thickness variables to store the slider values

gap_thickness1 = tk.DoubleVar(value=10.0)  # Set a default value (where the slider begins when the program is first opened)
gap_thickness2 = tk.DoubleVar(value=10.0)  # Set a default value (where the slider begins when the program is first opened)
gap_thickness3 = tk.DoubleVar(value=10.0)  # Set a default value (where the slider begins when the program is first opened)

# Temp variables to store the slider values
temp_I = tk.DoubleVar(value=0.0) 
temp_O = tk.DoubleVar(value=0.0)   

outside_air_speed = tk.DoubleVar(value=0.0)



#PRODUCT DROPDOWN MENU 
def update_solid_layers_pane1(selected_option):
    update_solid_layers(selected_option, p=0)

def update_solid_layers_pane2(selected_option):
    update_solid_layers(selected_option, p=1)

def update_solid_layers_pane3(selected_option):
    update_solid_layers(selected_option, p=2)

def update_solid_layers_pane4(selected_option):
    update_solid_layers(selected_option, p=3)



def update_solid_layers(selected_option, p):
    global solid_layers
    
    if selected_option == "Clear 3mm Glass":
        solid_layers[p] = clear_3
    elif selected_option == "Clear 6mm Glass":
        solid_layers[p] = clear_6
    elif selected_option == "3mm PMMA":
        solid_layers[p] = PMMA_3
    elif selected_option == "3mm SS Hastings F":
        solid_layers[p] = ss_3_F
    elif selected_option == "3mm SS Hastings B":
        solid_layers[p] = ss_3_B
    elif selected_option == "3mm DS Hastings F":
        solid_layers[p] = ds_3_F
    elif selected_option == "3mm DS Hastings B":
        solid_layers[p] = ds_3_B

    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(),gap_thickness3.get(), gas_Ar, temp_I.get(), temp_O.get(), u_value_label,outside_air_speed.get())



options = ["Pane 1", "Clear 3mm Glass", "Clear 6mm Glass", "3mm PMMA", "3mm SS Hastings F","3mm SS Hastings B", "3mm DS Hastings F","3mm DS Hastings B"]
options2 = ["Pane 2", "Clear 3mm Glass", "Clear 6mm Glass", "3mm PMMA", "3mm SS Hastings F","3mm SS Hastings B", "3mm DS Hastings F","3mm DS Hastings B"]
options3 = ["Pane 3", "Clear 3mm Glass", "Clear 6mm Glass", "3mm PMMA", "3mm SS Hastings F","3mm SS Hastings B", "3mm DS Hastings F","3mm DS Hastings B"]
options4 = ["Pane 4", "Clear 3mm Glass", "Clear 6mm Glass", "3mm PMMA", "3mm SS Hastings F","3mm SS Hastings B", "3mm DS Hastings F","3mm DS Hastings B"]

selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Set the default selected option
selected_option2 = tk.StringVar(root)
selected_option2.set(options2[0])  
selected_option3 = tk.StringVar(root)
selected_option3.set(options3[0])  

selected_option_pane1 = tk.StringVar(root)
selected_option_pane1.set(options[0])
product_menu_pane1 = tk.OptionMenu(root, selected_option_pane1, *options, command=lambda option: update_solid_layers(option, p=0))
product_menu_pane1.config(width=20)
product_menu_pane1.grid(row=1, column=16)

selected_option_pane2 = tk.StringVar(root)
selected_option_pane2.set(options2[0])
product_menu_pane2 = tk.OptionMenu(root, selected_option_pane2, *options2, command=lambda option: update_solid_layers(option, p=1))
product_menu_pane2.config(width=20)
product_menu_pane2.grid(row=1, column=18)

selected_option_pane3 = tk.StringVar(root)
selected_option_pane3.set(options3[0])
product_menu_pane3 = tk.OptionMenu(root, selected_option_pane3, *options3, command=lambda option: update_solid_layers(option, p=2))
product_menu_pane3.config(width=20)
product_menu_pane3.grid(row=1, column=20)

selected_option_pane4 = tk.StringVar(root)
selected_option_pane4.set(options4[0])
product_menu_pane4 = tk.OptionMenu(root, selected_option_pane4, *options4, command=lambda option: update_solid_layers(option, p=3))
product_menu_pane4.config(width=20)
product_menu_pane4.grid(row=1, column=22)

    
#PANE BUTTONS


def on_2p_click():
    print("2P button clicked!")
    global pane, paneB_3
    pane = 2
    gap_slider1.config(state='normal')
    gap_slider2.config(state='disabled')
    btn_2p.config(bg="orange", activebackground="green")
    btn_3p.config(bg="SystemButtonFace", activebackground="SystemButtonFace")
    btn_4p.config(bg="SystemButtonFace", activebackground="SystemButtonFace")

    if pane == 2:
        product_menu_pane3.config(state='disabled')
        product_menu_pane4.config(state='disabled')

    paneB_3.destroy()
    paneB_4.destroy()
    btn_G3.config(state="disabled")
    btn_G2.config(state="normal")

    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(),gap_thickness3.get(), gas_Ar, temp_I.get(), temp_O.get(), u_value_label, outside_air_speed.get())



def on_3p_click():
    print("3P button clicked!")
    global pane, paneB_3
    pane = 3
    gap_slider1.config(state='normal')
    gap_slider2.config(state='normal')
    btn_3p.config(bg="orange", activebackground="green")
    btn_2p.config(bg="SystemButtonFace", activebackground="SystemButtonFace")
    btn_4p.config(bg="SystemButtonFace", activebackground="SystemButtonFace")

    if pane == 3:
        paneB_3 = tk.Button(root, text="", bg="light blue", command=click3)
        paneB_3.place(x=1041, y=600, width=23, height=87) 
    if pane == 3:
        product_menu_pane3.config(state='normal')
        product_menu_pane4.config(state='disabled')

    paneB_4.destroy()
    btn_G2.config(state="disabled")
    btn_G3.config(state="normal")

    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(), gap_thickness3.get(),gas_Ar, temp_I.get(), temp_O.get(), u_value_label,outside_air_speed.get())

def on_4p_click():
    print("4P button clicked!")
    global pane, paneB_3
    pane = 4
    gap_slider1.config(state='normal')
    gap_slider2.config(state='normal')
    gap_slider3.config(state='normal')

    btn_4p.config(bg="orange", activebackground="green")
    btn_3p.config(bg="SystemButtonFace", activebackground="SystemButtonFace")
    btn_2p.config(bg="SystemButtonFace", activebackground="SystemButtonFace")
    if pane == 4:
        paneB_3 = tk.Button(root, text="", bg="light blue", command=click3)
        paneB_3.place(x=1041, y=600, width=23, height=87)
        paneB_4 = tk.Button(root, text="", bg="light blue", command=click4)
        paneB_4.place(x=1329, y=600, width=23, height=87) 
    if pane == 4:
        product_menu_pane3.config(state='normal')
        product_menu_pane4.config(state='normal')

    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(),gap_thickness3.get(), gas_Ar, temp_I.get(), temp_O.get(), u_value_label,outside_air_speed.get())
    btn_G2.config(state="disabled")
    btn_G3.config(state="disabled")

     

def TvU(gap_thickness1, gap_thickness2,gap_thickness3, gas): #Function to generate a contour plot when the button is pressed (takes no arguments, only variable is the window construction which is global) 


    global current_gas_type
    if current_gas_type is None:
        # If no gas type is selected, return without calculating the u-value
        return
    if current_gas_type == "argon":
        gas = gas_Ar
        print("Ar")
    elif current_gas_type == "xenon":
        gas = gas_Xe
        print("Xe")
    elif current_gas_type == "krypton":
        gas = gas_Kr
        print("Kr")
    elif current_gas_type =="air":
        gas = gas_Air
        print("Air")




    inside_temp_l=[]
    u_value_l=[]
    u_value_l2=[]
    btn_G1.config(bg="magenta", activebackground="green")
    btn_G2.config(bg="SystemButtonFace", activebackground="SystemButtonFace")
    btn_G3.config(bg="SystemButtonFace", activebackground="SystemButtonFace")

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

    for i in range(233,323):
        inside_air_temperature = i
        inside_temp_l = inside_temp_l + [i]
        outside_temp_l = []
        u_value_l=[]
        for j in range(233,323):
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
            if pane == 4:
                gap_layer1 = pywincalc.Layers.gap(thickness=float(gap_thickness1/1000), gas=gas)
                gap_layer2 = pywincalc.Layers.gap(thickness=float(gap_thickness2/1000), gas=gas)
                gap_layer3 = pywincalc.Layers.gap(thickness=float(gap_thickness3/1000), gas=gas)
                gap_layers=[gap_layer1,gap_layer2,gap_layer3]
            if pane == 3:
                gap_layer1 = pywincalc.Layers.gap(thickness=float(gap_thickness1/1000), gas=gas)
                gap_layer2 = pywincalc.Layers.gap(thickness=float(gap_thickness2/1000), gas=gas)
                gap_layers=[gap_layer1,gap_layer2]

            if pane == 2:
                gap_layer1 = pywincalc.Layers.gap(thickness=float(gap_thickness1/1000), gas=gas)
                gap_layers=[gap_layer1]

                
            glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, gap_layers = gap_layers, environment=environmental_conditions)

            u_value = glazing_system.u()
            u_value_l=u_value_l+[u_value]
        u_value_l2=u_value_l2+[u_value_l]

    contour = plt.contourf(outside_temp_l,inside_temp_l,u_value_l2)
    cbar = plt.colorbar(contour)
    cbar.set_label('U-Value')
    selected_options = "+".join([
        selected_option_pane1.get(),
        selected_option_pane2.get(),
        selected_option_pane3.get(),
        selected_option_pane4.get()
        ])
    plt.xlabel('Indoor Temperature [°C]')
    plt.ylabel('Outdoor Temperature [°C]')
    plt.title(f'U-Value as a Function of Indoor and Outdoor Temperture - Constructions: {selected_options}', fontsize=11)
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H_%M_%S")  # Replace colons with underscores since colons arent allowed in file names 
    image_path = f'{user_input}/Contour_TempVU_{formatted_datetime}.png' 
    plt.savefig(image_path)
    print("Image saved at {v}".format(v=image_path))

    plt.show()

def GasesPlot2P(): #Generates a plot to show the optimum gap thickness for double pane when button is clicked
    btn_G2.config(bg="magenta", activebackground="green")
    btn_G1.config(bg="SystemButtonFace", activebackground="SystemButtonFace")
    btn_G3.config(bg="SystemButtonFace", activebackground="SystemButtonFace")

    num_points = 50
    thickness_values = np.linspace(0.001, 0.04, num_points)
    gases = [gas_Air, gas_Ar, gas_Kr, gas_Xe, gas_SF6, gas_CO2]
    gas_labels = ["Air", "Argon", "Krypton", "Xenon", "Sulfur Hexaflouride", "Carbon Dioxide"]
    gas_colors = ["black", "blue", "orange", "green", "purple", "red"]
    
    u_value_results = {label: {} for label in gas_labels}

    for gas, label in zip(gases, gas_labels):
        for gap_thickness in thickness_values:
            gap_layer = pywincalc.Layers.gap(thickness=gap_thickness, gas=gas)
            glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, gap_layers=[gap_layer])
            u_value = glazing_system.u()
            u_value_results[label][gap_thickness] = u_value

    plt.figure(figsize=(10, 6))

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(base=0.002)) 
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.3f')) 
    ax.yaxis.set_major_locator(MultipleLocator(base=0.1)) 
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))  

    for label, color in zip(gas_labels, gas_colors):
        u_values = list(u_value_results[label].values())
        thickness_list = list(u_value_results[label].keys())
        plt.plot(thickness_list, u_values, label=f"{label} Gas", color=color)


    selected_options = "+".join([
        selected_option_pane1.get(),
        selected_option_pane2.get(),
        ])
    plt.xlabel('Thickness (m)')
    plt.ylabel('U-value')
    plt.title(f'U-value vs. Gap Thickness for Glazing System - Construction:{selected_options}')
    plt.grid(True)
    plt.legend()

    legend_text = []  
    for label, color in zip(gas_labels, gas_colors):
        gas_min_index = np.argmin(list(u_value_results[label].values()))
        gas_min_u_value = list(u_value_results[label].values())[gas_min_index]
        gas_min_thickness = list(u_value_results[label].keys())[gas_min_index]
        legend_text.append(f"Min U-value ({label}): {gas_min_u_value:.5f} | Thickness: {gas_min_thickness:.5f} m")
        plt.scatter(gas_min_thickness, gas_min_u_value, color='red')


          
    plt.legend(legend_text, loc='upper right')

    plt.grid(False)
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H_%M_%S")  # Replace colons with underscores since colons arent allowed in file names 
    image_path = f'{user_input}/Gap2P_{formatted_datetime}.png'
    plt.savefig(image_path)
    print("Image saved at {v}".format(v=image_path))

    plt.show()




def GasesPlot3P():
    btn_G3.config(bg="magenta", activebackground="green")
    btn_G2.config(bg="SystemButtonFace", activebackground="SystemButtonFace")
    btn_G1.config(bg="SystemButtonFace", activebackground="SystemButtonFace")

    gases = [gas_Air, gas_Ar, gas_Kr, gas_Xe, gas_SF6, gas_CO2]
    gas_labels = ["Air", "Argon", "Krypton", "Xenon", "Sulfur Hexaflouride", "Carbon Dioxide"]
    gas_colors = ["black", "blue", "orange", "green", "purple", "red"]
    t = 0.030
    x_values = np.linspace(-t/2, t/2, 50)
    
    plt.figure(figsize=(10, 6))
    
    for gas, label, color in zip(gases, gas_labels, gas_colors):
        R_value_results = []
        
        for x in x_values:
            gap_1 = pywincalc.Layers.gap(thickness=x + t/2 + 0.00001)
            gap_2 = pywincalc.Layers.gap(thickness=-x + t/2 + 0.00001, gas=gas)
            

            
            glazing_system = pywincalc.GlazingSystem(solid_layers=solid_layers, gap_layers=[gap_1, gap_2])
            R_value = (1 / glazing_system.u()) * 5.678
            R_value_results.append(R_value)
            
        selected_options = "+".join([
            selected_option_pane1.get(),
            selected_option_pane2.get(),
            selected_option_pane3.get()
        ])
        plot_title = f'3P: R-Value vs Gap Thickness - Construction: {selected_options}'

        plot_label = f'{label}'  # Combine selected options and gas label

        plt.plot(x_values, R_value_results, label=plot_label, color=color)

    plt.xlabel('Gap Thickness (x) [m]')
    plt.ylabel('R-Value')
    plt.title(plot_title)
    plt.legend()
    plt.grid(True)
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H_%M_%S")  # Replace colons with underscores since colons arent allowed in file names 
    image_path = f'{user_input}/Gap3P_{formatted_datetime}.png'
    plt.savefig(image_path)
    print("Image saved at {v}".format(v=image_path))
    plt.show()
    
def set_gas_type(gas_type, button):
    global current_gas_type
    global pane
    
    if current_gas_type == gas_type:
        return

    current_gas_type = gas_type
    calculate_u_value(gap_thickness1.get(), gap_thickness2.get(),gap_thickness3.get(), gas_Ar, temp_I.get(), temp_O.get(), u_value_label,outside_air_speed.get())
    
    # Highlight the active button
    for btn in gas_buttons:
        if btn == button:
            btn.config(bg="green", activebackground="green")  
        else:
            btn.config(bg="SystemButtonFace", activebackground="SystemButtonFace")  # Reset the background color for other buttons

    

button1 = tk.Button(root, text="Argon", command=lambda: set_gas_type("argon", button1), font=font, width=10, height=2)
button2 = tk.Button(root, text="Xenon", command=lambda: set_gas_type("xenon", button2), font=font, width=10, height=2)
button3 = tk.Button(root, text="Krypton", command=lambda: set_gas_type("krypton", button3), font=font, width=10, height=2)
button4 = tk.Button(root, text="Air", command=lambda: set_gas_type("air", button4), font=font, width=10, height=2)

button1.grid(row=1, column=1, sticky="nsew")
button2.grid(row=1, column=2, sticky="nsew")
button3.grid(row=1, column=3, sticky="nsew")
button4.grid(row=1, column=4, sticky="nsew")

btn_2p = tk.Button(root, text="Double Pane", command=on_2p_click, font=font, width=10, height=2)
btn_3p = tk.Button(root, text="Triple Pane", command=on_3p_click, font=font, width=10, height=2)
btn_4p = tk.Button(root, text="Quadruple Pane", command=on_4p_click, font=font, width=12, height=2)
btn_G1 = tk.Button(root, text="Temp vs U-Value", command=lambda: TvU(gap_thickness1.get(), gap_thickness2.get(), gap_thickness3.get(), gas_Ar), font=("Helvetica", 8), width=14, height=2)
btn_G2 = tk.Button(root, text="Gap Thickness 2P", command=GasesPlot2P, font=("Helvetica", 8), width=14, height=2)
btn_G3 = tk.Button(root, text="Gap Thickness 3P", command=GasesPlot3P, font=("Helvetica", 8), width=14, height=2)

btn_2p.grid(row=1, column=0, sticky="nw")
btn_3p.grid(row=2, column=0, sticky="nw")
btn_4p.grid(row=3, column=0, sticky="nw")
btn_G1.grid(row=15, column=0, sticky="nw")
btn_G2.grid(row=15, column=1, sticky="nw")
btn_G3.grid(row=16, column=0, sticky="nw")

gas_buttons = [button1, button2, button3, button4]



def slider_callback(event):
    # Call the function to calculate and display the U-value
        print("Gap Thickness 1:", gap_thickness1.get())
        print("Gap Thickness 2:", gap_thickness2.get())
        print("Gas Type:", current_gas_type)
        print("Inside Temperature:", temp_I.get())
        print("Outside Temperature:", temp_O.get())
        print("Outside Air Speed:", outside_air_speed.get())
        calculate_u_value(gap_thickness1.get(), gap_thickness2.get(), gap_thickness3.get(), gas_Ar, temp_I.get(), temp_O.get(), u_value_label, outside_air_speed.get())

# Sliders for gap thickness 1 and gap thickness 2
if pane == 4: 
    gap_slider1 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 1 (mm)", variable=gap_thickness1)
    gap_slider1.bind("<ButtonRelease-1>", slider_callback)  
    gap_slider1.grid(row=5, column=0, columnspan = 1)
    
    gap_slider2 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 2 (mm)", variable=gap_thickness2)
    gap_slider2.bind("<ButtonRelease-1>", slider_callback) 
    gap_slider2.grid(row=6, column=0, columnspan=1)

    gap_slider3 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 3 (mm)", variable=gap_thickness3)
    gap_slider3.bind("<ButtonRelease-1>", slider_callback) 
    gap_slider3.grid(row=7, column=0, columnspan=1)

    btn_G2.config(state="disabled")
    btn_G3.config(state="disabled")
if pane == 3: 
    gap_slider1 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 1 (mm)", variable=gap_thickness1)
    gap_slider1.bind("<ButtonRelease-1>", slider_callback)  
    gap_slider1.grid(row=5, column=0, columnspan = 1)
    
    gap_slider2 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 2 (mm)", variable=gap_thickness2)
    gap_slider2.bind("<ButtonRelease-1>", slider_callback) 
    gap_slider2.grid(row=6, column=0, columnspan=1)


    gap_slider3 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 3 (mm)", variable=gap_thickness3)
    gap_slider3.bind("<ButtonRelease-1>", slider_callback)
    gap_slider3.config(state='disabled')
    gap_slider3.grid(row=7, column=0, columnspan=1)
    product_menu_pane4.config(state='disabled') #Disables dropdown menu for pane 4 


    btn_G2.config(state="disabled")
    btn_G3.config(state="normal")

    
if pane == 2: 
    gap_slider1 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 1 (mm)", variable=gap_thickness1)
    gap_slider1.bind("<ButtonRelease-1>", slider_callback) 
    gap_slider1.grid(row=5, column=0, columnspan=1)

    gap_slider2 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 2 (mm)", variable=gap_thickness2)
    gap_slider2.bind("<ButtonRelease-1>", slider_callback) 
    gap_slider2.config(state='disabled')
    gap_slider2.grid(row=6, column=0, columnspan=1)

    gap_slider3 = tk.Scale(root, from_=1, to=40, orient="horizontal", label="Gap 3 (mm)", variable=gap_thickness3)
    gap_slider3.bind("<ButtonRelease-1>", slider_callback)
    gap_slider3.config(state='disabled')
    gap_slider3.grid(row=7, column=0, columnspan=1)


    product_menu_pane3.config(state='disabled') #Disables dropdown menu for pane 3 
    product_menu_pane4.config(state='disabled') #Disables dropdown menu for pane 4 
    btn_G3.config(state="disabled")
    btn_G2.config(state="normal")

#Sliders for inside and outside temperature
temp_slider_I = tk.Scale(root, from_=temp_MIN_Russia, to=temp_MAX_Kuwait, orient="horizontal", label="Inside Temp[°C]", variable=temp_I)
temp_slider_I.bind("<ButtonRelease-1>", slider_callback)  
temp_slider_I.grid(row=8, column=0, columnspan=1)

temp_slider_O = tk.Scale(root, from_=temp_MIN_Russia, to=temp_MAX_Kuwait, orient="horizontal", label="Outside Temp[°C]", variable=temp_O)
temp_slider_O.bind("<ButtonRelease-1>", slider_callback)  #slider_callback function allows for the results to be updated by moving the slider 
temp_slider_O.grid(row=9, column=0, columnspan=1)

#Slider for outside air speed 

air_slider_O = tk.Scale(root, from_=0, to=23, orient="horizontal", label="Outside Air Speed [m/s]", variable=outside_air_speed)
air_slider_O.bind("<ButtonRelease-1>", slider_callback)  
air_slider_O.grid(row=10, column=0, columnspan=1)


root.mainloop()


