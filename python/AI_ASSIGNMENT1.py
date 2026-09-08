# Python Code
# Driving Test Passers vs Two-Wheeler Sales Prediction
# Linear Regression 

test_passers = [100,120,140,160,180,200]
two_wheeler_sold = [72,84,110,126,144,160]

# Number of Observations
n = len(test_passers)

# Calculate mean
mean_x = sum(test_passers) / n
mean_y = sum(two_wheeler_sold) / n

# Calculate Numerator And Denominator
numerator = 0
denominator = 0

for i in range(n):
    numerator += (test_passers[i] - mean_x) * (two_wheeler_sold[i] - mean_y)
    denominator += (test_passers[i] - mean_x) ** 2

# Calculate slope (m) and intercept (c)
slope = numerator / denominator
intercept = mean_y - (slope * mean_x)
print("-" * 40)

# Predict two-wheeler sales
target_passers =float(input("Enter driving test passers:"))

predicted_two_wheeler = (slope * target_passers) + intercept

print("\n mean_x = ",mean_x)
print(" mean_y = ",mean_y)
print("Slope = ",slope)
print("Intercept = ",intercept)

print("\nDriving Test Passers =", target_passers)
print("Predicted Two-Wheeler Sold =", round(predicted_two_wheeler, 2))
print("Average Two-Wheeler Sales = ",round(mean_y)," vahicles.")

# SUGGESTION
if target_passers>mean_x:
    print("\n SUGGESTION : Increase two-wheeler stock bacause")
    print("the number of driving test passers is higher than average.\n")

elif target_passers<mean_x:
    print("\n SUGGESTION : Keep moderate stock bacause")
    print("the number of driving test passers is lower than average.")
    print("Avoid excess stock and focus on targeted offers.\n")

else:
    print("\nSUGGESTION : Maintain current stock level")
    print("because the number of driving test passers is around average.\n")