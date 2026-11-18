'''
def add_bonus(score):
    return score + 10

def cap_score(score):
    if score > 100:
        return 100
    else:
        return score

def process_batch(adjustment_func,score_list):
    result = []
    for score in score_list:
        new_result = adjustment_func(score)
        result.append(new_result)
    return result

bonus = process_batch(add_bonus, [45,85,105,90])
cap = process_batch(cap_score, [45,85,105,90])

print(bonus)
print(cap)
'''

def apply_luxury_tax(price):
    '''Transformation function for luxury tax'''
    return price * 1.2

def apply_clearance_cut(price):
    '''Transformation function for clearance cut'''
    return price / 2

def is_expensive(price):
    ''' condition/filter function '''
    if price > 50:
        return True
    else:
        return False

def smart_pipeline(data_list, transform_func, condition_func):
    result = []
    for item in data_list:
        if condition_func(item):
            result.append(transform_func(item))
        else:
            result.append(item)
    return result

result_1 = smart_pipeline([20, 120, 45, 200, 15, 80], apply_luxury_tax,is_expensive)
result_2 = smart_pipeline([20, 120, 45, 200, 15, 80], apply_clearance_cut,is_expensive)

print(result_1)
print(result_2)
