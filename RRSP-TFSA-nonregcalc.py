import taxcalc

investment_info = {
    "contribution": float(input("Amount invested: ")),
    "dep_tax": float(input("Marginal tax rate upon deposit: ")),
    "with_tax": float(input("Marginal tax rate upon withdrawal: ")),
    "eq_port": float(input("Percentage of your returns that is taxed as capital gains (ie. equities): ")),
    "return_rate": float(input("Rate of return, compounded annually: ")),
    "years": int(input("Timeframe, in years: "))
}

RRSP = taxcalc.calc_RRSP(investment_info)
TFSA = taxcalc.calc_TFSA(investment_info)
nonreg = taxcalc.calc_nonreg(investment_info)

# Output results
print("Post-tax value in a non-registered account: {:.2f}".format(nonreg))
print("Post-tax value in an RRSP account: {:.2f}".format(RRSP))
print("Post-tax value in a TFSA account: {:.2f}".format(TFSA))
