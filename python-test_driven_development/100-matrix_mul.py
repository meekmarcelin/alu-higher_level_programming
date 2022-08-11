#!/usr/bin/python3
""" multiplication of matrix """


def matrix_mul(m_a, m_b):
    """ multiply matrix """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")
    elif len(m_a) < 1:
        raise ValueError("m_a can't be empty")
    elif len(m_b) < 1:
        raise ValueError("m_b can't be empty")
    for m in m_a:
        if type(m) != list:
            raise TypeError("m_a must be a list of lists")
    for m in m_a:
        if len(m) < 1:
            raise ValueError("m_a can't be empty")
    for m in m_a:
        for eq in m:
            if type(eq) != int and type(eq) != float:
                raise TypeError("m_a should contain only integers or floats")
    for m in m_a:
        if len(m) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for k in m_b:
        if type(k) != list:
            raise TypeError("m_b must be a list of lists")
    for k in m_b:
        if len(k) < 1:
            raise ValueError("m_b can't be empty")
    for k in m_b:
        for eq_2 in k:
            if type(eq_2) != int and type(el_2) != float:
                raise TypeError("m_b should contain only integers or floats")
    for k in m_b:
        if len(k) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise TypeError("m_a and m_b can't be multiplied")
    result = []
    for q in m_a:
        temp_res = []
        for m in range(len(m_b[0])):
            temp = [k[m] for k in m_b]
            addition = 0 
            for s, g in zip(q, temp):
                addition += s * 1
            temp_res.append(tamp_res)
    return result
