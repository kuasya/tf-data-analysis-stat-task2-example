import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1031228237 # Ваш chat ID, не меняйте название переменной


# def solution(p: float, x: np.array) -> tuple:
#     alpha = 1 - p
#     loc = x.mean()
#     scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
#     return loc - scale * norm.ppf(1 - alpha / 2), \
#            loc - scale * norm.ppf(alpha / 2)

def solution(p: float, x: np.array) -> tuple:
    t = 44
    n = len(x)
    d = x
    a = 2 * d / t ** 2
    mean_a = np.mean(a)
    std_a = 2 * np.std(d) / t ** 2 * np.sqrt(n)
    left = mean_a - norm.ppf(1 - p / 2) * (std_a / np.sqrt(n))
    right = mean_a + norm.ppf(1 - p / 2) * (std_a / np.sqrt(n))
    return left, right
