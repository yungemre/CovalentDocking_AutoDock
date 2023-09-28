My approach to the 'flexible side chain' covalent docking as described in the paper:

"Covalent docking using autodock: Two-point attractor and flexible side chain methods"
   http://www.ncbi.nlm.nih.gov/pubmed/26103917

-----------------------------------------------------------------------------------------------

Requirements:

   - python 2.7
   - MGLtools/AutoDockTools

-----------------------------------------------------------------------------------------------

1. Prepare the Dataset:
   
   - Extract ligand and the residue to which it is bound and save it in a pdb file.
   - Delete Cofactors and water in the protein file.
   
  (OR                                                )
  (                                                  )
  (- Delete Cofactors and water in the protein file  )
  (- Align the ligand you want to dock to the protein)
  
  The provided code for this approach does not work!


2. Generate PDBQT files

   Use AutoDockTools to generate PDBQT files.
   
   Protein:
   
	python <path>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py \
	-r prepared_protein.pdb -A hydrogens
	[output: protein.pdbqt]
	
    Ligand:
    	
	python <path>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py
	-r ligand.pdb
	[output: ligand.pdbqt]
	
	
   Look up to which residue the ligand is bound to and change the ligand name and 
   residue number to the corresponding residue name and residue number (in the generated
   PDBQT file).
   
   i.e. 1pwc has a ligand called APNM with residue number 400 in chain A. The ligand is 
        bound to a serine with residue number 62. Change the residue name APNM to SER
        and the residue number to 62.
        APNM A 400 -> SER A 400


3. Generate flexible/rigid PDBQT files:

   Use AutoDockTools to generate flexible/rigid PDBQT files.
   
   Protein:
   
	<path>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_flexreceptor4.py \
	-r protein.pdbqt -s protein:chain:res_nameres_number
	                          (i.e. 1pwc:A:SER400)
	[output: protein_rigid.pdbqt and protein_flex.pdbqt]
	
   Ligand:
   
	<path>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_flexreceptor4.py \
	-r ligand.pdbqt -s ligand:chain:res_nameresnumber
	                     (i.e. ligand_1pwc:A:SER400)
        [output: ligand_rigid.pdbqt and ligand_flex.pdbqt]
        
        
4. Generate GPF and DPF files:

   Use AutoDockTools to generate GPF files for Autogrid:
   
   The rigid files PDBQT files created in step 3 must be placed in the working directory!
   
	<path>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py -r protein_rigid.pdbqt\
                -x ligand_flex.pdbqt\
                -l ligand_flex.pdbqt\
                -y -I 20\
                -o priotein.gpf
	[output: priotein.gpf]
	
	
   The following command instructs the script to dock the covalent ligand as a flexible residue
   and ignore any 'true' ligand ("move='empty'"). To do this, an empty file must be created,
   and it can be done with the following Unix command:
    
    touch empty
    
                
   Use AutoDocktools to generate DPF files for AutoDock:
   
	<path>/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_dpf4.py -r protein_rigid.pdbqt\
                -x ligand_flex.pdbqt\
                -l ligand_flex.pdbqt\
                -o ligand_protein.dpf\
                -p move=empty
	[output: ligand_protein.dpf]

   The DPF file must be manually edited to set the appropriate energy model so that the 
   docking score corresponds to the interaction between the flexible residue 
   (the ligand) and the rigid receptor. For this, the entry:
   
	unbound_model bound

   must be replaced with:

	unbound_energy 0.0
   
   
   In the paper you are supposed to add the following parameter to the DPF file:
	
	rmsdatoms all
   
   However, ADT did not recognise this parameter in my case.
   

5. Run AutoGrid and AutoDock:

	autogrid4 -p priotein.gpf -l priotein.glg
	
	autodock4 -p ligand_protein.dpf -l  ligand_protein.dlg


6. Extract the docked ligand:

  AutoDock4 generates a DLG file for the Docking.
  Use following commands to extract the docked ligand (+ residue) as a pdb file.
  
	grep '^DOCKED' ligand_protein.dlg | cut -c9- > ligand_protein_docking.pdbqt
	
	cut -c-66 ligand_protein_docking.pdbqt > ligand_protein_docking.pdb
	
