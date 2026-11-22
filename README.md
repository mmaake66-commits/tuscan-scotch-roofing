# Tuscan Scotch Roofing — Streamlit MVP

A beginner-friendly roofing business MVP with services, a demo project gallery, an indicative GBP quote estimator, and a customer enquiry form.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open http://localhost:8501.

## Deploy to Streamlit Community Cloud
1. Push this repository to GitHub.
2. Open share.streamlit.io and sign in with GitHub.
3. Choose this repository, the main branch, and app.py as the main file.
4. Deploy. No secrets are required for this MVP.

## Quote assumptions
The sample UK planning model starts at £95/m² pitched roofing, £85/m² flat roofing, £55/m² repairs, £120 callout/setting out, and 10% contingency. All values are editable in the sidebar. The result is deliberately non-binding.

## File map
- app.py - Streamlit pages, layout and form UI.
- lib/quote.py - quote calculation and GBP formatting.
- lib/enquiry.py - enquiry validation.
- assets/ - demo SVG gallery images.
- tests/test_quote.py - quote logic tests.
- tests/test_enquiry.py - enquiry validation tests.
- .streamlit/config.toml - Streamlit theme.
- requirements.txt - Python dependency.

The enquiry form only prepares a summary. It does not send or store customer data and requires no secrets.
