"""
Basic engineering calculations.

Author: Ruan Vitorino Souza
Description:
Simple electrical calculations used as part of engineering studies.
"""

# Electrical parameters
voltage = 220  # Volts
current = 5    # Amperes

# Power calculation
power = voltage * current

print(f"Voltage: {voltage} V")
print(f"Current: {current} A")
print(f"Electrical Power: {power} W")

# Ohm's Law calculation
voltage_ohm = 12  # Volts
current_ohm = 2   # Amperes

resistance = voltage_ohm / current_ohm

print("\nOhm's Law Example")
print(f"Voltage: {voltage_ohm} V")
print(f"Current: {current_ohm} A")
print(f"Resistance: {resistance} Ohms")
