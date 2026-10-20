import pandas as pd
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

adsl = pd.read_sas("external/submissions-pilot1/adam/adsl.xpt", format="xport", encoding="utf-8")
print("N subjects:", len(adsl))
print(adsl["TRT01P"].value_counts(), "\n")

client = Anthropic()
cols = ", ".join(adsl.columns)
msg = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=300,
    messages=[{"role": "user", "content":
        f"These are the variables in a CDISC ADaM ADSL dataset: {cols}. "
        "Which variables define the safety, ITT, and efficacy populations? Answer in 3 short lines."}],
)
print("Claude says:\n" + msg.content[0].text)
print(f"\nTokens used: {msg.usage.input_tokens} in / {msg.usage.output_tokens} out")
