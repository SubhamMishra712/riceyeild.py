import pandas as pd

# Prompt user to enter precipitation data
precip_data = input("Enter monthly precipitation data for the area, separated by commas: ")
precip_list = precip_data.split(',')
precip_array = pd.Series(precip_list)

# Convert data types and clean data
precip_array = pd.to_numeric(precip_array, errors='coerce')
precip_array = precip_array.dropna()

# Calculate annual precipitation
annual_precip = precip_array.sum()

# Prompt user to enter rice cultivation information
area_cultivated = float(input("Enter the area of land under rice cultivation (in hectares): "))
rice_variety = input("Enter the variety of rice grown: ")
planting_date = input("Enter the planting date (YYYY-MM-DD): ")
harvest_date = input("Enter the harvest date (YYYY-MM-DD): ")

# Calculate expected rice yield
# Replace this with appropriate crop model based on rice variety and planting/harvest dates
expected_yield = annual_precip * 10  # Placeholder formula

# Display results to user
print("Annual precipitation: {:.2f} mm".format(annual_precip))
print("Expected yield of {} rice: {:.2f} tonnes".format(rice_variety, expected_yield))
