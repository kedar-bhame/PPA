# Flight Delay vs Food Packets Sold
# Simple Linear Regression
# With Number of Passengers

# Given data
flight_delay = [5, 8, 10, 15, 20]
food_packets = [281, 297, 308, 334, 360]

# Number of observations
n = len(flight_delay)

# Calculate mean of X and Y
mean_x = sum(flight_delay) / n
mean_y = sum(food_packets) / n

# Calculate covariance and variance
covariance = 0
variance_x = 0

for i in range(n):
    covariance += (flight_delay[i] - mean_x) * (food_packets[i] - mean_y)
    variance_x += (flight_delay[i] - mean_x) ** 2

# Calculate slope
m = covariance / variance_x

# Calculate intercept
c = mean_y - (m * mean_x)

# Regression equation
print("----- Simple Linear Regression -----")
print("Independent Variable (X): Flight Delay")
print("Dependent Variable (Y): Food Packets Sold")

print("\nMean of X =", round(mean_x, 2))
print("Mean of Y =", round(mean_y, 2))
print("Covariance =", round(covariance, 2))
print("Variance of X =", round(variance_x, 2))

print("\nSlope (m) =", round(m, 3))
print("Y-Intercept (c) =", round(c, 3))

print("\nRegression Equation:")
print("Y =", round(m, 3), "X +", round(c, 3))


# ---------------- USER INPUT ----------------

print("\n----- Enter Flight Details -----")

delay = float(input("Enter expected flight delay in minutes: "))
passengers = int(input("Enter number of passengers in the airplane: "))

# Prediction using regression
predicted_food = m * delay + c

# ---------------- OUTPUT ----------------

print("\n----- Prediction -----")
print("Flight Delay =", delay, "minutes")
print("Number of Passengers =", passengers)
print("Predicted Food Packets =", round(predicted_food))


# ---------------- SUGGESTIONS ----------------

print("\n----- Suggestions -----")

if passengers <= 100:
    passenger_suggestion = "Low passenger count. Normal food stock is sufficient."
elif passengers <= 200:
    passenger_suggestion = "Medium passenger count. Keep some extra food packets."
else:
    passenger_suggestion = "High passenger count. Keep additional food packets ready."

print(passenger_suggestion)


# Extra stock based on passenger count
if passengers > 200:
    final_packets = round(predicted_food + 20)
elif passengers > 100:
    final_packets = round(predicted_food + 10)
else:
    final_packets = round(predicted_food)

print("Recommended Food Packets =", final_packets)

if final_packets < 300:
    print("Demand Level: Low")
elif final_packets <= 350:
    print("Demand Level: Medium")
else:
    print("Demand Level: High")

print("\n----- Final Recommendation -----")
print("For", passengers, "passengers and", delay,
      "minutes of flight delay, keep around",
      final_packets, "food packets ready.")