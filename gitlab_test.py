import gitlab

gl = gitlab.Gitlab('https://gitlab.intecracy.com/', private_token='token')

gl.auth()
projects = gl.projects.list()
for project in projects:
    print(project)

