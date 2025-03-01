import streamlit as st

st.set_page_config(page_title='Unit Convertor', layout='centered')
# note: the data for the conversion factor was fetched from the 
# internet and can be erroneous :)

length_conversion = {
    "m": 1,
    "km": 0.001,
    "cm": 100,
    "mm": 1000,
    "inch": 39.3701,
    "foot": 3.28084,
    "mile": 0.000621371
}
area_conversion = {
    "m²": 1,
    "km²": 1e-6,
    "cm²": 10000,
    "mm²": 1e6,
    "acre": 0.000247105,
    "hectare": 0.0001
}
data_transfer_conversion = {
    "bps": 1,
    "kbps": 1e-3,
    "Mbps": 1e-6,
    "Gbps": 1e-9,
    "Tbps": 1e-12
}
energy_conversion = {
    "J": 1,
    "kJ": 0.001,
    "cal": 0.239006,
    "kWh": 2.77778e-7
}
volume_conversion = {
    "m³": 1,
    "cm³": 1e6,
    "mm³": 1e9,
    "L": 1000,
    "mL": 1e6,
    "ft³": 35.3147,
    "in³": 61023.7,
    "gallon (US)": 264.172,
    "gallon (UK)": 219.969
}
digital_storage_conversion = {
    "B": 1,
    "KB": 1e-3,
    "MB": 1e-6,
    "GB": 1e-9,
    "TB": 1e-12,
    "PB": 1e-15,
    "bit": 8
}
frequency_conversion = {
    "Hz": 1,
    "kHz": 1e-3,
    "MHz": 1e-6,
    "GHz": 1e-9,
    "THz": 1e-12
}
fuel_economy_conversion = {
    "km/L": 1,
    "mpg (US)": 2.35215,
    "mpg (UK)": 2.82481,
    "L/100 km": 100
}
mass_conversion = {
    "kg": 1,
    "g": 1000,
    "mg": 1e6,
    "lb": 2.20462,
    "oz": 35.274,
    "tonne": 0.001,
    "ton (US)": 0.00110231
}
angle_conversion = {
    "rad": 1,
    "degree": 57.2958,
    "minute of arc": 3437.75,
    "second of arc": 206265,
    "gon": 63.662
}
pressure_conversion = {
    "Pa": 1,
    "kPa": 1e-3,
    "MPa": 1e-6,
    "bar": 1e-5,
    "atm": 9.86923e-6,
    "psi": 0.000145038
}
speed_conversion = {
    "m/s": 1,
    "km/h": 3.6,
    "mph": 2.23694,
    "knot": 1.94384,
    "ft/s": 3.28084
}
time_conversion = {
    "s": 1,
    "ms": 1000,
    "minute": 1/60,
    "hour": 1/3600,
    "day": 1/86400,
    "week": 1/604800,
    "month": 1/2.628e6,  # Approximate
    "year": 1/3.154e7   # Approximate
}


st.title('Unit Convertor 🚀')

def convert_units(value, from_unit, to_unit, conversion_dict):
    value_in_base = value / conversion_dict[from_unit]
    
    converted_value = value_in_base * conversion_dict[to_unit]
    
    return round(converted_value, 3)

st.write('Convert Phisical Quantities with the help of this convertor - Made by Uzair Bin Aisf')
quantities = ['Area', 'Volume', 'Length', 'Data Transfer Rate', 'Digital Storage', 'Energy', 'Frequency', 'Fuel Economy', 'Mass', 'Plane Angle', 'Pressure', 'Speed', 'Time']
category = st.selectbox('Choose the quantity you wish to convert', quantities)

if category == "Length":
    conversion_dict = length_conversion
elif category == "Area":
    conversion_dict = area_conversion
elif category == "Data Transfer Rate":
    conversion_dict = data_transfer_conversion
elif category == "Energy":
    conversion_dict = energy_conversion
elif category == "Volume":
    conversion_dict = volume_conversion
elif category == "Digital Storage":
    conversion_dict = digital_storage_conversion
elif category == "Frequency":
    conversion_dict = frequency_conversion
elif category == "Fuel Economy":
    conversion_dict = fuel_economy_conversion
elif category == "Mass":
    conversion_dict = mass_conversion
elif category == "Plane Angle":
    conversion_dict = angle_conversion
elif category == "Pressure":
    conversion_dict = pressure_conversion
elif category == "Speed":
    conversion_dict = speed_conversion
elif category == "Time":
    conversion_dict = time_conversion


value = st.number_input("Enter the value to convert:", format="%0f")
from_val_unit = st.selectbox("From Unit:", list(conversion_dict.keys()))
to_unit = st.selectbox("To Unit:", list(conversion_dict.keys()))

if st.button("Convert"):
    result = convert_units(value, from_val_unit, to_unit, conversion_dict)
    st.write(f'Result: {result} {to_unit}')
