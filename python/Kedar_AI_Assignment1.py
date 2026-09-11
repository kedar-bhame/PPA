
marketing_spend = [18,12,10,15,20]
tyre_volume = [3350,2500,2050,2950,3700]

# Number of Observations
n = len(marketing_spend)

# Calculate mean
mean_x = sum(marketing_spend) / n
mean_y = sum(tyre_volume) / n

# Calculate Numerator And Denominator
numerator = 0
denominator = 0

for i in range(n):
    numerator += (marketing_spend[i] - mean_x) * (tyre_volume[i] - mean_y)
    denominator += (marketing_spend[i] - mean_x) ** 2

# Calculate slope (m) and intercept (c)
slope = numerator / denominator
intercept = mean_y - (slope * mean_x)
print("-" * 40)

# Predict two-wheeler sales
target =float(input("Enter Marketing spend"))

predicted_tyre_volume = (slope * target) + intercept

print("\n mean_x = ",mean_x)
print(" mean_y = ",mean_y)
print("Slope = ",slope)
print("Intercept = ",intercept)

print("\nMarketing spend =", target)
print("predicted_tyre_volume =", round(predicted_tyre_volume, 2))
