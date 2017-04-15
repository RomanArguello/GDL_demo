#Include third-party librariesimport vcf#opening IO to the vcf filevcfIO = open("chr21_61YRI_61FIN.vcf", 'r') # Declare IO with vcf inputvcf_data = vcf.Reader(vcfIO) # Declaring the vcf object (requires pyVCF module);#opening IO to output fileoutput_file_name = "dadi_input_file.txt"outIO = open(output_file_name,"w")outIO.write("\t".join(["Human","Chimp","Allele1","YRI","FIN","Allele2","YRI","FIN","Gene","Position\n"]))for variant in vcf_data:    #Declare and re-initialize allele frequencies    yri_freq_alt = 0    yri_freq_ref = 0    fin_freq_alt = 0    fin_freq_ref = 0for idx1,sampleCall in enumerate(variant.samples):    if idx1 >= 0 and idx1 < 61: #( or 0 <= idx1 < 62). If sample belongs to the yoruba population        yri_freq_alt = yri_freq_alt + sampleCall.gt_type #Count number of alternate alleles in the Yoruba sample        if idx1 >= 61 and idx1 < 122: #or 62 <= idx1 < 122            fin_freq_alt = fin_freq_alt + sampleCall.gt_type#Calclate frequencies of the reference alleles (NOTE: this assumes a constant sample size (i.e. no missing data))yri_freq_ref = 122 - yri_freq_altfin_freq_ref = 122 - fin_freq_alt#outIO.write("-{0}-\t---\t{0}\t{2}\t{3}\t{1}\t{4}\t{5}\tchr21\t{6}\n".format(variant.alleles[0],variant.alleles[1],yri_freq_ref,fin_freq_ref,yri_freq_alt,fin_freq_alt,variant.POS))