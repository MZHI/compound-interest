#!/usr/bin/env python3   
# -*- coding utf-8 -*-

"""
Calculating compound interest given initial amount, annual interest
and monthly adding

@author: Zhidenko Mikhail
"""

import argparse
import sys


# recursive method
def calculate_compound_interest(initial_amount, monthly_adding, interest, years_to_calc):
    year_adding = 12 * monthly_adding
    years_to_calc -= 1
    if years_to_calc >= 0:
        initial_amount = initial_amount * (1.0 + interest * 1.0 / 100.0) + year_adding
        initial_amount = calculate_compound_interest(initial_amount, monthly_adding, interest, years_to_calc)
    return initial_amount


# recursive method
def calculate_compound_interest_monthly(initial_amount, monthly_adding, interest, months_to_calc):
    months_to_calc -= 1
    if months_to_calc >= 0:
        initial_amount = initial_amount * (1.0 + interest * 1.0 / 100.0 / 12.0) + monthly_adding
        initial_amount = calculate_compound_interest_monthly(initial_amount, monthly_adding, interest, months_to_calc)
    return initial_amount


# original method
# def calculate_compound_interest_2(initial_amount, monthly_adding, interest, years_to_calc):
#     res = initial_amount
#     for i in range(years_to_calc):
#         res = res * (1.0 + interest * 1.0 / 100.0) + 12 * monthly_adding
#     return res


def main(args):

    initial_amount = args.initial_amount
    interest = args.interest
    years = args.years
    monthly_add = args.monthly_add
    is_monthly = args.is_monthly
    if not is_monthly:
        res = calculate_compound_interest(initial_amount, monthly_add, interest, years)
    else:
        res = calculate_compound_interest_monthly(initial_amount, monthly_add, interest, years * 12)
        
#     res_1 = calculate_compound_interest_2(initial_amount, monthly_add, interest, years)

    if not is_monthly:
        print("Reinvesting once a year. Start: {}$, monthly add: {}$, interest: {:.2f}%, years: {}".format(initial_amount, monthly_add, interest, years))
    else:
        print("Reinvesting every month. Start: {}$, monthly add: {}$, interest: {:.2f}%, years: {}".format(initial_amount, monthly_add, interest, years))
    
    print("Your final amount: {:.2f}$".format(res))


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--initial-amount", type=int, default=5000,
            help="Initial investment amount. Default 5000")
        parser.add_argument("--monthly-add", type=int, default=100,
            help="Investing monthly sum. Default 100")
        parser.add_argument("--interest", type=int, default=10, 
            help="estimated annual interest, in %%. Default 10%%")
        parser.add_argument("--years", type=int, default=10,
            help="number of years of inverstment. Default 10")
        parser.add_argument("--is-monthly", type=int, default=0,
            help="Whether to reinvestment every month or once a year. Default 0 (once a year)")

    except Exception as ex:
        print("Error: {}".format(ex))
    main(parser.parse_args(sys.argv[1:]))

