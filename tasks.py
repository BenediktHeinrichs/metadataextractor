import os
from invoke import task


@task
def install(ctx, develop=False, pty=True):
    ctx.run("python setup.py develop")
    req_file = "requirements.txt"
    cmd = "pip install --upgrade -r {}".format(req_file)
    ctx.run(cmd, pty=pty)
