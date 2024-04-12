# display-password.py

Displays the most recent cracked password on the Pwnagotchi display.
It currently processes every .potfile file on the `/root/hanshakes` directory.
Feel free to help out if you want.

# Installation

## Via installation script

This script will execute the same steps as the manual installation.

1. SSH into your Pwnagotchi and run the following command:
``` bash
git clone https://github.com/nothingbutlucas/pwnagotchi-display-password-plugin
cd pwnagotchi-display-password-plugin
```
2. Run the installation script as root:
``` bash
sudo ./install.sh

```
It will install the plugin to your configured `main.custom_plugins` variable on `/etc/pwnagotchi/config.toml`. If you don't have a `main.custom_plugins` variable, it will add it to the end of the file and then ask you to declare it

3. Reboot the Pwnagotchi daemon to ensure all changes are applied, you can do so with the following command:
``` bash
sudo systemctl restart pwnagotchi
```

This also allow you to update the plugin by running  ```git pull``` on the plugin repo directory.

## Manual

1. SSH into your Pwnagotchi and create a new folder for third-party Pwnagotchi plugins. I use `/root/custom_plugins/` but it doesn't really matter: `mkdir /root/custom_plugins/`
2. Grab the `display-password.py` and `display-password.toml` file from this Github repo and put it into that custom plugins directory.
3. Edit `/etc/pwnagotchi/config.toml` and change the `main.custom_plugins` variable to point to the custom plugins directory you just created: `main.custom_plugins = "/root/custom_plugins/"`
4. In the same `/etc/pwnagotchi/config.toml` file, add the following lines to enable the plugin:
``` bash
main.plugins.display-password.enabled = true # true or false
main.plugins.display-password.orientation = "horizontal" # horizontal or vertical
main.plugins.display-password.position = "30,160" # Depends on screen
main.plugins.display-password.last_only = false # false will loop to every file and password. true will only display the most recent password from every potfile
```
Once the above steps are completed, reboot the Pwnagotchi daemon to ensure all changes are applied, you can do so with the following command:
``` bash
sudo systemctl restart pwnagotchi
```

# Screenshot:

![display-password.py](/screenshot.jpg?raw=true "display-password.py")
