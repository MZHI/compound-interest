# compound-interest

**compound-interest** proposes simple python script for compound interest calculation.

## What is compound interest

Referring to the definition from [this](https://www.investopedia.com/terms/c/compoundinterest.asp) resource:  
`Compound interest (or compounding interest) is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods. Thought to have originated in 17th-century Italy, compound interest can be thought of as "interest on interest," and will make a sum grow at a faster rate than simple interest, which is calculated only on the principal amount.`

## Usage

Just run script `compound_interest_calc.py` in console mode. Parameters: 
* `--initial-amount` - initial amount of deposit, default 5000
* `--monthly-add` - amount of monthly adding sum to deposit. Default 100
* `--interest` - estimated annual interest, in %. Default 10
* `--years` - investment term. Default 10
* `--is-monthly` - whether to reinvest profit every month (==1) or only once a year (==0). Default 0 (once a year)

## Examples

<details><summary><b>Show instructions</b></summary>

1. Running with default parameters:
```sh
$ python3 compound_interest_calc.py
```

Output: 
```sh
$ Reinvesting once a year. Start: 5000$, monthly add: 100$, interest: 10.00%, years: 10
$ Your final amount: 32093.62$
```

2. Using custom parameters, reinvesting profit once a year:
```sh
$ python3 compound_interest_calc.py --initial-amount 5000 --monthly-add 300 --interest 10 --years 20
```
Output:
```sh
$ Reinvesting once a year. Start: 5000$, monthly add: 300$, interest: 10.00%, years: 20
$ Your final amount: 239827.50$
```

3. Using custom parameters, reinvesting profit every month:
```sh
$ python3 compound_interest_calc.py --initial-amount 5000 --monthly-add 300 --interest 10 --years 20 --is-monthly 1
```
Output:
```sh
$ Reinvesting every month. Start: 5000$, monthly add: 300$, interest: 10.00%, years: 20
$ Your final amount: 264451.02$
```

</details>

**Have fun to calculation your investment strategy!**
**Any contributions and ideas for further developing are appreciated!**
