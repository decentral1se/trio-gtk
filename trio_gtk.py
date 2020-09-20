import traceback

import gi
import trio

gi.require_version("Gtk", "3.0")

from gi.repository import GLib as glib
from gi.repository import Gtk as gtk
from outcome import Error

__all__ = ["run"]


def run(trio_main):
    """Run Trio and PyGTK together."""

    def done_callback(outcome):
        if isinstance(outcome, Error):
            exc = outcome.error
            traceback.print_exception(type(exc), exc, exc.__traceback__)
        gtk.main_quit()

    def glib_schedule(function):
        glib.idle_add(function)

    trio.lowlevel.start_guest_run(
        trio_main,
        run_sync_soon_threadsafe=glib_schedule,
        done_callback=done_callback,
        host_uses_signal_set_wakeup_fd=True,
    )

    gtk.main()
