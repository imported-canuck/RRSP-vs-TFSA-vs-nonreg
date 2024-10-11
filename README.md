# RRSP vs TFSA vs Non-Registered Investment Calculator

This calculator compares the after-tax future values of investments in different account types (non-registered, RRSP, TFSA) over a set period of time. The goal is to help users better understand their investments' tax implications and future growth based on various scenarios.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Assumptions](#assumptions)
5. [Licence](#licence)
6. [Future Work](#future-work)

## Features

- Calculates after-tax future value for investments in:
  - Non-registered accounts
  - Registered Retirement Savings Plans (RRSPs)
  - Tax-Free Savings Accounts (TFSAs)
- Considers tax implications during contribution, withdrawal, and investment periods.
- Customizable contribution amounts, growth rates, and time horizons.

## Requirements

- Python 3+
- No libraries at the moment

## Usage

To run the calculator, download RRSP-TFSA-nonregcalc.py and run it in your Python IDE (I use VS Code). 

The script will then request you to input various parameters. Input them as instructed and it will print the post-tax investment returns if the investment were to be held in a Registered Retirement Savings Plan (RRSP), Tax-Free Savings Account (TFSA) or a non-registered account with no particular tax advantage. 

## Assumptions

- No dividends.
  - This assumption affects the non-registered account, as dividends are taxed in the year they are realized, rather than upon withdrawal.
  - This assumption can be disregarded for the TFSA and RRSP, as both have no tax implications until withdrawal.
- One-time, lump-sum contribution and withdrawal
- Marginal tax rate invariant.
  - The marginal tax rate you are subject to during the contribution and withdrawal is assumed to be constant.
  - This does not mean that the marginal tax rate you are subject to never changes throughout the life of your investment. Rather, the act of depositing money (and thus reducing your taxable income if an RRSP is used) and the act of withdrawing money (and thus increasing your taxable income if an RRSP or non-registered account is used) will not cause you to move up or down a tax bracket.
- 50% capital gains inclusion rate.
  - From June 25, 2024, onwards, capital gains in excess of $250,000 in a given year will be subject to a 66.67% inclusion rate, rather than the former 50%. This is disregarded at the current moment.
  - Once again, this assumption can be disregarded for the TFSA and RRSP, as investment gains in a TFSA are not subject to tax and all withdrawals from a RRSP are taxed as income (subject to a 100% inclusion rate).
 
## Licence

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Work
- Support different contribution profiles. Such as invariant annual contributions, uniform gradient series contributions, and geometric series contributions.
- Incorporate real provincial and federal tax rates to automatically determine contribution and withdrawal tax rates.
- Incorporate the new inclusion rate for capital gains over $250,000. 
