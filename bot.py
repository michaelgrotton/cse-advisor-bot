import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('z9eG60WrWK4GWw5K3ibZ0QcMb-zlnzI4Axhq4u_wTQqq')
assistant = AssistantV2(
    version='2018-09-20',
    authenticator=authenticator)
assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com')

#########################
# Sessions
#########################

session = assistant.create_session("a1a77e9e-7878-4cec-8db7-fe34c3fb24c4").get_result()
print("Bot: Hey, how can I help you?")

while(True):
    # get user question
    print(">", end=" ")
    question = input()
    print("You: " + question)

    # call api
    response = assistant.message(
        "a1a77e9e-7878-4cec-8db7-fe34c3fb24c4", session["session_id"],
        input={'text': question},
        context={
            'metadata': {
                'deployment': 'myDeployment'
            }
        }).get_result()
    print("Bot: " + response["output"]["generic"][0]["text"])

assistant.delete_session("a1a77e9e-7878-4cec-8db7-fe34c3fb24c4", session["session_id"]).get_result()

# logs = assistant.list_logs(
#     "<YOUR ASSISTANT ID>"
# )
# print(json.dumps(logs, indent=2))
