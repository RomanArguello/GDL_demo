#!/usr/bin/perl -w -I/Users/uncleneptune/perl5/lib/perl5/darwin-thread-multi-2level/


# provide file and path info
open (IN1, "<", $ARGV[0]) || die("cant open dadi file\n"); # open dadi file w/ the prob. of anc. state column added 
#   open (OUT, ">>", "SFSTEST.txt") || die("cant open outputted SFS file\n");

#@SFS = (0,0,0,0,0,0,0,0,0,0,0,0,0);
#$q=1;
while (<IN1>) { # loop over dadi file to get out the chrom and position and anc. state probs.
    #print $q, "\n";
    chomp $_;
    #print $_, "\n";
    @dat = split("\t", $_);
    
    if ($dat[0] ne "Dmel") {  # ignore the header
        $anc_call = $dat[1];
        $anc_call =~ s/-//g; 
        $Allele1 = $dat[2];
        $Allele2 = $dat[8];
        $postprob = $dat[-1];
        #print join(",", $anc_call, $Allele1, $Allele2), "\n";
    
        if ($anc_call eq $Allele1) {$der_count = $dat[13];}
        if ($anc_call eq $Allele2) {$der_count = $dat[7];}
        #print "Derived Count: ", $der_count, "\n"; 
        if ($der_count > 0){
            print $der_count, "\t", $postprob, "\n";
            #print $postprob, "\t", $der_count, "\n";
            #print $SFS[$der_count-1], " ----\n";
            #$SFS[$der_count-1] = $SFS[$der_count-1] + 1;
            #print @SFS, "\n";
            #exit;
        }
    #$q++;
    }
    
}
#print join("\t", @SFS), "\n";
close(IN1);