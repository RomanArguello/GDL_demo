#!/usr/bin/perl -w -I/Users/uncleneptune/perl5/lib/perl5/darwin-thread-multi-2level/
use Math::Random qw(random_binomial);

# provide file and path info
open (IN1, "<", $ARGV[0]) || die("cant open dadi file\n"); # open dadi file w/ the prob. of anc. state column added 

# open output file
open (OUT, ">", "temp_dadi_input.txt") || die("cant open temp output file output file\n");


# count the number of postitions that lack a post. prob. assignment.
$no_pp = 0;
$num_flips = 0;

while (<IN1>) { # loop over dadi file to get out the chrom and position and anc. state probs.
    chomp $_;
    @dat = split("\t", $_);
    $postprob = $dat[-1]; # get the post prob.
    
    if ($dat[0] eq "Dmel") {  # print the header to the new file
        print OUT join("\t", @dat[0..15]), "\n"; # <-------
    }
    if ($dat[0] ne "Dmel") { # skip the header
        
        if ($postprob eq "NA") {
            $no_pp++;
            $postprob = 1; # leave the ancestral call as is
        }

        my $v = random_binomial(1, 1, $postprob); # indicator variable; if=0 then flip the frequency

        if ($v==0) {
            $anc_call = $dat[1];
            $Allele1 = "-".''.$dat[2].''."-";
            $Allele2 = "-".''.$dat[8].''."-";

            # get the variant that will be the replacement anc. state
            if ($anc_call eq $Allele1) { 
                $new_anc = $Allele2;
            }
            if ($anc_call eq $Allele2) {
                $new_anc = $Allele1;
            }
            
            $num_flips++;
            print OUT $dat[0], "\t", $new_anc, "\t", join("\t", @dat[2..15]), "\n"; # <-------
        }
        
        else {
            print OUT  join("\t", @dat[0..15]), "\n"; # <-------
        }
    }
}


close (IN1);
#print("# of SNPs w/out a post. prob. assigned to ancestral state: ", $no_pp, "\n");
print("# of SNPs w/ reassigned freq: ", $num_flips, "\n");