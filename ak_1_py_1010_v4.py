# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:01:03 2026

@author: Metele-707. 
"""

#Showing the yearly cost of petrol car versus electric car. 
# 1 year defined at 365 days.

#Yearly km driven 10000 both cars
km_driven_yearly = 10000

#Traffic insurance 8.38 pr.day both cars 
traffic_insurance = (8.38 * 365)

#Petrol car expenses aka dinosaur car.
#insurance yearly fee
insurance_yearly_fee_rawrcar = (7500 * 1) 

# Petrol price  pr/km.
rawr_juice_expense_prkm = (1.0 * km_driven_yearly)

#toll fee
toll_fee = (0.3 * km_driven_yearly) 

#Total cost petrol car
total_cost_dino_car = (traffic_insurance + insurance_yearly_fee_rawrcar + rawr_juice_expense_prkm + toll_fee)

#Electric car expenses

# insurance yearly fee
electric_insurance_fee = (5000 * 1)

# Price charging electric car pr.km driven
charge_up_the_battery_car = (0.2 * 2.00 * km_driven_yearly) 

# Toll fee
toll_fee_battery_car = (0.1 * km_driven_yearly)

# total cost electric car
total_cost_battery_car = (traffic_insurance + electric_insurance_fee + charge_up_the_battery_car + toll_fee_battery_car)

cost_differential_electric_to_petrol = total_cost_dino_car - total_cost_battery_car
print('Differential to petrol and electric car is', cost_differential_electric_to_petrol, 'kr')
print(cost_differential_electric_to_petrol,'er differanse mellom bensinbil og elektrisk bil som er rimeligere med årlig avgift på', total_cost_battery_car, total_cost_dino_car, 'respectively')
print('basert på tallene lønner det seg å kjøre elektrisk bil')






