# PMPML Bus Ridership vs Bus Fleet Growth - Linear Regression
# Input data
ridership_increase = [5, 0, 0, 100, 97]  # X values (% increase in ridership)
bus_increase = [2, 3, 1, 0, 10]          # Y values (% increase in buses)
n = len(ridership_increase)

# Step 1: Calculate mean of X and Y
mean_x = sum(ridership_increase) / n
mean_y = sum(bus_increase) / n
print("Step 1: Find mean of X and Y")
print(f"x̄ = {mean_x}")
print(f"ȳ = {mean_y}\n")
# Step 2: Calculate slope and intercept
numerator = 0
denominator = 0
for i in range(n):
    x_dev = ridership_increase[i] - mean_x
    y_dev = bus_increase[i] - mean_y
    numerator += x_dev * y_dev
    denominator += x_dev ** 2

# Step 3: Calculate slope
slope = numerator / denominator
print("Step 3: Calculate Slope (m)")
print(f"m = {slope:.4f}")

print("Suggestion: Slope value is very low (0.03), meaning buses are")
print("not growing proportionally with ridership demand.\n")
# Step 4: Calculate intercept
intercept = mean_y - (slope * mean_x)
print("Step 4: Calculate Intercept (c)")
print(f"c = {intercept:.2f}\n")
# Step 5: Regression equation
print("Step 5: Regression Equation")
print(f"y = {slope:.4f}x + {intercept:.2f}")
print("Suggestion: Use this formula to predict bus additions for any")
print("given ridership increase percentage.\n")
# Step 6: Prediction
target_x = 50
predicted_y = (slope * target_x) + intercept
print("Step 6: Predict for 50% ridership increase")
print(f"y = {predicted_y:.2f}%")
print("Suggestion: When ridership increases by 50%, buses increase by only 3.47%.")
print("PMPML should aim for a 1:1 ratio (equal % increase) to avoid overcrowding.\n")
# Additional suggestion
print("="*60)
print("OVERALL SUGGESTIONS:")
print("="*60)
print("1. Current slope (0.03) is too low - buses lag behind demand")
print("2. In 2021-22: ridership +100% but buses +0% = severe overcrowding")
print("3. PMPML should increase bus purchase rate to match ridership growth")
print("4. Target: Achieve a slope closer to 1.0 (equal growth rates)")
print("5. This will prevent overcrowding and improve service quality")