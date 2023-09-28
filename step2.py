import subprocess
import os

# STEP 2
# Generate pdbqt files

structure_files = os.listdir("prepared_structures")
ligand_files = os.listdir("prepared_ligands")

# Proteins
for structure in structure_files:

    subprocess.run(
        ["python", "<path>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py",
         "-r", "prepared_structures/" + structure, "-A", "hydrogens"])

# Ligands
for ligand in ligand_files:

    subprocess.run(
        ["python", "<path>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py",
         "-r", "prepared_structures/" + ligand])
