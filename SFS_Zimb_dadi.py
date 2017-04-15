import dadi
import matplotlib.pyplot as pyplot #only if you want ti use the plotting function
import sys
from sys import argv


# sample sizes, orders:
#(1) 15: Beijing (B)
#(2) 19: Ithaca (I)
#(3) 19: Netherlands (N)
#(4) 18: Tasmania (T)
#(5) 13: Zimbabwe (Z)



#Load data into object of class data_dict
snp_data =  dadi.Misc.make_data_dict("autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_random_allele_polarized_dadi_input.txt")
#snp_data =  dadi.Misc.make_data_dict("autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_random_allele_polarized_dadi_input_postprob_anc_above95.txt")
fs = dadi.Spectrum.from_data_dict(snp_data, pop_ids=['Bpop','Ipop','Npop','Tpop','Zpop'], projections=[13,16,14,15,12], polarized=True)

#folded = fs.fold()

# marginalize
#sfs_Z = folded.marginalize([0,1,2,3])
sfs_Z = fs.marginalize([0,1,2,3])

sfs_Z.to_file("SFS_Z.txt")

SegS_fs_Z = sfs_Z.S()
print("The number of segregating sites:  {0}".format(SegS_fs_Z))
