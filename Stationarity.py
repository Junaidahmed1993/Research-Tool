#This illustrate the graphical presentations of the two graphs based on Auto-correlation function that shows the stationarity in the timeseires. 

#1. ACF function for non-stationarity time series
# Create a stationary series
stationary_series = noise  # Random noise is inherently stationary

# Plot ACF
plot_acf(stationary_series, lags=30)
plt.title("ACF of Stationary Series")
plt.show()


2. Non-Stationarity
# Create a stationary series
stationary_series = noise  # Random noise is inherently stationary

# Plot ACF
plot_acf(stationary_series, lags=30)
plt.title("ACF of Stationary Series")
plt.show()
