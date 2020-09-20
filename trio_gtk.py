import gi
import trio

gi.require_version("Gtk", "3.0")

from gi.repository import GLib as glib
from gi.repository import Gtk as gtk

__all__ = ["run"]


def run(trio_main):
    """Run Trio and PyGTK together."""

    async def _trio_main():
        async with trio.open_nursery() as nursery:
            nursery.start_soon(trio_main, nursery)
            while gtk.main_level() != 0:
                await trio.sleep(1)

    def done_callback(outcome):
        glib.idle_add(gtk.main_quit)

    def glib_schedule(function):
        glib.idle_add(function)

    trio.lowlevel.start_guest_run(
        _trio_main,
        run_sync_soon_threadsafe=glib_schedule,
        done_callback=done_callback,
        host_uses_signal_set_wakeup_fd=True,
    )

    gtk.main()
