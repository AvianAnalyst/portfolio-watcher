from invoke import task


@task
def ready_python(c):
    c.run('pipenv run migrate')


@task
def ready_vue(c):
    with c.cd('vue_frontend'):
        c.run('npm install')


@task(ready_python)
def start_django(c):
    c.run('pipenv run start')
    with c.cd('vue_frontend'):
        c.run('npm run serve')

@task(ready_vue)
def start_vue(c):
    with c.cd('vue_frontend'):
        c.run('npm run serve')
