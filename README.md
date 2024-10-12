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

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/imported-canuck/RRSP-vs-TFSA-vs-nonreg.git
   cd RRSP-vs-TFSA-vs-nonreg
2. Run the main script
   ```bash
   python main.py
3. You will be prompted to enter investment-related information:
   - Amount invested
   - Marginal tax rate upon deposit
   - Marginal tax rate upon withdrawal
   - Percentage of returns taxed as capital gains
   - Annual rate of return
   - Timeframe in years
4. After entering the required information, the script will calculate and display the post-tax values for:
   - Non-registered accounts
   - TFSA accounts
   - RRSP accounts
     
## Assumptions

- No dividends.
  - This assumption affects the non-registered account, as dividends are taxed in the year they are realized, rather than upon withdrawal.
  - This assumption can be disregarded for the TFSA and RRSP, as both have no tax implications until withdrawal.
- One-time, lump-sum contribution and withdrawal
- RRSP refund is immediately realized and invested in an RRSP.
  - The act of depositing money in an RRSP causes you to receive a refund, equal to your marginal tax rate multiplied by the deposited amount. Reinvesting this in the RRSP would once again yield a (smaller) refund. Thus, the terminal amount of the money deposited in an RRSP is modelled using an infinite geometric series.
  - Alternatively, one may simply assume that the initial refund is invested in a TFSA. However, this would yield a different result than the aforementioned method if your marginal tax rate at the time of investment isn't equal to your marginal tax rate at the time of withdrawal.  
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
