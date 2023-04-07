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
    # Измените код этой функции
    alpha = 1 - p
    n = len(x)
    loc = np.mean(x) / 44
    scale = np.sqrt(np.var(x) / n) / 44
    t_value = t.ppf(1 - alpha / 2, n - 1)
    left_bound = loc - t_value * scale
    right_bound = loc + t_value * scale
    return left_bound, right_bound
