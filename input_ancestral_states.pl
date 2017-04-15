#!/usr/bin/perl -w

open (IN, $ARGV[0]) || die("cant open dadi input file\n"); # open the dadi file w/out the ancestral state file

while (<IN>) {
    if ($_ =~ m/Dmel/) {chomp; print "$_\n"; } # ignore the header and just print it to the new file
    if (!($_ =~ m/Dmel/)) {
        chomp;
        @dat = split("\t",$_);
        
        # get out the chr and position, which will be used to pull out the ancestral state (w/ awk, below)
        $chr = $dat[-2];
        $pos = $dat[-1];

        
        # split up the chroms. here to run more quickly
        if ($chr eq "2L") {
            $AAfile = "/Volumes/Passport/multi_species_aln/Ancestral_States_for_Fully_Masked_VCFs/chr2L_IBD_masked_biallelic_ZW184removed_AncDer_States.txt";
        }
        if ($chr eq "2R") {
            $AAfile = "/Volumes/Passport/multi_species_aln/Ancestral_States_for_Fully_Masked_VCFs/chr2R_IBD_masked_biallelic_ZW184removed_AncDer_States.txt";
        }
        if ($chr eq "3L") {
            $AAfile = "/Volumes/Passport/multi_species_aln/Ancestral_States_for_Fully_Masked_VCFs/chr3L_IBD_masked_biallelic_ZW184removed_AncDer_States.txt";
        }
        if ($chr eq "3R") {
            $AAfile = "/Volumes/Passport/multi_species_aln/Ancestral_States_for_Fully_Masked_VCFs/chr3R_IBD_masked_biallelic_ZW184removed_AncDer_States.txt";
        }
        if ($chr eq "4") {
            $AAfile = "/Volumes/Passport/multi_species_aln/Ancestral_States_for_Fully_Masked_VCFs/chr4_IBD_masked_biallelic_ZW184removed_AncDer_States.txt";
        }
        
        
        # use awk to pull out the ancestral state
        $com = "awk '{if (\$1==$pos) {print \$4; exit}}' $AAfile";
        #print $com, "\n";
        $AS = `$com`;
        chomp $AS;
        
        # error out if there is not data for this variable site <- shouln't happen!
        if (length($AS) < 1) {
            die("no anc. state: $chr\t$pos\n");
        }
        
        # fiddle w/ format 
        $AS = "-$AS-";
        #print "--- ", $AS, "\n";
        
        $dat[1] =  $AS;
        print join("\t", @dat), "\n";

    }
    
}