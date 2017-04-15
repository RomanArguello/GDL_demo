import dadi
import matplotlib.pyplot as pyplot #only if you want ti use the plotting function


# sample sizes, orders:
#(1) 15: Beijing (B)
#(2) 19: Ithaca (I)
#(3) 19: Netherlands (N)
#4) 18: Tasmania (T)
#(5) 13: Zimbabwe (Z)

for x in range(1, 16):

    #Load data into object of class data_dict
    snp_data =  dadi.Misc.make_data_dict("autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_random_allele_polarized_dadi_input_postprob_anc_above95.txt")
    fs= dadi.Spectrum.from_data_dict(snp_data, pop_ids=['Bpop','Ipop','Npop','Tpop','Zpop'], projections=[x,1,1,1,1],polarized=True)

    # marginalize
    fs_B = fs.marginalize([1,2,3,4])
    #fs_I = fs.marginalize([0,2,3,4])
    #fs_N = fs.marginalize([0,1,3,4])
    #fs_T = fs.marginalize([0,1,2,4])
    #fs_Z = fs.marginalize([0,1,2,3])


    S_B = fs_B.S()
    print("Bpop {0}\t{1}".format(x,S_B))
