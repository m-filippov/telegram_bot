from datetime import datetime

PatchToChangelog = "C:\Users\maksym.fillipov\PycharmProjects\\telegram_bot\core\git\CHANGELOG.md"
PatchToJson = "C:\Users\maksym.fillipov\PycharmProjects\\telegram_bot\core\git\packeg.json"
SkypeUser = ""
SkypePassword = ""
TestChat = ""
projectID = 183
time = datetime.now()
timeNow = str(time.strftime("%Y-%m-%d-%H.%M.%S")+": ")

connectToEnvironment = {
    "Name":     "demo_1, demo_2, demo_3, prod, cpc_qa, qa, stage",

    }

permisionUser = {
    "admin": "live:m_tech_4"
}


jobsName = {
    "JobName": "qa, test",
    "qa": "deploy_QA",
    "test": "run_test",
    "artifact": "test_artifact"
}

if "QA" in connectToEnvironment["Name"]:
    print "ok"
elif "qa" in connectToEnvironment:
    print connectToEnvironment["Name"]