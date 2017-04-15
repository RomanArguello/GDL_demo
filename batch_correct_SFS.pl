#!/usr/bin/perl -w 


# repeatedly generate new dadi-like files based on the post prob. of ancestral state

for (my $i=1; $i <= 300; $i++) {
    print "working on: $i\n";
    $com1 = "perl correct_SFS.pl autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_random_allele_polarized_dadi_input_postprob_anc.txt"; # "correct SFS"
    $com2 = "perl compute_SFS_from_dadi_file.pl temp_dadi_input.txt >> TEMPSFS.out"; # collect the SFS
    
    `$com1`;
    `$com2`;
    `rm temp_dadi_input.txt`;   
}