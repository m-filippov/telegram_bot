from core import GitLab
from core.docker import backup
from core import settings

def permision(userId, conectToSkype):
    if userId in settings.permisionUser["admin"]:
        return True
    else:
        conectToSkype.sendMsg(userId + " You do not have permission to run this command.")
        return False


def ComandForSkype(comand,userId,conectToSkype):
    if comand == "$bot":
        conectToSkype.sendMsg("Hi, i Bob builder")
    if comand == "$help":
        conectToSkype.sendMsg("I know these commands:\n"
                              "bot\n"
                              "transfer copy database <source> to <destination>\n"
                              "create backup <environment>"
                              )

    if comand == "$build" and permision(userId, conectToSkype):
        conectToSkype.sendMsg("I`m start build")
        GitLab.Git()
        conectToSkype.sendMsg("Build done")
    if  "$deploy to" in comand and permision(userId, conectToSkype):
        splitJob = comand
        splitJobGetName =  splitJob.split(' ', 3)
        jobName = splitJobGetName[2]
        if jobName in settings.jobsName["JobName"]:
            try:
                conectToSkype.sendMsg("I`m start deploy to " + jobName)
                GitLab.RunJobs(settings.jobsName[jobName], conectToSkype)
                conectToSkype.sendMsg("job done")
            except:
                conectToSkype.sendMsg("somsing wrong")
                conectToSkype.sendMsg(jobTrace)
    if '$transfer copy database ' in comand and permision(userId, conectToSkype):
        s = comand
        split= s.split(' ', 5)
        source = split[3]
        distination = split[5]
        if source in settings.connectToEnvironment["Name"] and distination in settings.connectToEnvironment["Name"]:
            try:
                conectToSkype.sendMsg("I began to transfer a databse from  " + source + " to " + distination)
                backup.RestoreBackupBot(settings.connectToEnvironment[source], settings.connectToEnvironment[distination])
                conectToSkype.sendMsg("Database restore from  " + source + " to " + distination)
            except:
                conectToSkype.sendMsg("I could not restore a backup check please. If there is an error correct it.")
            else:
                conectToSkype.sendMsg(
                    "I dont know such an environment. Please add to the settings that. The environments that I know: " + "\n" \
                    + settings.connectToEnvironment["Name"])
    if '$create backup' in comand and permision(userId, conectToSkype):
        get = comand.split(' ', 3)
        target = get[2]
        if target in settings.connectToEnvironment["Name"]:
            try:
                print settings.timeNow + userId + " create backup"
                conectToSkype.sendMsg("I began to create backup  " + target)
                backup.CreateBackupBot(settings.connectToEnvironment[str(target)])
                conectToSkype.sendMsg("I made a backup and deleted it from the environment " + settings.connectToEnvironment[target])
            except:
                conectToSkype.sendMsg("I could not make a backup check please. If there is an error correct it.")
            else:
                conectToSkype.sendMsg("I dont know such an environment. Please add to the settings that. The environments that I know: " + "\n" \
                                        + settings.connectToEnvironment["Name"])