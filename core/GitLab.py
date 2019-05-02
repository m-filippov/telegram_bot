import gitlab
import settings
import os
from git import Repo
import git
import changelog
import time


gl = gitlab.Gitlab()

gl.auth()
#name = 'deploy_QA'

def Git():
#    git.Git.
#    Repo.pull("https://maksym.fillipov:dxQyb5fNbLnBxvvpFjyc@gitlab.intecracy.com/DevOpsSoftengi/devops_test.git","C:\\Users\\maksym.fillipov\\PycharmProjects\\telegram_bot\\core\\git")
    if not os.path.isdir("C:\\Users\\maksym.fillipov\\PycharmProjects\\telegram_bot\\core\\git"):
        os.makedirs("C:\\Users\\maksym.fillipov\\PycharmProjects\\telegram_bot\\core\\git")
    if not os.path.isdir("C:\\Users\\maksym.fillipov\\PycharmProjects\\telegram_bot\\core\\git\\.git"):
        Repo.clone_from("https://maksym.fillipov:dxQyb5fNbLnBxvvpFjyc@gitlab.intecracy.com/DevOpsSoftengi/devops_test.git","C:\\Users\\maksym.fillipov\\PycharmProjects\\telegram_bot\\core\\git")
    Repo("C:\\Users\\maksym.fillipov\\PycharmProjects\\telegram_bot\\core\\git").remotes.origin.pull()

    changelog.ChangeLog(settings.PatchToChangelog)

    repo = Repo("C:\\Users\\maksym.fillipov\\PycharmProjects\\telegram_bot\\core\\git")
    repo.git.add(update=True)
    repo.index.commit("Bob builder")
    origin = repo.remote(name='origin')
    origin.push()

#def RunJobs (nameJobs, conectToSkype):
def TestJob(nameJobs):
    project = gl.projects.get(settings.projectID)
    pipelines = project.pipelines.list()[0]
    pipelineId = project.pipelines.get(pipelines.id)
    jobsList = pipelineId.jobs.list()
    print jobsList
    for list in jobsList:
        nameJob = project.jobs.get(list.name, lazy=True)
        idJob = project.jobs.get(list.id, lazy=True)
        jobStatus = project.jobs.get(list.status, lazy=True)
#        print idJob

        if format(str(nameJobs)) in str(nameJob):
            print "ok"
            idJob.play()
            print project.jobs.get(list.id, lazy=True)
#            print idJob.trace()

            print jobStatus
            time.sleep(3)
            if JobStatus(jobStatus, idJob):
#                conectToSkype.sendMsg('Done deploy to ' + nameJobs)
                 print "OK"
            elif not JobStatus(jobStatus, idJob):
#                conectToSkype.sendMsg(str(idJob.trace()))
#                conectToSkype.sendMsg('ERROR deploy to ' + nameJobs)
                print (idJob.trace(-5))
            break

def JobStatus(jobStatus, idJob):
    time.sleep(3)
    if "running" in str(jobStatus) or "manual" in str(jobStatus):
            JobStatus(jobStatus, idJob)
            print ("Runing")
    elif "success" in str(jobStatus):
#        idJob.artifacts("C:\\Users\\maksym.fillipov\\PycharmProjects\\telegram_bot\\core")
        print "success"
        return True
    elif "failed" in str(jobStatus):
        print "Filed"
        return False
#    jobs = project.jobs.get(jobsId.id, lazy=True)
#    print jobs
TestJob(settings.jobsName["artifact"])
