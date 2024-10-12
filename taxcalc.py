def calc_RRSP(info):

    contribution = info["contribution"]
    return_rate = info["return_rate"]
    years = info["years"]
    dep_tax = info["dep_tax"]
    with_tax = info["with_tax"]

    RRSP_contribution = contribution / (1 - dep_tax / 100) # Sum of a geometric series

    RRSP_pretax = RRSP_contribution * ((1 + return_rate / 100) ** years)
    RRSP = RRSP_pretax * (1 - with_tax / 100)
    return RRSP 

def calc_TFSA(info):
    contribution = info["contribution"]
    return_rate = info["return_rate"]
    years = info["years"]
    
    TFSA = contribution * ((1 + return_rate / 100) ** years)
    return TFSA

def calc_nonreg(info):
    contribution = info["contribution"]
    return_rate = info["return_rate"]
    years = info["years"]
    with_tax = info["with_tax"]
    eq_port = info["eq_port"]

    nonreg_pretax = contribution * ((1 + return_rate / 100) ** years)
    nonreg_gain = nonreg_pretax - contribution # ACB is not taxed
    eff_taxrate = with_tax / 100 * (eq_port / 100 * 0.5 + (1 - eq_port / 100))
    nonreg_gain_posttax = nonreg_gain * (1 - eff_taxrate)

    nonreg = nonreg_gain_posttax + contribution
    return nonreg
