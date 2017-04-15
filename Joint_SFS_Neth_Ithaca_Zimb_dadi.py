import dadi
#import matplotlib.pyplot as pyplot #only if you want ti use the plotting function


# sample sizes & order:
#(1)/0 15: Beijing (B)
#(2)/1 19: Ithaca (I) <-
#(3)/2 19: Netherlands (N) <-
#(4)/3  18: Tasmania (T)
#(5)/4 13: Zimbabwe (Z) <-



#Load data into object of class data_dict
snp_data =  dadi.Misc.make_data_dict("autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_random_allele_polarized_dadi_input.txt")
fs = dadi.Spectrum.from_data_dict(snp_data, pop_ids=['Bpop','Ipop','Npop','Tpop','Zpop'], projections=[13,16,14,15,12], polarized=True)


fs_N_I_Z = fs.marginalize([0,3]) # w/o 1,2,4

fs_N_I_Z.to_file("SFS_N_I_Z.txt")

SegS_fs_N_I_Z = fs_N_I_Z.S()
print("The number of segregating sites:  {0}".format(SegS_fs_N_I_Z))
