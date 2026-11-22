import streamlit as st
from lib.enquiry import validate_enquiry
from lib.quote import DEFAULT_ASSUMPTIONS, build_quote_breakdown, format_gbp

st.set_page_config(page_title="Tuscan Scotch Roofing", page_icon="🏠", layout="wide")
st.markdown("""<style>
.hero{padding:3.5rem 3rem;border-radius:20px;background:linear-gradient(135deg,#173f35,#285e4f);color:white;margin-bottom:1.5rem}.hero h1{font-size:2.7rem;margin:0 0 .5rem}.hero p{max-width:680px;font-size:1.12rem;color:#e8f2ee}.stat{border:1px solid #dce7e2;border-radius:14px;padding:1rem;background:white;height:100%}.demo-label{display:inline-block;background:#eef5f2;color:#285e4f;border-radius:999px;padding:.2rem .65rem;font-size:.78rem;font-weight:700}
</style>""",unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Tuscan Scotch Roofing")
    st.caption("Complete roofing services")
    page=st.radio("Navigate",["Home","Services","Project gallery","Quote estimator","Enquiry"],label_visibility="collapsed")
    st.divider()
    st.caption("Example UK coverage — update this copy to match the business.")

if page=="Home":
    st.markdown("""<div class="hero"><h1>Roofing work, planned properly.</h1><p>From repairs and flat roofs to complete replacements, get clear service information and an indicative estimate before arranging a site visit.</p></div>""",unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    for col,number,label in [(c1,"UK-wide","service messaging"),(c2,"Free","initial enquiry"),(c3,"No-obligation","site assessment")]:
        with col: st.markdown(f"<div class=\"stat\"><strong style=\"font-size:1.35rem\">{number}</strong><br><span style=\"color:#557069\">{label}</span></div>",unsafe_allow_html=True)
    st.write("")
    left,right=st.columns([1.15,1])
    with left:
        st.subheader("Built around a clear process")
        st.markdown("1. Tell us what needs attention\n2. Review a non-binding estimate\n3. Arrange a detailed on-site assessment\n4. Confirm scope, timing and a formal quotation")
    with right:
        st.subheader("Start with an estimate")
        st.caption("Use Quote estimator in the navigation.")

elif page=="Services":
    st.title("Roofing services")
    st.write("Final scope and price require an on-site assessment.")
    services=[("Roof repairs","Targeted repairs for slipped tiles, flashing, leaks and weather damage."),("Flat roofing","Practical repairs and replacement systems for garages and extensions."),("Roof replacement","Planned removal and replacement for tired or damaged pitched roofs."),("Guttering and drainage","Inspection and replacement of external rainwater components."),("Roofline care","Maintenance for exposed roof edges and weather-facing timber."),("Maintenance","Scheduled checks to identify small issues before they become larger leaks.")]
    for start in range(0,len(services),2):
        cols=st.columns(2)
        for col,(name,description) in zip(cols,services[start:start+2]):
            with col:
                with st.container(border=True): st.subheader(name); st.write(description)

elif page=="Project gallery":
    st.title("Project gallery")
    st.info("These are demonstration concepts, not records of completed customer work.",icon="ℹ️")
    projects=[("Demo 01","Pitched roof refresh","assets/project-pitched.svg"),("Demo 02","Flat roof extension","assets/project-flat.svg"),("Demo 03","Roofline renewal","assets/project-roofline.svg")]
    cols=st.columns(3)
    for col,(tag,title,filename) in zip(cols,projects):
        with col:
            st.markdown(f"<span class=\"demo-label\">{tag} · SAMPLE DATA</span>",unsafe_allow_html=True)
            st.image(filename,use_container_width=True); st.subheader(title)

elif page=="Quote estimator":
    st.title("Indicative quote estimator")
    st.warning("Planning estimate only — not a quotation or offer. Actual costs require an on-site assessment.",icon="!")
    with st.sidebar:
        st.header("Estimate assumptions")
        pitched=st.number_input("Pitched roof £/m²",20.0,500.0,float(DEFAULT_ASSUMPTIONS["pitched_rate"]),5.0)
        flat=st.number_input("Flat roof £/m²",20.0,500.0,float(DEFAULT_ASSUMPTIONS["flat_rate"]),5.0)
        repair=st.number_input("Repair £/m²",10.0,500.0,float(DEFAULT_ASSUMPTIONS["repair_rate"]),5.0)
        callout=st.number_input("Callout/setting out",0.0,5000.0,float(DEFAULT_ASSUMPTIONS["callout"]),50.0)
        contingency=st.slider("Contingency",0,30,int(DEFAULT_ASSUMPTIONS["contingency"]*100),1)
        assumptions={"pitched_rate":pitched,"flat_rate":flat,"repair_rate":repair,"callout":callout,"contingency":contingency/100}
    c1,c2=st.columns(2)
    with c1:
        work_type=st.selectbox("Main work",["Repair","Pitched roof","Flat roof"])
        area=st.number_input("Roof area (m²)",1.0,10000.0,50.0,5.0)
    with c2:
        complexity=st.select_slider("Access and complexity",["Standard","Challenging","Complex"],value="Standard")
        urgency=st.selectbox("Timing",["Flexible","Urgent"])
    breakdown=build_quote_breakdown(work_type,area,complexity,urgency,assumptions)
    st.divider(); st.subheader("Planning range")
    low=format_gbp(breakdown["low"]); high=format_gbp(breakdown["high"])
    st.metric("Estimated range",f"{low} – {high}")
    m1,m2,m3=st.columns(3)
    m1.metric("Base work",format_gbp(breakdown["base"]))
    m2.metric("Callout/setting out",format_gbp(breakdown["callout"]))
    m3.metric("Contingency",str(contingency)+"%")
    with st.expander("How this estimate is calculated"):
        st.write(f"Area: {area:,.1f} m²")
        st.caption("VAT, waste disposal, structural repairs and specialist permissions are not separately included.")

elif page=="Enquiry":
    st.title("Customer enquiry")
    st.write("Share a few details and prepare an enquiry summary.")
    with st.form("enquiry_form"):
        c1,c2=st.columns(2)
        with c1:
            name=st.text_input("Name *",max_chars=80)
            email=st.text_input("Email *",max_chars=120)
            postcode=st.text_input("Postcode *",max_chars=12)
        with c2:
            phone=st.text_input("Phone",max_chars=30)
            service=st.selectbox("Service",["Roof repair","Flat roofing","Roof replacement","Guttering","Maintenance","Not sure"])
            preferred=st.selectbox("Preferred contact",["Email","Phone"])
        message=st.text_area("How can we help? *",max_chars=1500)
        consent=st.checkbox("I am happy to be contacted about this enquiry. *")
        submitted=st.form_submit_button("Prepare enquiry",type="primary")
    if submitted:
        errors=validate_enquiry(name,email,postcode,phone,message,consent)
        if errors:
            for error in errors: st.error(error)
        else:
            st.success("Your enquiry looks ready.")
            summary="Roofing enquiry\n\nName: "+name.strip()+"\nEmail: "+email.strip()+"\nPhone: "+(phone.strip() or "Not provided")+"\nPostcode: "+postcode.strip()+"\nService: "+service+"\nPreferred contact: "+preferred+"\n\nDetails:\n"+message.strip()
            st.text_area("Enquiry summary",summary,height=220)
            st.caption("No enquiry data is sent or stored by this demo. Connect a production form to an email service or database.")
