
# Needed information to get serialport package NODE_MODULE_VERSION
# to match VSCode's Electron version.
import os
os.system("npm i -D electron-rebuild")
os.system("rm -rf ./node_modules/serial*")
os.system("npm i")
# Window "Set-ExecutionPolicy RemoteSigned"
os.system("./node_modules/.bin/electron-rebuild -v 7")

# Solution?
# https://github.com/pycom/pymakr-vsc/issues/53