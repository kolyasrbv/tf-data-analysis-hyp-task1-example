import pandas as pd
import numpy as np


chat_id = 433193277 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    if(x_cnt / y_cnt < x_success / y_success):
        return True
    return False
solution(x_success, x_cnt, y_success, y_cnt)
