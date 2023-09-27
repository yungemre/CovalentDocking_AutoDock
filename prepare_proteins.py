from pymol import cmd
import os

structure_files = os.listdir("protein_structures")

for structure in structure_files:

    cmd.reinitialize()

    cmd.load("structures/" + structure)

    # delete water
    cmd.remove("resn hoh")

    # delete organic including ligands
    cmd.remove("organic")

    # save structure
    cmd.save(structure, "all")
