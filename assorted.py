def vector_addition(targ_vector , source_vector):
    for i in range(len(targ_vector)):
        #dimension check
        if(len(source_vector) <= i):
            break
        targ_vector[i] += source_vector[i]
        
def vector_array_summed(vector_arr , dimension = 2 , targ_vector = None , divisor = 1):
    if targ_vector is None:
        targ_vector = [0 for x in range(dimension)]

    for i in range(len(targ_vector)):
        for active_vector in vector_arr:
            # dimension check
            if(len(active_vector) <= i):
                continue
            targ_vector[i] += round(active_vector[i] / float(divisor))
    return targ_vector
