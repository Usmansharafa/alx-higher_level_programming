#!/usr/bin/python3
"""Module to perform matrix multiplication using Numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """"Function that multiplies two matrices

    Args:
        m_a (list of lists of integers/floats): 2d array of integers
        m_b (list of lists of integers/floats): 2d array of integers

    Return:
        result of matrix multiplication
    """
    return np.matmul(m_a, m_b)
