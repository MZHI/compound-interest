# compound-interest

**compound-interest** proposes simple python script for compund interest calculation.

## What is compund interest

Base on [this](https://www.investopedia.com/terms/c/compoundinterest.asp) resource, 
`Compound interest (or compounding interest) is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods. Thought to have originated in 17th-century Italy, compound interest can be thought of as "interest on interest," and will make a sum grow at a faster rate than simple interest, which is calculated only on the principal amount.`

## Usage

Script `comp_interest_calculate.py` run in console mode and can include next parameters:
* `--initial-amount` - initial amount of deposit, default 5000
* `--monthly-add` - amount of monthly adding sum to deposit. Default 100
* `interest` - estimated annual interest, in %. Default 10
* `--years` - investment term. Default 10
* `is-monthly` - whether to reinvest profit every month (==1) or only once a year (==0). Default 0 (once a year)

To calculate interest, just run script in console with corresponding parameters:
```sh
$ 
```
