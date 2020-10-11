# trio-gtk

[![Build Status](https://drone.autonomic.zone/api/badges/decentral1se/trio-gtk/status.svg?ref=refs/heads/master)](https://drone.autonomic.zone/decentral1se/trio-gtk)

## Trio guest mode wrapper for PyGTK

Using the [Trio guest mode](https://trio.readthedocs.io/en/latest/reference-lowlevel.html#using-guest-mode-to-run-trio-on-top-of-other-event-loops) feature, we can run both the Trio and PyGTK event loops alongside each other in a single program. This allows us to make use of the Trio library and the usual `async`/`await` syntax and not have to directly manage thread pools. This library provides a thin wrapper for initialising the guest mode and exposes a single public API function, `trio_gtk.run` into which you can pass your Trio main function.

## Install

```sh
$ pip install trio-gtk
```

Please note, `trio-gtk` does install [pygobject](https://gitlab.gnome.org/GNOME/pygobject) directly as a Python package. We use relaxed bounds to ensure that the hard dependency on system packages (see [cairo integration documentation](https://pygobject.readthedocs.io/en/latest/guide/cairo_integration.html) will not stop you having a successful installation. This may not always work out. If you see a build error during your Pip installation, please raise a ticket and we will see what we can do.

## Example

```python
import gi
import trio

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk as gtk

import trio_gtk


class Example(gtk.Window):
    def __init__(self, nursery):
        gtk.Window.__init__(self, title="Example")

        self.button = gtk.Button(label="Create a task")
        self.button.connect("clicked", self.on_click)
        self.add(self.button)

        self.counter = 0
        self.nursery = nursery

        self.connect("destroy", gtk.main_quit)
        self.show_all()

    def on_click(self, widget):
        self.counter += 1
        self.nursery.start_soon(self.say_hi, self.counter)

    async def say_hi(self, count):
        while True:
            await trio.sleep(1)
            print(f"hi from task {count}")


async def main():
    async with trio.open_nursery() as nursery:
        Example(nursery)
        await trio.sleep_forever()


trio_gtk.run(main)
```
