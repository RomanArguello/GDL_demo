#!/usr/bin/perl -w -I/Users/uncleneptune/perl5/lib/perl5/darwin-thread-multi-2level/

# provide file and path info
open (IN1, "<", $ARGV[0]) || die("cant open dadi file\n"); # open dadi file
open (OUT, ">", "autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_random_allele_polarized_dadi_input_PostProbAnc.txt") || die("cant open metagene output file\n");


while (<IN1>) { # loop over dadi file to get out the chrom and position
    chomp $_;
    @dat = split("\t", $_);
    $chr = $dat[-2];
    $pos = $dat[-1];
        print $chr, "\t", $pos, "\n";
    
    if ($dat[0] eq "Dmel") {  # print the header to the new file
        print OUT join("\t", @dat[0..15]),"\tProbDerAlelles\n";
    }
    
    if ($dat[0] ne "Dmel") { # skip the header

        $com = "awk \'{if (\$1==$pos) {print \$0; exit}}\'  /Volumes/Passport/multi_species_aln/Ancestral_States_for_Fully_Masked_VCFs/chr2L_IBD_masked_biallelic_ZW184removed_AncDer_States.txt";
        $postprob_info = `$com`;
        @pi = split("\t", $postprob_info);
        $PostProb = $pi[-1];
        chomp $PostProb;

        if ($PostProb eq "NA") {
            $PostProb = 1; # leave the ancestral call as is
        }

        # output to new file
        print OUT join("\t", @dat[0..15]), "\t", $PostProb ,"\n";
        
    }
}


close (IN1);