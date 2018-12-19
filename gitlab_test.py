import gitlab

gl = gitlab.Gitlab('https://gitlab.intecracy.com/', private_token='EYPqkTYDR4AZrB-9FR5_')

gl.auth()
projects = gl.projects.list()
for project in projects:
    print(project)

