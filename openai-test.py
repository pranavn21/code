from openai import OpenAI
client = OpenAI()

syscontent = "You are a virtual political assistant, skilled in providing expertise in United States (U.S.) politics and the history of U.S. politics, including U.S. politicians."


# Self-Consistency
print("Self-Consistency")
print("Q: Was there ever a US Senator that represented the state of Texas and whose alma mater was Rutgers New Brunswick??")
for x in range(0, 3):
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": syscontent},
    {"role": "user", "content": "Was there ever a US Senator that represented the state of Texas and whose alma mater was Rutgers New Brunswick?"}
  ]
  )   

  print(completion.choices[0].message)

print("\n\n")


print("SAC3")
# SAC3
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": syscontent},
    {"role": "user", "content": "Has there ever been a US Senator who represented Texas whose alma mater was Rutgers New Brunswick?"}
  ]
)
completion2 = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": syscontent},
    {"role": "user", "content": "Who is or was a US Senator for Texas who went to Rutgers New Brunswick making it their alma mater?"}
  ]
)
completion3 = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": syscontent},
    {"role": "user", "content": "Can you find me a Rutgers alumnus who served as a Senator in the United States Senate for the state of Texas?"}
  ]
)

print("Q: Has there ever been a US Senator who represented Texas whose alma mater was Rutgers New Brunswick?")
print(str(completion.choices[0].message) + "\n")

print("Q: Who is or was a US Senator for Texas who went to Rutgers New Brunswick making it their alma mater?")
print(str(completion2.choices[0].message)+ "\n")

print("Q: Can you find me a Rutgers alumnus who served as a Senator in the United States Senate for the state of Texas?")
print(str(completion3.choices[0].message)+ "\n")