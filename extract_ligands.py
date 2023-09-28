from pymol import cmd
import os

structure_files = os.listdir("protein_structures")

for structure in structure_files:

    cmd.reinitialize()
    cmd.load("protein_structures/" + structure)

    cmd.select("sele_ligand", "byres (last organic)")

    cmd.select("sele_ligand_and_aa", "byres (bound_to sele_ligand)")

    cmd.save("prepared_ligands/ligand_" + structure, "sele_ligand_and_aa")


cmd.reinitialize()
cmd.load("structures/4f49.pdb")
cmd.select("sele_ligand", "byres (first organic)")
cmd.select("sele_ligand_and_aa", "byres (bound_to sele_ligand)")
cmd.save("ligands_aa/ligand_4f49.pdb", "sele_ligand_and_aa")


cmd.reinitialize()
cmd.load("structures/3pr0.pdb")
cmd.select("sele_ligand", "byres (first organic)")
cmd.select("sele_ligand_and_aa", "byres (bound_to sele_ligand)")
cmd.save("ligands_aa/ligand_3pr0.pdb", "sele_ligand_and_aa")