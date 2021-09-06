from metaL import *

p = Project(
    title='minimized code editor',
    about='''''') \
    | Rust()

p.toml.deps // f'{"tui":<22} = "0.16"'

p.sync()
