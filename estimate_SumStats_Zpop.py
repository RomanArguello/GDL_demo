import dadi
import matplotlib.pyplot as pyplot #only if you want ti use the plotting function


fs_Z = dadi.Spectrum.from_file("SFS_Z_replaced_monomorphic.txt")


# Zimbabwe
Zpop_TW = fs_Z.Watterson_theta()
Zpop_TP = fs_Z.pi()
Zpop_TD = fs_Z.Tajima_D()
print("Zpop.ThetaW: {0}\tZpop.ThetaPi: {1}\tZpop.TajD: {2}\n".format(Zpop_TW,Zpop_TP,Zpop_TD))