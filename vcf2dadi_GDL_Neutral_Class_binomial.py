
#Include third-party libraries
import vcf
import random
fuck = 0

#opening IO to the vcf file
vcfIO = open("autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites.vcf", 'r')  # Declare IO with vcf input
#vcfIO = open("test.vcf", 'r')  # Declare IO with vcf input
vcf_data = vcf.Reader(vcfIO)               # Declaring the vcf object (requires pyVCF module);

#opening IO to output file
output_file_name = "autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_dadi_input.txt"
outIO = open(output_file_name,"w")

#variant = vcf_data.next()  # This could be shown during the course
#calledBase = variant.genotype("NA19197")

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
    
    #Get ancestral state

    #anc_state = variant.INFO["AA"]


    for idx1,sampleCall in enumerate(variant.samples):

        print("call: ", sampleCall.gt_type)
        if idx1 >= 0 and idx1 < 15: 
            if sampleCall.gt_type == None: #Count missing data
                B_miss = B_miss + 1

            if sampleCall.gt_type != None: 

                
                if(sampleCall.gt_type==1): # if the call is heterozygous then random choose one allele

                    myG = [0,2] # the two possible genotype calls (homo ref = 0; homo alt = 2)
                    myS = random.choice(myG) # choose 0 or 2 at radom

                    if (myS == 2):
                        B_freq_alt = B_freq_alt + 1 #Count number of alternate alleles in the Bpop sample

       
        


            
    #Calclate frequencies of the reference alleles
    B_freq_ref = 15 - B_freq_alt - B_miss
    print("###### ", B_freq_ref)



    #outIO.write("-{0}-\t---\t{0}\t{2}\t{3}\t{4}\t{5}\t{6}\t{1}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\n".format(variant.alleles[0], variant.alleles[1],B_freq_ref,I_freq_ref,N_freq_ref,T_freq_ref,Z_freq_ref,B_freq_alt,I_freq_alt,N_freq_alt,T_freq_alt,Z_freq_alt, variant.CHROM,variant.POS))












