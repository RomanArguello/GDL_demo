__author__ = 'stefan & roman'

#Include third-party libraries
import vcf
import random

#opening IO to the vcf file
vcfIO = open("autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites.vcf", 'r')  # Declare IO with vcf input
#vcfIO = open("test.vcf", 'r')  # Declare IO with vcf input


vcf_data = vcf.Reader(vcfIO)               # Declaring the vcf object (requires pyVCF module);

#opening IO to output file
output_file_name = "autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_random_allele_dadi_input.txt"
outIO = open(output_file_name,"w")


#print calledBase.gt_type

outIO.write("\t".join(["Dmel","AncState","Allele1","Bpop","Ipop","Npop","Tpop","Zpop","Allele2","Bpop","Ipop","Npop","Tpop","Zpop","Gene","Position\n"]))

for variant in vcf_data:
    #print variant
    #Declare and re-initialize allele frequencies & missing data
    B_freq_alt = 0
    B_freq_ref = 0
    B_miss = 0

    I_freq_alt = 0
    I_freq_ref = 0
    I_miss = 0

    N_freq_alt = 0
    N_freq_ref = 0
    N_miss = 0

    T_freq_alt = 0
    T_freq_ref = 0
    T_miss = 0

    Z_freq_alt = 0
    Z_freq_ref = 0
    Z_miss = 0
    


    for idx1,sampleCall in enumerate(variant.samples):

        # Bpop
        if idx1 >= 0 and idx1 < 15: 
            if sampleCall.gt_type == None: #Count missing data
                B_miss = B_miss + 1

            if sampleCall.gt_type != None:
                #print(sampleCall.gt_type)
                
                if (sampleCall.gt_type==2):
                    B_freq_alt = B_freq_alt + 1 #Count number of alternate alleles in the Bpop sample
                if(sampleCall.gt_type==1): # if the call is heterozygous then random choose one allele
                    myG = [0,2] # the two possible genotype calls (homo ref = 0; homo alt = 2)
                    myS = random.choice(myG) # choose 0 or 2 at radom

                    if (myS == 2):
                        #print("alt")
                        B_freq_alt = B_freq_alt + 1 #Count number of alternate alleles in the Bpop sample


        # Ipop
        if idx1 >= 16 and idx1 < 34:
            if sampleCall.gt_type == None:  #Count missing data
                I_miss = I_miss + 1

            if sampleCall.gt_type != None:

                if (sampleCall.gt_type==2):
                    I_freq_alt = I_freq_alt + 1 #Count number of alternate alleles in the Ipop sample
                    
                if(sampleCall.gt_type==1): # if the call is heterozygous then random choose one allele
                    myG = [0,2] # the two possible genotype calls (homo ref = 0; homo alt = 2)
                    myS = random.choice(myG) # choose 0 or 2 at radom

                    if (myS == 2):
                        I_freq_alt = I_freq_alt + 1 #Count number of alternate alleles in the Ipop sample

        # Npop
        if idx1 >= 34 and idx1 < 53:
            if sampleCall.gt_type == None:  #Count missing data
                N_miss = N_miss + 1

            if sampleCall.gt_type != None:

                if (sampleCall.gt_type==2):
                    N_freq_alt = N_freq_alt + 1 #Count number of alternate alleles in the Npop sample
                    
                if(sampleCall.gt_type==1): # if the call is heterozygous then random choose one allele
                    myG = [0,2] # the two possible genotype calls (homo ref = 0; homo alt = 2)
                    myS = random.choice(myG) # choose 0 or 2 at radom

                    if (myS == 2):
                        N_freq_alt = N_freq_alt + 1 #Count number of alternate alleles in the Npop sample 
            
        # Tpop
        if idx1 >= 53 and idx1 < 71:
            if sampleCall.gt_type == None:  #Count missing data
                T_miss = T_miss + 1

            if sampleCall.gt_type != None:

                if (sampleCall.gt_type==2):
                    T_freq_alt = T_freq_alt + 1 #Count number of alternate alleles in the Tpop sample
                    
                if(sampleCall.gt_type==1): # if the call is heterozygous then random choose one allele
                    myG = [0,2] # the two possible genotype calls (homo ref = 0; homo alt = 2)
                    myS = random.choice(myG) # choose 0 or 2 at radom

                    if (myS == 2):
                        T_freq_alt = T_freq_alt + 1 #Count number of alternate alleles in the Tpop sample 
            
        # Zpop
        if idx1 >= 71 and idx1 < 84:
            if sampleCall.gt_type == None:  #Count missing data
                Z_miss = Z_miss + 1

            if sampleCall.gt_type != None:

                if (sampleCall.gt_type==2):
                    Z_freq_alt = Z_freq_alt + 1 #Count number of alternate alleles in the Zpop sample
                    
                if(sampleCall.gt_type==1): # if the call is heterozygous then random choose one allele
                    myG = [0,2] # the two possible genotype calls (homo ref = 0; homo alt = 2)
                    myS = random.choice(myG) # choose 0 or 2 at radom

                    if (myS == 2):
                        Z_freq_alt = Z_freq_alt + 1 #Count number of alternate alleles in the Zpop sample   
        

            
            
    #Calclate frequencies of the reference alleles (NOTE: this assumes a constant sample size (i.e. no missing data))
    B_freq_ref = 15 - B_freq_alt - B_miss
    I_freq_ref = 19 - I_freq_alt - I_miss
    N_freq_ref = 19 - N_freq_alt - N_miss
    T_freq_ref = 18 - T_freq_alt - T_miss
    Z_freq_ref = 13 - Z_freq_alt - Z_miss

    #B_freq_ref = 15 - B_freq_alt - B_miss
    #I_freq_ref = 19 - I_freq_alt - I_miss
    #N_freq_ref = 19 - N_freq_alt - N_miss
    #T_freq_ref = 18 - T_freq_alt - T_miss
    #Z_freq_ref = 13 - Z_freq_alt - Z_miss

    
    #print("-{0}-\t---\t{0}\t{2}\t{3}\t{4}\t{5}\t{6}\t{1}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\n".format(variant.alleles[0], variant.alleles[1],B_freq_ref,I_freq_ref,N_freq_ref,T_freq_ref,Z_freq_ref,B_freq_alt,I_freq_alt,N_freq_alt,T_freq_alt,Z_freq_alt, variant.CHROM,variant.POS))

    outIO.write("-{0}-\t---\t{0}\t{2}\t{3}\t{4}\t{5}\t{6}\t{1}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\n".format(variant.alleles[0], variant.alleles[1],B_freq_ref,I_freq_ref,N_freq_ref,T_freq_ref,Z_freq_ref,B_freq_alt,I_freq_alt,N_freq_alt,T_freq_alt,Z_freq_alt, variant.CHROM,variant.POS))














