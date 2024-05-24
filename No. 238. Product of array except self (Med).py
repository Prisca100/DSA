"""Array, Math"""
# Brute force
def product_of_array_excluding_self(l):
    product_list = []
    for i in range(len(l)):
        product = 1
        for j in range(len(l)):
            if l[i] == l[j]:
                continue
            product *= l[j]
        product_list.append(product) 
    return product_list

# Optimized with Division
def product_of_array_excluding_self_with_division(l):
    """Optimize the time complexity"""
    count_zero = 0
    product = 1

    for i in l:
        if i == 0:
            count_zero+=1
            continue
        product*= i

    if count_zero > 1:
        return [0]*len(l)

    return [0 if i != 0 else product for i in l] if count_zero !=0 else [product/i for i in l]


# Optimized with prefix and suffix addition
