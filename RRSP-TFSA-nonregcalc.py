# Input section
contribution = float(input("Amount contributed to RRSP: "))  # Amount contributed to RRSP
dep_tax = float(input("Marginal tax rate upon deposit: "))   # Marginal tax rate upon deposit
with_tax = float(input("Marginal tax rate upon withdrawal: "))  # Marginal tax rate upon withdrawal
eq_port = float(input("Percentage of your returns that is taxed as capital gains (ie. equities): ")) # Amount taxed as capital gains 
# Investment parameters
return_rate = float(input("Rate of return, compounded annually: ")) # Annual return rate
years = int(input("Timeframe, in years: "))  # Number of years for investment


# Calculate after-tax income percentages
inc_left = 100 - with_tax
cap_gains = with_tax / 2
inc_cg = 100 - cap_gains

# Calculate RRSP refund and principal
RRSP_refund = dep_tax / 100 * contribution
RRSP_principal = contribution + RRSP_refund

# Calculate pre-tax values for all scenarios
pretax_noRRSP = contribution * ((1 + return_rate / 100) ** years)
pretax_RRSP = RRSP_principal * ((1 + return_rate / 100) ** years)
TFSA = contribution * ((1 + return_rate / 100) ** years)

# Calculate taxable amount for the non-RRSP scenario
taxable_noRRSP = pretax_noRRSP - contribution
cg_noRRSP = taxable_noRRSP * (eq_port / 100)
inc_noRRSP = taxable_noRRSP - cg_noRRSP

# Calculate post-tax values for both scenarios
posttax_noRRSP = contribution + (cg_noRRSP * inc_cg / 100 + inc_noRRSP * inc_left / 100)
posttax_RRSP = inc_left / 100 * pretax_RRSP

# Output results
print("Post-tax value in a non-registered account: {:.2f}".format(posttax_noRRSP))
print("Post-tax value in an RRSP account: {:.2f}".format(posttax_RRSP))
print("Post-tax value in a TFSA account: {:.2f}".format(TFSA))
