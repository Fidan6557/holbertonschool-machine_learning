#!/usr/bin/env python3
"""Plot frequency histogram of student grades"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plot a histogram of student grades for Project A."""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.hist(student_grades, bins=10, edgecolor='black')
    plt.show()
