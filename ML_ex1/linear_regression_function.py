import numpy as np


def feature_normalize(feature_data):

    x_norm = np.array(feature_data)
    mu = np.array(x_norm.mean(axis=0))
    sigma = np.array(x_norm.std(axis=0))
    for i in range(0, mu.size):
        x_norm[:, i] = (x_norm[:, i] - mu[i])/sigma[i]
    return [x_norm, mu, sigma]


def compute_cost(feature_data, labels, parameters):

    x = feature_data
    y = labels
    theta = parameters
    m = labels.size
    ele1 = np.dot(x, theta) - y
    j = ele1.T.dot(ele1)/2/m
    return j[0, 0]


def gradient_descent_multi(feature_data, labels, parameters, learning_rate, num_iters):

    x = np.array(feature_data)
    y = labels
    m = labels.size
    theta = parameters
    alpha = learning_rate
    j_history = []

    for i in range(0, num_iters):
        theta = theta - alpha / float(m) * x.T.dot(x.dot(theta) - y)
        j_history.append(compute_cost(x, y, theta))

    return [theta, j_history]


def normal_equation(feature_data, labels):

    x = feature_data
    y = labels
    theta = np.dot(np.linalg.inv(x.T.dot(x)), x.T).dot(y)

    return theta