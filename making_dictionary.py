def count_blood(x):
    blood_dict = {}
    for p in x:
        if blood_dict.get(p):
            blood_dict[p] += 1
        else:
            blood_dict[p] = 1
    return blood_dict