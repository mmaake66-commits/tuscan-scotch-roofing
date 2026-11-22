from lib.enquiry import validate_enquiry

def valid(**overrides):
    values={"name":"Alex Smith","email":"alex@example.com","postcode":"SW1A 1AA","phone":"07123456789","message":"There is a leak above the kitchen.","consent":True}
    values.update(overrides)
    return validate_enquiry(**values)

def test_valid_enquiry(): assert valid()==[]

def test_invalid_contact_and_consent():
    errors=valid(email="bad",postcode="no",consent=False)
    assert any("email" in error.lower() for error in errors)
    assert any("postcode" in error.lower() for error in errors)
    assert any("contact" in error.lower() for error in errors)

def test_optional_phone_may_be_blank(): assert valid(phone="") == []
