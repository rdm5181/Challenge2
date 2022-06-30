# Project Title

This is a python command-line interface application that allows users to see qualifying loans from lenders quickly and easily. The application works by taking in a `daily_rate_sheet` of loan criteria from various loan providers, asking the user a number of questions to evaluate their loan eligibility, and then returning to them a list of qualifying loans.

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

---

## Installation Guide

Before running the application first install the following dependencies.

python
  pip install fire
  pip install questionary

---

## Usage

The program asks a path for the rate sheet followed by five questions:
  What's your credit score?
  What's your current amount of monthly debt?
  What's your total monthly income?
  What's your desired loan amount?
  What's your home value?
Financial ratios are calculated and the number of qualifying loans are given.
The user may save the information to a file of their choice.

---

## Contributors

Russell Moore
-Linkedin: https://www.linkedin.com/in/russell-david-moore/

---

## License

Business Operations (BizOps)

## Updates
v.1: 6/29/2022 First draft of save function and save qualifying loan implemented.
v.2: 6/29/2022 Updated Readme file and dialog for save qualifying loan.
v.3: 6/29/2022 Successfully writes loan list
v.4: 6/30/2022 Business Requirements successfully translated into code.