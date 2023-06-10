districts = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
populations = [247100, 333300, 266800, 420900, 318000]
areas = [9.224, 43.35, 12.04, 9.96, 10.09]

population_densities = [population / area for population, area in zip(populations, areas)]

print("Population density of:")
for district, density in zip(districts, population_densities):
    print(f"- {district}: {density}")

average_density = sum(population_densities) / len(population_densities)

print("Average population density:")
print(average_density)