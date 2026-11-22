def validate_enquiry(name,email,postcode,phone,message,consent):
    errors=[]
    if len(name.strip())<2: errors.append("Please enter your name.")
    if "@" not in email or "." not in email: errors.append("Please enter a valid email address.")
    clean_postcode="".join(postcode.strip().upper().split())
    if len(clean_postcode)<5 or len(clean_postcode)>7: errors.append("Please enter a valid UK postcode.")
    if phone.strip():
        digits="".join(ch for ch in phone if ch.isdigit())
        if len(digits)<10 or len(digits)>15: errors.append("Please enter a valid phone number or leave it blank.")
    if len(message.strip())<10: errors.append("Please provide at least 10 characters of project detail.")
    if not consent: errors.append("Please confirm that we may contact you.")
    return errors
