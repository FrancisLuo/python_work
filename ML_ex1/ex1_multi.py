import numpy as np
import matplotlib.pyplot as plt
import linear_regression_function as lrf

# load data
data = np.loadtxt('ex1data2.txt')
X = np.array(data[:, 0:2])
y = np.array(data[:, 2:3])
# normalize data
[X_norm, mu, sigma] = lrf.feature_normalize(X)
intercept = np.ones([m, 1])
X_norm = np.hstack((intercept, X_norm))

# set the learning rate and iteration
alpha = 0.1
num_iters = 50
theta = np.zeros((X_norm.shape[1], 1))
# Using the gradient descent to obtain the theta in the linear equation
[theta, J_history] = lrf.gradient_descent_multi(X_norm, y, theta, alpha, num_iters)
test_sample = np.array([1, (1650-mu[0])/sigma[0], (3-mu[1])/sigma[1]])
price = np.dot(test_sample, theta)

print "Through the gradient descent"
print "For x = [1, 1650, 3]"
print "The future price will be " + str(price)

# Using the normal equation to obtain the value of theta
test_sample2 = np.array([1, 1650, 3])
X = np.hstack((intercept, X))
theta2 = lrf.normal_equation(X, y)
price = np.dot(test_sample2, theta2)
print "Through the normal equation"
print "For x = [1, 1650, 3]"
print "The future price will be " + str(price)

# Plot the cost function J
iteration = list(range(1, num_iters+1))
plt.plot(iteration, J_history, linewidth=5)
plt.title("relationship between cost function J and iteration")
plt.xlabel("iters")
plt.ylabel("cost")
plt.show()
