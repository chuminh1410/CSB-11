districts = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
populations = [247100, 333300, 266800, 420900, 318000]
populations = [247100, 333300, 266800, 420900, 318000]
max_population = populations.index(max(populations))
min_population = populations.index(min(populations))

print("Indices of:")
print("- Most populated dist.:", max_population)
print("- Least populated dist.:", min_population)

print("Names of:")
print("- Most populated dist.:", districts[max_population])
print("- Least populated dist.:", districts[min_population])