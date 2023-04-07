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
    n = len(x)
    alpha = 1 - p
    mean = x.mean()
    std = np.sqrt(np.var(x))
    dof = n - 1
    t_value = abs(t.ppf(alpha/2, dof))
    conf_int = t_value * std / np.sqrt(n)
    lower = mean - conf_int
    upper = mean + conf_int
    return (lower, upper)
