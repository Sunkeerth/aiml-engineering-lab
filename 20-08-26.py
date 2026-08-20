# """
# ================================================================================
# PROBLEM STATEMENT: DOLLAR TO RUPEE CONVERTER
# ================================================================================

# Description:
# Write a program that converts a given amount of US Dollars (USD) into Indian 
# Rupees (INR) using a fixed exchange rate of 1 USD = 82.73 INR. Your program 
# must handle multiple test cases and print each result formatted to a specific 
# decimal precision.

# Input Format:
# The input consists of multiple lines. Each line contains a single integer 
# representing an amount in US Dollars (USD).

# Output Format:
# For each input line, print the converted amount in Indian Rupees (INR). Every 
# output value must be formatted to exactly 4 decimal places.
# """
# import sys

# def solve(input_data):
#     # Split input into separate lines
#     lines = input_data.split("\n")
    
#     for i in lines:
#         # Check if the line is not empty
#         if i.strip():
#             # Convert the string to a floating-point number
#             dollar = float(i.strip())
#             # Calculate the conversion (1 USD = 82.73 INR)
#             res = dollar * 82.73
#             # Print each result formatted to exactly 4 decimal places
#             print(f"{res:.4f}")

# # Read all input from standard input
# input_data = sys.stdin.read().strip()

# # Call the function to execute the logic
# solve(input_data)

# # =============================================================================================

# """ 
# ========================================================================
# PROBLEM STATEMENT: Rectangle Perimeter
# ========================================================================
# Write a program to find the perimeter of the rectangle. 

# Formula: perimeter = 2 * (length + width)

# ------------------------------------------------------------------------
# INPUT FORMAT
# ------------------------------------------------------------------------
# * First line contains an Integer, length of a rectangle.
# * Second line contains an Integer, represents width of a rectangle.

# ------------------------------------------------------------------------
# OUTPUT FORMAT
# ------------------------------------------------------------------------
# * Print the perimeter of the rectangle.

# ========================================================================
# SAMPLE TEST CASES
# ========================================================================

# --- Sample Case 1 ---
# Input:
# 2
# 4

# Output:
# 12

# --- Sample Case 2 ---
# Input:
# 10
# 20

# Output:
# 60

# ========================================================================
# CONSTRAINTS
# ========================================================================
# 1 <= length, width <= 1000
# """

# import sys

# # Read input from standard input
# input_data = sys.stdin.read().strip()

# def solve1(input_data):
#     # Split lines and filter out any empty lines
#     lines = [line.strip() for line in input_data.split("\n") if line.strip()]
    
#     # Convert the first two lines to integers
#     length = int(lines[0])
#     width = int(lines[1])
    
#     # Calculate perimeter using the formula: 2 * (length + width)
#     perimeter = 2 * (length + width)
#     print(perimeter)

# # Call the function
# solve1(input_data)

""" 
# ==========================================
# PROBLEM STATEMENT: Square Perimeter
# Formula: Perimeter = 4 * side
#
# Input Format:
# First line contains an Integer, side of a square
 10
#
# Output Format:
# Print the perimeter of the square
# ========================================== """

n=int(input("enter the side of circle: "))
# def square(x):
#     per=4*x
#     return per
# res=square(n)
# print("perimeter of square is:",res)


# ==========================================
# PROBLEM STATEMENT: Circle Area
# Formula: area = pi * r * r
# Consider pi = 3.142 (double data type)
#
# NOTE: 
# 4 decimal points have to be printed.
#
# Input Format:
# First line contains an Integer, radius of a circle
#
# Output Format:
# Print the area of the circle. The area of the circle should have four decimal places only.
# ==========================================

import math
def area_circle(x):
    res=math.pi*x*x
    return res
obj=area_circle(n)
print(obj)
