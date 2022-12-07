## chatGPT demo OpenAI in PYTHON

### Step 1: register account with personal use:
confirm email and cellphone
https://beta.openai.com/signup
### Step 2: get token 

get personal token 
https://beta.openai.com/account/api-keys

consult Usage credit
https://beta.openai.com/account/usage

### Step 3: install requirements in env 
`pip install -r requirements.txt`

### Optional, export API KEY
`echo "export OPENAI_API_KEY='sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx'" >> ~/.bashrc`

`source ~/.bashrc`

`echo $OPENAI_API_KEY`


### Step 4: execute script 
`python example_chat_gpt.py`

example Instruction:

**Convert this text to a programmatic command: i want an algorithm to convert audio to text in python**

Result
![Diagram process](chatGTP.png)

