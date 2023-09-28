import subprocess
import os

# STEP 5
# Run AutoGrid and AutoDock

gpf_files = os.listdir("gpf_files")

for gpf in gpf_files:
    name = gpf[:-3]
    subprocess.run(
        ["autogrid4", "-p", "gpf_files/" + name + "gpf", "-l", name + "glg"])

dpf_files = os.listdir("dpf_files")

for dpf in dpf_files:
    name = dpf[:-3]
    subprocess.run(
        ["autodock4", "-p", "dpf_files/" + name + "dpf", "-l", name + "dlg"])