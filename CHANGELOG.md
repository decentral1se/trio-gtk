# trio-gtk 3.0.0 (2020-10-11)

- Re-introduce PyGObject with more backwards compatible bounds. I should
  explain here a little after all the backwards and forwards on this. Because
  PyGObject has some system dependency issues, it looked impossible to include
  it as a Python dependency here and not create issues for people who are
  installing who may be relying on their system package manager installed
  PyGObject. However, after speaking with Gtk devs, I have a set of bounds
  which supports compatibility with older distributions with some fairly OK
  guarantees. I want to include the dependencies here so people can just "pip
  install trio-gtk" and hopefully get moving fast from there without having to
  deal with system package manager installed packages.

# trio-gtk 2.0.0 (2020-10-08)

- Remove PyGObject as Python dependency.

# trio-gtk 1.0.1 (2020-10-08)

- Relax bounds on PyGObject (>= 3.36).

# trio-gtk 1.0.0 (2020-09-21)

- Remove mandatory `nursery` argument for trio main.

# trio-gtk 0.1.1 (2020-09-20)

- Fix traceback handling on `done_callback`.
- Exit gracefully calling `gtk.main_quit` directly.

# trio-gtk 0.1.0 (2020-09-20)

- Initial pre-alpha release.
