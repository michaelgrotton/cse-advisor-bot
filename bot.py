import json
import config
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(config.api_key)
assistant = AssistantV2(
    version='2018-09-20',
    authenticator=authenticator)
assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com')

#########################
# Sessions
#########################

session = assistant.create_session(config.application_id).get_result()
print("Bot: Hey, how can I help you?")

while(True):
    # get user question
    print(">", end=" ")
    question = input()
    print("You: " + question)

    # call api
    response = assistant.message(
        config.application_id, session["session_id"],
        input={'text': question},
        context={
            'metadata': {
                'deployment': 'myDeployment'
            }
        }).get_result()
    print("Bot: " + response["output"]["generic"][0]["text"])

assistant.delete_session(config.application_id, session["session_id"]).get_result()

# logs = assistant.list_logs(
#     "<YOUR ASSISTANT ID>"
# )
# print(json.dumps(logs, indent=2))
