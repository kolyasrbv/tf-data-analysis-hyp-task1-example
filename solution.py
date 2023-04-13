import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 433193277 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = x_success / x_cnt
    y = y_success / y_cnt
    std_diff = np.sqrt((x * (1 - x) / x_cnt) + (y * (1 - y) / y_cnt))
    t = np.abs(y - x) / std_diff
    c = st.norm.ppf(1 - 0.05/2)
    return t > c
