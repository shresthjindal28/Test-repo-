import os
import json
import pprint
from dotenv import load_dotenv
from portia import (
    Config,
    LLMProvider,
    Portia,
    example_tool_registry,
)
from tools.find_significance import FindSignificanceTool
from tools.fetch_text_img import FetchTextAndImgTool
from tools.fetch_img import FetchImgTool
from tools.slack_tool import SlackTool


def init_agent(code):
    print("loading env...")

    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # Instantiate a Portia instance. Load it with the config and with the example tools.
    portia = Portia(config=openai_config, tools=[FindSignificanceTool(),FetchTextAndImgTool(),FetchImgTool(),SlackTool()])

    print("portia planning and running...")

    # if you get error here, then it is most probably in tools
    plan = portia.plan(f"""
You will a github push made by a user to a particular repo. All the tools that you are provided with ONLY ACCEPT STRING AS ARGUMENT. It will be provides here below:
{code}
First get significance of the code changes made in this github push. Then get the code summary and code snippet. Then if the significance is low, ignore but if sginificance is medium or high Extract the code snippet in text format from code_snippet and get an image from it. Then send this text code summary in the slack channel.
    """)
    print(plan)
    print(plan.pretty_print())

    run= portia.run_plan(plan)

    dict_output=json.loads(run.model_dump_json(indent=2))
    summary:str=dict_output["outputs"]["final_output"]["summary"]

    print("\n\n")
    print(f"\033[92m{summary}\033[0m")

