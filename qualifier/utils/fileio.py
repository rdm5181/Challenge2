# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(qualifying_loans, csvpath):
    """Saves data to a csv file:
    
    Args:
        csvpath (Path): The csv file path to be written to.
        qualifying_loans: A list of loan data.
    
    Returns: 
        Saves file.
        
    """
    with open(csvpath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Lender','Max Loan','Max Loan to Value','Max Debt to Income','Min Credit Score','Interest Rate'])  #Header
        writer.writerows(qualifying_loans)
