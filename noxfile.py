import nox


@nox.session
def tests(session):
    session.install('-e', '.')
