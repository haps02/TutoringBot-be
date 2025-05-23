import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .tools import calculate_unary_operation, calculate_binary_operation, lookup_constant
from google.adk.tools import load_memory

greeting_agent = Agent(
         model="gemini-2.0-flash-exp",
            name="greeting_agent",
            instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. " "Do not engage in any other conversation or tasks.",
            # Crucial for delegation: Clear description of capability
            description="Handles simple greetings and hellos",
            
 )

farewell_agent = Agent(
          model="gemini-2.0-flash-exp",
            name="farewell_agent",
            instruction="You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message. "
                        "Do not perform any other actions.",
            # Crucial for delegation: Clear description of capability
            description="Handles simple farewells and goodbyes",
            
 )
 
# calculator_agent = Agent(
#           model="gemini-2.0-flash-exp",
#           name="calculator_agent",
#           instruction="You are the calculator agent. Your ONLY task is to perform mathematical calculations and give correct answer. Also if there's any error(like divide by zero), respond to it. Do not perform any other actions.",
#           description="Handles mathematical calculations",
#
#  )
 
math_agent = Agent(
          model="gemini-2.0-flash-exp",
          name="math_agent",
          instruction="You are the math tutor Agent. Your ONLY task is to provide a correct answers to math problems. Also always use the calculator tool for mathematical calculations, if possible. Do not perform any other actions. Use the 'load_memory' tool if the answer might be in past conversations. ",
          description="Handles math questions",
          tools=[calculate_binary_operation, calculate_unary_operation, load_memory]
            
 )
 
physics_agent = Agent(
          model="gemini-2.0-flash-exp",
          name="physics_agent",
          instruction="You are the physics tutor Agent. Your ONLY task is to provide a correct answers to physics problems. Also use the calculator tool for simple mathematical calculations, if possible. Take constants values from the 'lookup_constant' tool, if present, otherwise search online (no need to tell user about this). Use the 'load_memory' tool if the answer might be in past conversations. Do not perform any other actions.",
          description="Handles physics questions",
          tools=[calculate_binary_operation, calculate_unary_operation, lookup_constant, load_memory]
            
 )
 
biology_agent = Agent(
          model="gemini-2.0-flash-exp",
          name="biology_agent",
          instruction="You are the biology tutor Agent. Your ONLY task is to provide a correct answers to biology problems. Do not perform any other actions.",
          description="Handles biology questions",
            
 )


root_agent = Agent(
        name="weather_agent_v2", 
        model="gemini-2.0-flash-exp",
        description="You are the main coordinator app. - Your main task: send the query to the corresponding agent. - Delegation Rules: - If the user gives a simple greeting (like 'Hi', 'Hello'), delegate to `greeting_agent`. - If the user gives a simple farewell (like 'Bye', 'See you'), delegate to `farewell_agent`. - If the user asks a question related to math, physics or biology delegate to the corresponding agent from the sub_agents. - After getting the responses, format the final text properly such that it can be directly shown in the frontend. - For other queries, state clearly if you cannot handle them.",
        sub_agents=[greeting_agent, farewell_agent, physics_agent, math_agent, biology_agent],
)
