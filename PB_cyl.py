import numpy as np
import scipy.special as sp
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(5.91,7.72),dpi=300)

#x1=(0.005,0.01,0.02,0.05,0.1,0.2,0.5,1.0,1.41,1.68,1.83,1.99)
#y1=(0.00625,0.0125,0.025,0.0625,0.125,0.25,0.7,1.6,3.2,7.0,12.5,1000)

y1 = np.geomspace(0.00625, 1000.0)
x1 = (-1.0+np.sqrt(1.0+1.6*y1**2))/y1

x2=(10.0,10.0)
y2=(1.e-3,1.e3)

x3 = np.geomspace(0.01, 200.0)
y3 = 0.2*sp.iv(1,x3)/sp.iv(0,x3)

x4=(0.005,0.8)
y4=(200.0,1.25)

x5=(0.005,200.0)
y5=(1.0,1.0)

y6=(0.001,1000.0)
x6=(1.0,1.0)

y6=(0.001,1000.0)
x6=(1.0,1.0)

x7=(0.005,1.0)
y7=(0.005,1.0)

x8=(0.005,1.0)
y8=(200.0,1.0)

#x9 = np.array([0.005, 0.1])
#y9 = 0.06/x9
x9 = np.geomspace(0.005, 0.4)
y9 = 0.2/x9

x10 = np.array([0.1, 1.5])
y10 = 100/x10

#x11=(1.26,1.26)
#y11=(1.0e-3,1.0e3)
#plt.loglog(x11, y11, ls='--',color='k',linewidth=1)


plt.loglog(x5, y5, ls='--',color='k',linewidth=1)
plt.loglog(x6, y6, ls='--',color='k',linewidth=1)
plt.loglog(x7, y7, ls='--',color='k',linewidth=1)
plt.loglog(x8, y8, ls='--',color='k',linewidth=1)

plt.loglog(x1, y1, ls='--',color='r',linewidth=3)
plt.loglog(x2, y2, ls='--',color='g',linewidth=3)
plt.loglog(x3, y3, ls='--',color='b',linewidth=3)
#plt.loglog(x4, y4, ls=':',color='r',linewidth=2)
plt.loglog(x9, y9, ls=':',color='r',linewidth=2)
#plt.loglog(x10, y10, ls=':',color='r',linewidth=2)

plt.annotate(' ', xy=(0.72, 720.0),  xycoords='data',
            xytext=(0.3, 300.0), textcoords='data',
            arrowprops=dict(facecolor='r', shrink=0.01),
            horizontalalignment='right', verticalalignment='top',
            )

plt.xlabel(r"$r_1 = R / \lambda_\mathrm{D}$", size=14)
plt.ylabel(r"$r_2 = \lambda_\mathrm{D}/\ell_\mathrm{GC}$", size=14)

plt.xlim(0.005,200)
plt.ylim(0.001,1000)
plt.grid(True, which="both", ls="-")

plt.text(31.0, 1.2, r"$\lambda_\mathrm{D} = \ell_\mathrm{GC}$", size=14)
plt.text(0.6, 0.0013, r"$\lambda_\mathrm{D} = R$", rotation=90, size=14)
plt.text(0.0055, 85.0, r"$\ell_\mathrm{GC} = R$", rotation=-45, size=14)
plt.text(0.006, 0.004, r"$\lambda_\mathrm{D}^2 = \ell_\mathrm{GC} R$", rotation=45, size=14)

plt.text(0.005, 3.e-4, "strong overlap", size=14)
plt.text(20.0, 3.e-4, "no overlap", size=14)
plt.text(0.0008, 1.e-3, "low surface charge", rotation=90, size=14)
plt.text(0.0008, 12, "high surface charge", rotation=90, size=14)

plt.text(0.012, 0.7, "no co-ion", rotation=90, color='r', size=28)
plt.text(0.05, 50.0, "Gouy-Chapman", rotation=-45, color='r', size=14)
plt.text(0.035, 0.42, "ideal gas", rotation=-45, color='r', size=14)
plt.text(0.3, 0.007, "Debye-Hückel", rotation=0, color='b', size=28)
plt.text(12.5, 0.15, "thin EDLs", rotation=90, color='g', size=28)


plt.show()
