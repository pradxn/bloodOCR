import openai

openai.api_key = open("key.txt", "r").read().strip('\n')
'''
completion = openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  temperature=0,
  max_tokens=7
)

print(completion)
'''

def greetings(params):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Say hello to " + params + " in Deutsch!",
        temperature=1,
        max_tokens=2048
    )
    #total_response = response
    selected_response = response.choices[0].text.strip()
    return selected_response


name = input('Whats your name? :\n')
x = greetings(name)
print(x)

'''

row_name = input("Enter test name: ")
rowStr = str(row_name)
#rowStr = "\"" + row_name + "\""


def dataParsed(params):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Values of " + params + " in " + strX,
        temperature=1,
        max_tokens=2048
    )
    #total_response = response
    selected_response = response.choices[0].text.strip()
    return selected_response

output = dataParsed(rowStr)
print(output)
'''