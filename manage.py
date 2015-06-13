#!/usr/bin/env python
import os

from flask_script import Manager, Shell

from app import create_app


config_opt = os.getenv('FLASKCONFIG') or 'default'

print "CONFIGURED FOR " + config_opt

app = create_app(config_opt)

manager = Manager(app)


def make_shell_context():
    return dict(app=app)  # , db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
