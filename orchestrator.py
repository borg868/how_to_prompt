import pandas as pd

# Read the CSV file
raw_data = pd.read_csv("agent_master_list.csv")
raw_data.head()

#acquire the agent name list -- seems succesful. but note the carriage return
agent_name_list = raw_data['agent name'].tolist()


#agent descriptions
temp_list = pd.DataFrame(raw_data[['agent name','description']])
temp_list

alist = temp_list['agent name'].to_dict()
dlist = temp_list['description'].to_dict()

agent_description_list  = ""
newline = '\n'
for count, value in enumerate(alist):
    index = count+1
    func_name = alist[value]
    func_desc = dlist[value]
    temp_string = f"""{index}) {func_name} {newline} {func_desc} {newline}"""
    #print(temp_string)
    agent_description_list += temp_string

#agent examples
temp_list = pd.DataFrame(raw_data[['example','thought','action']])
temp_list

elist = temp_list['example'].to_dict()
tlist = temp_list['thought'].to_dict()
alist = temp_list['action'].to_dict()

agent_example_list  = ""
newline = '\n'
for count, value in enumerate(elist):
    index = count+1
    example = elist[value]
    thought = tlist[value]
    action  = alist[value]

    temp_string = f""" Example {newline}
--------- {newline} {example} {newline} --------- {newline} Thought: {newline} {thought} {newline} Action: {newline} ``` {newline} {action}{newline} ``` {newline}"""
    #print(temp_string)
    agent_example_list += temp_string


question = """what are the latest earnings of Tesla?"""

common_instruction = f"""
Given a user query, your job is to recommend the tool to answer user queries. You have access to the following tools:\n\n

{agent_description_list}

Use the following format:
Question: the input question you must answer
Thought: you should always think bout what to do
Action:
```
Must be ONE of {agent_name_list}
```

{agent_example_list}

Begin! Suggest ONLY ONE tool.
REMEMBER to format is Thought then Action: ```\\n$TOOL_NAME\\n``` including the 3 BACKTICKS!

Take a deep breath and work on this step by step. 
Question: {question}
""".strip()


