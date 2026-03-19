"""Minimal script prototyping the logic of an ARINC 661 User Application (UA)."""

import datetime
import os
from pathlib import Path
from time import sleep

from taf.a661libgen_rev9_v1 import UA, Server, Standard_rev9_v1
import taf.a661libutil

# Initialize SCADE ARINC 661 Widget API and constants
Standard_rev9_v1()
PERIOD = 0.020  # in seconds
SCADE_INSTALL = os.getenv("SCADE_INSTALL")
if not Path(SCADE_INSTALL).exists():
    print(f"Invalid SCADE installation path, exiting.\nPath is: {SCADE_INSTALL}")
    exit(code=1)

# Start a SCADE CDS server as a background task
cds = Server(
    exe=f"{SCADE_INSTALL}/SCADE A661/bin/A661Server.exe",
    df_list=["graphics/DF/UA_1.bin"],
)
cds.run(debug="all")

# Parse DF and connect to the server as UA 1
df_from_sgfx = taf.a661libutil.create_df_from_sgfx(
    sgfx_path="graphics/UADF.sgfx",
    a661_path=f"{SCADE_INSTALL}/SCADE A661/server/a661_description/a661.xml",
)
ua1 = UA(ua_id=1).connect()
ua1.register_df(df_object=df_from_sgfx)

# Start polling loop
pushbutton = ua1.get_widget(layer_id=1, widget_id=3)
target_label = ua1.get_widget(layer_id=1, widget_id=2)
while True:
    notifs = ua1.get_notifications()
    if notifs:
        for notif in notifs:
            if (
                notif["RuntimeCommand"] == "A661_NOTIFY_WIDGET_EVENT"
                and notif["WidgetIdent"] == pushbutton.widget_id
                and notif["EventIdent"] == "A661_EVT_SELECTION"
            ):
                now = datetime.datetime.now()
                ua1.send_block(target_label.string(now.strftime("%H:%M:%S")))
    sleep(PERIOD)
