from lib.quote import build_quote_breakdown

def test_repair_quote_increases_with_area():
    small=build_quote_breakdown("Repair",20,"Standard","Flexible")
    large=build_quote_breakdown("Repair",40,"Standard","Flexible")
    assert large["base"]==2*small["base"]

def test_complex_urgent_quote_is_higher():
    standard=build_quote_breakdown("Pitched roof",50,"Standard","Flexible")
    complex=build_quote_breakdown("Pitched roof",50,"Complex","Urgent")
    assert complex["high"]>standard["high"]

def test_zero_area_is_rejected():
    try:
        build_quote_breakdown("Flat roof",0,"Standard","Flexible")
        assert False
    except ValueError:
        pass
