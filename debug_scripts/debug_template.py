"""
ImSwitch debug script template.

Define a function `run(ctx)`. It is called when you trigger this script via
the REST API (DebugController/runScript). The `ctx` object gives you full
access to the live ImSwitch instance:

    ctx.master              -> MasterController (all *Manager instances)
    ctx.commChannel         -> CommunicationChannel
    ctx.setupInfo           -> active setup info
    ctx.logger              -> logger (use instead of print)
    ctx.getController(name) -> another controller, e.g. "Experiment"
    ctx.stop_requested()    -> True once a stop was requested via the API
    ctx.sleep(seconds)      -> stop-aware sleep
    ctx.run_coroutine(coro) -> run an async call on the server event loop

The script runs in a background thread and shares the process, so you have
access to all managers and controllers. Any exception is caught and reported
back through the API instead of crashing ImSwitch.

You can set breakpoints in this file and debug it natively while ImSwitch is
running, since it is hot-loaded from disk on every run.
"""


def run(ctx):
    ctx.logger.info("Debug script started")

    # Example: list available hardware
    detectors = ctx.master.detectorsManager.getAllDeviceNames()
    positioners = ctx.master.positionersManager.getAllDeviceNames()
    lasers = ctx.master.lasersManager.getAllDeviceNames()

    ctx.logger.info(f"Detectors:   {detectors}")
    ctx.logger.info(f"Positioners: {positioners}")
    ctx.logger.info(f"Lasers:      {lasers}")

    # Example: cooperative long-running loop that can be stopped via the API
    # for i in range(100):
    #     if ctx.stop_requested():
    #         ctx.logger.info("Stop requested, exiting loop")
    #         break
    #     ctx.logger.info(f"working... {i}")
    #     ctx.sleep(1.0)

    # The returned value is reported back through getJobStatus (JSON-safe).
    return {
        "detectors": detectors,
        "positioners": positioners,
        "lasers": lasers,
    }
