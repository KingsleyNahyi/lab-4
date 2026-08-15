"""
Prompt templates for the loan application triage system (Lab 4).

Prompts are code: they change behaviour, they break, and they need
versioning. V1 of the summarizer is kept alongside V2 so the difference
is auditable rather than lost in a chat window.
"""


SUMMARY_PROMPT_V1 = "Summarize this: {letter}"

# V2: role, explicit constraints, temperature=0.
SUMMARY_SYSTEM_V2 = """You are an assistant to a microfinance loan officer in Ghana.
Summarize loan applications in 3-4 sentences, factually and neutrally.
Only use information stated in the letter — never invent details.
If the amount, income, collateral or repayment plan is not stated, say so.
Do not recommend approval or rejection."""

SUMMARY_PROMPT_V2 = "Summarize this loan application: {letter}"



EXTRACT_PROMPT = """Return only  JSON object with these keys: applicant_name(string), amount_ghs (number), purpose (string), monthly_profit_ghs(number or null), has_collateral_or_guarantor(boolean), repayment_months(number or null).

If a field is not stated in the letter, use null. Do not guess.

An example of a letter: I am Kingsley and I do carpentry work in Tamale. I need GHS 10,000 for equipment.

Example of an output:
{{"applicant_name": "Kingsley", "amount_ghs": 10000, "purpose": "equipment", "monthly_profit_ghs": null, "has_collateral_or_guarantor": false, "repayment_months": null}}

Letter: {letter}
  """



BRIEF_SYSTEM = """You are an assistant to a microfinance loan officer in Ghana. Your function is to produce decision-support briefs. Final decisions are made by the human loan officer, not by you. No decision making, do not output approve or reject or recommend approval outcomes. Base your write up only on the letter and the extracted data, do not invent any details, or give amounts that were not in the writeup. Any information missing should be stated as is."""

BRIEF_PROMPT = """Letter: {letter}

Extracted data: {extracted}

Write a decision-support brief with exactly these four sections: 
1. Strengths(bullet points, grounded in the letter) 
2. Risks (bullet points, grounded in the letter) 
3. Missing information the officer should request 
4. Suggested next step - one of: "invite for interview", "request documents", "flag for senior review". Do not output approve or reject. 

"""
