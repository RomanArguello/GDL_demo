import dadi
import matplotlib.pyplot as pyplot #only if you want ti use the plotting function


# sample sizes & order:
#(1)/0 15: Beijing (B)
#(2)/1 19: Ithaca (I)
#(3)/2 19: Netherlands (N)
#4)/3  18: Tasmania (T)
#(5)/4 13: Zimbabwe (Z)



#Load data into object of class data_dict
snp_data =  dadi.Misc.make_data_dict("autosomal_IBD_Callability_masked_ZW184removed_biallelic_neutral_sites_random_allele_polarized_dadi_input.txt")
fs = dadi.Spectrum.from_data_dict(snp_data, pop_ids=['Bpop','Ipop','Npop','Tpop','Zpop'], projections=[13,16,14,15,12], polarized=True)


print("JAFS: {0}\n".format(fs))



# marginalize to get pop-specific SFS
fs_B = fs.marginalize([1,2,3,4])
fs_I = fs.marginalize([0,2,3,4])
fs_N = fs.marginalize([0,1,3,4])
fs_T = fs.marginalize([0,1,2,4])
fs_Z = fs.marginalize([0,1,2,3])
# print(fs)
# fs.to_file()

# pairise 
#fs_B_I = fs.marginalize([2,3,4]) # w/o 0,1
#fs_B_N = fs.marginalize([1,3,4]) # w/o 0,2
#fs_B_T = fs.marginalize([1,2,4]) # w/o 0,3
#fs_B_Z = fs.marginalize([1,2,3]) # w/o 0,4

#fs_N_I = fs.marginalize([0,3,4]) # w/o 2,1
#fs_N_T = fs.marginalize([0,1,4]) # w/o 2,3
#fs_N_Z = fs.marginalize([0,1,3]) # w/o 2,4

#fs_B_I = fs.marginalize([2,3,4])
#fs_B_I = fs.marginalize([2,3,4])

#fs_B_I = fs.marginalize([2,3,4])

print("Bpop.SFS: {0}\n".format(fs_B))
print("Ipop.SFS: {0}\n".format(fs_I))
print("Npop.SFS: {0}\n".format(fs_N))
print("Tpop.SFS: {0}\n".format(fs_T))
print("Zpop.SFS: {0}\n".format(fs_Z))
print("\n\n")


Fst = fs.Fst ()
print("Overall Fst: {0}\n".format(Fst))

#Fst = fs.Fst ()
#print("Overall Fst: {0}\n".format(Fst))



# Beijing
Bpop_TW = fs_B.Watterson_theta()
Bpop_TP = fs_B.pi()
Bpop_TD = fs_B.Tajima_D()
print("Bpop.ThetaW: {0}\tBpop.ThetaPi: {1}\tBpop.TajD: {2}\n".format(Bpop_TW,Bpop_TP,Bpop_TD))

# Ithaca
Ipop_TW = fs_I.Watterson_theta()
Ipop_TP = fs_I.pi()
Ipop_TD = fs_I.Tajima_D()
print("Ipop.ThetaW: {0}\tIpop.ThetaPi: {1}\tIpop.TajD: {2}\n".format(Ipop_TW,Ipop_TP,Ipop_TD))

# Netherlands
Npop_TW = fs_N.Watterson_theta()
Npop_TP = fs_N.pi()
Npop_TD = fs_N.Tajima_D()
print("Npop.ThetaW: {0}\tNpop.ThetaPi: {1}\tNpop.TajD: {2}\n".format(Npop_TW,Npop_TP,Npop_TD))

# Tazmania
Tpop_TW = fs_T.Watterson_theta()
Tpop_TP = fs_T.pi()
Tpop_TD = fs_T.Tajima_D()
print("Tpop.ThetaW: {0}\tTpop.ThetaPi: {1}\tTpop.TajD: {2}\n".format(Tpop_TW,Tpop_TP,Tpop_TD))

# Zimbabwe
Zpop_TW = fs_Z.Watterson_theta()
Zpop_TP = fs_Z.pi()
Zpop_TD = fs_Z.Tajima_D()
print("Zpop.ThetaW: {0}\tZpop.ThetaPi: {1}\tZpop.TajD: {2}\n".format(Zpop_TW,Zpop_TP,Zpop_TD))
