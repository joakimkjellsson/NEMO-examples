#
# Plot results from DW_CHANNEL config in NEMO
#
# Author: Joakim Kjellsson, GEOMAR, March 2020
#

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cmocean 

# Open data
tfile = '../EXP00/DW_CHANNEL_grid_T.nc'
dst   = xr.open_dataset(tfile)

# Plot first step
fig,axs = plt.subplots(2,2)
ax = axs.flat

dst['toce'].isel(time_counter=0,deptht=0).plot.pcolormesh(ax=ax[0],vmin=15,vmax=25,cmap=cmocean.cm.thermal)
dst['toce'].isel(deptht=0,x=40,time_counter=[0,30,50,70]).plot.line(x='y',ax=ax[1], add_legend=False) ; ax[1].set_ylim([15,25])
dst['relvor'].isel(time_counter=-1).isel(deptht=0).plot.pcolormesh(ax=ax[2],vmin=-5e-5,vmax=5e-5,cmap=cmocean.cm.curl)
dst['ke_zint'].isel(time_counter=-1).plot.pcolormesh(ax=ax[3],cmap=cmocean.cm.speed)

ax[0].set_title('Initial sfc temp.')
ax[1].set_title('Sfc. temp. y section')
ax[2].set_title('Sfc. rel. vorticity at end')
ax[3].set_title('Vert. int. of KE at end')

fig.tight_layout()
fig.savefig('dw_channel.png',dpi=300,format='png')

plt.show()

