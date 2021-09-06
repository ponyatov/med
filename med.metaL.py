from metaL import *

p = Project(
    title='minimized code editor',
    about='''
* inspired by DOS Navigator & MultiEdit
* console-oriented to be usable in embedded systems
''') \
    | Rust()

p.toml.deps // f'{"tui":<22} = "0.16"'

p.sync()
