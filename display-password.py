from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import logging
import random
import os


class DisplayPassword(plugins.Plugin):
    __author__ = "@nagy_craig"
    __fork_author__ = "@nothingbutlucas"
    __version__ = "1.2.0"
    __license__ = "GPL3"
    __description__ = "A plugin to display recently cracked passwords"

    def on_loaded(self):
        logging.info("[DISPLAY-PASSWORD] loaded")

    def on_ui_setup(self, ui):
        try:
            if ui.is_waveshare_v2():
                h_pos = (0, 95)
                v_pos = (180, 61)
            elif ui.is_waveshare_v1():
                h_pos = (0, 95)
                v_pos = (170, 61)
            elif ui.is_waveshare144lcd():
                h_pos = (0, 92)
                v_pos = (78, 67)
            elif ui.is_inky():
                h_pos = (0, 83)
                v_pos = (165, 54)
            elif ui.is_waveshare2in7():
                h_pos = (0, 153)
                v_pos = (216, 122)
            elif ui.is_waveshare1in54V2():
                h_pos = (0, 92)
                v_pos = (70, 170)
            else:
                h_pos = (0, 91)
                v_pos = (180, 61)

            if self.options["orientation"] == "vertical":
                selected_position = v_pos
            else:
                selected_position = h_pos

            if self.options["position"]:
                try:
                    position_values = str(self.options["position"]).split(",")
                    position_x = int(position_values[0])
                    position_y = int(position_values[1])
                    selected_position = (position_x, position_y)
                except Exception as e:
                    logging.error(
                        f"[DISPLAY-PASSWORD] Error reading configuration: {e}"
                    )

            ui.add_element(
                "display-password",
                LabeledValue(
                    color=BLACK,
                    label="",
                    value="",
                    position=selected_position,
                    label_font=fonts.Bold,
                    text_font=fonts.Small,
                ),
            )
        except Exception as e:
            logging.error(f"[DISPLAY-PASSWORD] {e}")

    def on_unload(self, ui):
        try:
            with ui._lock:
                ui.remove_element("display-password")
        except Exception as e:
            logging.error(f"[DISPLAY-PASSWORD] {e}")

    def on_ui_update(self, ui):
        logging.debug("[DISPLAY-PASSWORD] Updating UI")
        try:
            if self.options.get("last_only") is True:
                last_only = True
            else:
                last_only = False
        except Exception as e:
            logging.error(f"[DISPLAY-PASSWORD] Error reading configuration: {e}")
            last_only = False
        try:
            # Choose a random potfile
            potfiles = os.listdir("/root/handshakes")
            potfiles = [x for x in potfiles if x.endswith(".potfile")]
            file = random.choice(potfiles)
            # Read the potfile
            with open(f"/root/handshakes/{file}", "r") as file:
                lines = file.readlines()
                if len(lines) > 0:
                    if not last_only:
                        # Choose a random password to show
                        line = random.choice(lines)
                    else:
                        line = lines[-1]
                    # Shows only the last password
                    line = ":".join(line.split(":")[2:])
                    ui.set("display-password", f"{line}")
        except RuntimeError as e:
            logging.debug(f"[DISPLAY-PASSWORD] {e}")
        except Exception as e:
            logging.error(f"[DISPLAY-PASSWORD] {e}")
