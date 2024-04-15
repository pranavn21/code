from openai import OpenAI
from array import *
client = OpenAI()


quesBank = [] 

# Index 0: Self-Consistency question, 1-3: SAC3, 4: System content parameter for GPT
quesBank.insert(-1, ["Was there ever a US Senator that represented the state of Texas and whose alma mater was Rutgers New Brunswick?",
                 "Has there ever been a US Senator who represented Texas whose alma mater was Rutgers New Brunswick?",
                 "Who is or was a US Senator for Texas who went to Rutgers New Brunswick making it their alma mater?",
                 "Can you find me a Rutgers alumnus who served as a Senator in the United States Senate for the state of Texas?",
                 "You are a virtual political assistant, skilled in providing expertise in United States (U.S.) politics and the history of U.S. politics, including U.S. politicians."
                 ])
quesBank.insert(-1, ["Is 5939 a prime number?",
                 "Is the number 5939 prime?",
                 "Are the only factors of 5939 itself and one?",
                 "Can 5939 only be divided by 1 and 5939?",
                 "You are a virtual mathematical assistant, skilled in providing expertise in mathematics, including number theory, prime numbers, etc."
                 ])
quesBank.insert(-1, ["Was there ever a US senator that represented the state of Mississippi and whose alma mater was University of Chicago?",
                 "Has there ever been a US Senator who represented Mississippi whose alma mater was University of Chicago?",
                 "Who is or was a US Senator for Mississippi who went to University of Chicago making it their alma mater?",
                 "Can you find me a University of Chicago alumnus who served as a Senator in the United States Senate for the state of Mississippi?",
                 "You are a virtual political assistant, skilled in providing expertise in United States (U.S.) politics and the history of U.S. politics, including U.S. politicians."
                 ])
quesBank.insert(-1, ["Is 3691 a prime number?",
                 "Is the number 3691 prime?",
                 "Are the only factors of 3691 itself and one?",
                 "Can 3691 only be divided by 1 and 3691?",
                 "You are a virtual mathematical assistant, skilled in providing expertise in mathematics, including number theory, prime numbers, etc."
                 ])

def runAI(questionList, startIndex, endIndex, GPTversion): 
  index = 0
  for index in range(startIndex, endIndex):
    # Self-Consistency
    print("Self-Consistency")
    print("Q: " + str(questionList[index][0]))
    for x in range(0, 3):
      completion = client.chat.completions.create(
      model=GPTversion,
      messages=[
        {"role": "system", "content": questionList[index][4]},
        {"role": "user", "content": questionList[index][0]}
      ]
      )   

      print(str(x+1) + ") " + str(completion.choices[0].message.content) + "\n---\n")

    print("\n\n")

    # SAC3
    print("SAC3")
    
    print("Q: " + str(questionList[index][1]))
    completion = client.chat.completions.create(
      model=GPTversion,
      messages=[
        {"role": "system", "content": questionList[index][4]},
        {"role": "user", "content": questionList[index][1]}
      ]
    )
    print(str(completion.choices[0].message.content) + "\n")


    print("Q: " + str(questionList[index][2]))
    completion2 = client.chat.completions.create(
      model=GPTversion,
      messages=[
        {"role": "system", "content": questionList[index][4]},
        {"role": "user", "content": questionList[index][2]}
      ]
    )
    print(str(completion2.choices[0].message.content)+ "\n")


    print("Q: " + str(questionList[index][3]))
    completion3 = client.chat.completions.create(
      model=GPTversion,
      messages=[
        {"role": "system", "content": questionList[index][4]},
        {"role": "user", "content": questionList[index][3]}
      ]
    )
    print(str(completion3.choices[0].message.content)+ "\n")
    print("\n\n ----- END OF QUESTION ----- \n\n")

runAI(quesBank, 0, len(quesBank), "gpt-3.5-turbo-0125")
