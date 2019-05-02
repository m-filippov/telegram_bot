import gitlab
from core import settings


gl = gitlab.Gitlab('https://gitlab.intecracy.com/', private_token='dxQyb5fNbLnBxvvpFjyc')

gl.auth()

project = gl.projects.get(settings.projectID)
print(project)
pipelines = project.pipelines.get(26452)
print pipelines
pipelines_jobs = pipelines.jobs.list()[2]
jobs = project.jobs.get(pipelines_jobs.id, lazy=True)
#jobs = project.jobs.get(52986)
print jobs
#print jsonString
jobs.play()
#jobs.trace()

#id_job = project.jobs.get()
#print id_job
