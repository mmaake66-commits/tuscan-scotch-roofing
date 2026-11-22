DEFAULT_ASSUMPTIONS = {"pitched_rate":95.0,"flat_rate":85.0,"repair_rate":55.0,"callout":120.0,"contingency":0.10}

def format_gbp(value): return f"£{value:,.0f}"

def build_quote_breakdown(work_type, roof_area, complexity, urgency, assumptions=None):
    if roof_area <= 0: raise ValueError("Roof area must be greater than zero")
    values = DEFAULT_ASSUMPTIONS.copy()
    if assumptions: values.update(assumptions)
    rates = {"Repair":values["repair_rate"],"Pitched roof":values["pitched_rate"],"Flat roof":values["flat_rate"]}
    if work_type not in rates: raise ValueError("Unknown work type")
    cm={"Standard":1.0,"Challenging":1.15,"Complex":1.35}; um={"Flexible":1.0,"Urgent":1.12}
    if complexity not in cm: raise ValueError("Unknown complexity")
    if urgency not in um: raise ValueError("Unknown timing")
    area_rate=float(rates[work_type]); cmp=cm[complexity]; ump=um[urgency]
    contingency=max(0.0,min(float(values["contingency"]),0.30))
    base=roof_area*area_rate*cmp*ump; subtotal=base+float(values["callout"])
    return {"area_rate":area_rate,"base":base,"callout":float(values["callout"]),"contingency":contingency,"complexity_multiplier":cmp,"urgency_multiplier":ump,"low":round(subtotal*(1-contingency*0.5)),"high":round(subtotal*(1+contingency))}
