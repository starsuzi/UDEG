from transformers import PegasusTokenizer, PegasusForConditionalGeneration

model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-xsum')
ARTICLE_TO_SUMMARIZE = (
"PG&E stated it scheduled the blackouts in response to forecasts for high winds "
"amid dry conditions. The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were "
"scheduled to be affected by the shutoffs which were expected to last through at least midday tomorrow."
)
inputs = tokenizer([ARTICLE_TO_SUMMARIZE], max_length=1024, return_tensors='pt')
# Generate Summary
summary_ids = model.generate(inputs['input_ids'])

print([tokenizer.decode(g, skip_special_tokens=True) for g in summary_ids])