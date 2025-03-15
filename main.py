import json

from analyze_tweets import analyze

tweets = [
    "Economic transformation, trade affair and boasting tourism sector Yes it's a strong pillar in easing mobility",
    "The sector appreciates and applauds the efforts of the Chief Executive Officer. These efforts will be discussed further at this year's Pearl of Africa Tourism Expo Conferences. You are invited to attend.",
    "London flights are long over due Get serious folks",
    "Kati mbu tusiime mbu mukola nyoo, ku buubii kwemutude",
    "We love to fly @UG_Airlines but last minute cancellation of flights without information is disturbing, mostly EBB to DXB, you returning from vacation, at airport is when you know flight is cancelled, you have a date to resume work even the next flight date won’t be communicated",
]


analysis_results = analyze(tweets)

# Print results
print(json.dumps(analysis_results, indent=2))
