import subprocess
import os

# STEP 4
# Generate GPF and DPF files

structure_files = os.listdir("prepared_structures")

for structure in structure_files:
    s = structure[0] + structure[1] + structure[2] + structure[3]

    subprocess.run(
        ["python", "/home/emre/Uni/DrugDiscovery/Projekt/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py",
         "-r", "protein_rigid/" + s + "_rigid.pdbqt", "-x", "ligand_flex/ligand_" + s + "_flex.pdbqt",
         "-l", "ligand_flex/ligand_" + s + "_flex.pdbqt", "-y", "-I", "20", "-o", s + "_priotein.gpf"])

    subprocess.run(["touch", s])  # empty file

    subprocess.run(
        ["python", "/home/emre/Uni/DrugDiscovery/Projekt/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py",
         "-r", "protein_rigid/" + s + "_rigid.pdbqt", "-x", "ligand_flex/ligand_" + s + "_flex.pdbqt",
         "-l", "ligand_flex/ligand_" + s + "_flex.pdbqt", "-o", "ligand_" + s + ".dpf",
         "-p" "move=" + s])