import gitlab

gl = gitlab.Gitlab('https://gitlab.intecracy.com/', private_token='SMbM8xa1sTxpdz3ptBbn')

gl.auth()
projects = gl.projects.list()
for project in projects:
    print(project)

