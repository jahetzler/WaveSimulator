# Import libraries
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from matplotlib.widgets import Button, Slider


#VARIABLES
#Initial values for sine function 
init_amp = 2.5 #Initial amplitude variable
init_freq = 0.01 #Initial frequency variable
init_yaxis = 10 #Initial x-axis scale variable
init_wavelen = 2

#Color of graphs
bg_col = 'black' #Plot background color
grid_col = 'white' #Grid and axis color

#Setup plot
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.set_facecolor(bg_col)

#figure 1 aesthetics:
ax1.set_facecolor(bg_col)
ax1.grid(color=grid_col, linewidth=0.4, alpha=0.3, zorder=0)
ax1.set_xlim((0,4))
ax1.set_ylim((-2,2))
ax1.spines['bottom'].set_color(grid_col)
ax1.spines['left'].set_color(grid_col)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.xaxis.label.set_color('white')
ax1.tick_params(axis='x', colors=grid_col)
ax1.tick_params(axis='y', colors=grid_col)

lambda_text_1 = ax1.text(1, 1,  ' ', fontsize=10, va='top', ha='right', color = "white", transform=ax1.transAxes)

#figure 2 aesthetics:
ax2.set_facecolor(bg_col)
ax2.grid(color=grid_col, linewidth=0.4, alpha=0.3, zorder=0)
ax2.set_xlim((0,4))
ax2.set_ylim((-2,2))
ax2.spines['bottom'].set_color(grid_col)
ax2.spines['left'].set_color(grid_col)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.xaxis.label.set_color(grid_col)
ax2.tick_params(axis='x', colors=grid_col)
ax2.tick_params(axis='y', colors=grid_col)

lambda_text_2 = ax2.text(1, -0.3,  ' ', fontsize=10, va='top', ha='right', color = "white", transform=ax1.transAxes)

#figure 3 aesthetics:
ax3.set_facecolor(bg_col)
ax3.grid(color=grid_col, linewidth=0.4, alpha=0.3, zorder=0)
ax3.set_xlim((0,4))
ax3.set_ylim((-2,2))
ax3.set_xlabel('Time [s]')
ax3.spines['bottom'].set_color(grid_col)
ax3.spines['left'].set_color(grid_col)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.xaxis.label.set_color(grid_col)
ax3.tick_params(axis='x', colors=grid_col)
ax3.tick_params(axis='y', colors=grid_col)

#Create line variable
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2)
line3, = ax3.plot([], [], lw=2)


#Initiate line function to be drawn in amation
def init():
   line1.set_data([], [])
   line2.set_data([], [])
   line3.set_data([], [])
   return line1, line2, line3

##SLIDERS
# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.2, bottom=0.2)

# Vertically oriented slider to control the amplitude in figure 1
axamp = fig.add_axes([0.05, 0.675, 0.01, 0.20])
amp_slider_1 = Slider(
    ax=axamp,
    label="Amp1",
    valmin=0,
    valmax=10,
    valinit=init_amp, #Initial amplitude variable
    orientation="vertical"
)

amp_slider_1.label.set_color("white")

# Vertically oriented slider to control the amplitude in figure 2
axamp2 = fig.add_axes([0.05, 0.45, 0.01, 0.20]) # [x, y, width, length]
amp_slider_2 = Slider(
    ax=axamp2,
    label="Amp2",
    valmin=0,
    valmax=10,
    valinit=init_amp, #Initial amplitude variable
    orientation="vertical"
)

amp_slider_2.label.set_color("white")

# Vertically oriented slider to control the frequency in figure 1
axfreq = fig.add_axes([0.1, 0.675, 0.01, 0.20])
freq_slider_1 = Slider(
    ax=axfreq,
    label="Freq 1",
    valmin=0,
    valmax=0.1,
    valinit=init_freq, #Initial amplitude variable
    orientation="vertical"
)

freq_slider_1.label.set_color("white")

# Vertically oriented slider to control the frequency in figure 2
axfreq2 = fig.add_axes([0.1, 0.45, 0.01, 0.20])
freq_slider_2 = Slider(
    ax=axfreq2,
    label="Freq 2",
    valmin=0,
    valmax=0.1,
    valinit=init_freq, #Initial amplitude variable
    orientation="vertical"
)

freq_slider_2.label.set_color("white")

# Horizontal slider to control the wavelength in figure 1
axwavelen = fig.add_axes([0.25, 0.1, 0.65, 0.02]) # [x, y, length, width]
wavelen_slider_1 = Slider(
   ax=axwavelen,
   label="Wavelength fig 1",
   valmin=0,
   valmax=4,
   valinit=init_wavelen,
   orientation="horizontal"
)

wavelen_slider_1.label.set_color("white")

# Horizontal slider to control the wavelength in figure 2
axwavelen2 = fig.add_axes([0.25, 0.05, 0.65, 0.02])
wavelen_slider_2 = Slider(
   ax=axwavelen2,
   label="Wavelength fig 2",
   valmin=0,
   valmax=4,
   valinit=init_wavelen,
   orientation="horizontal"
)

wavelen_slider_2.label.set_color("white")

# Scale y-axis in plot 3
axyaxis = fig.add_axes([0.05, 0.2, 0.01, 0.20])
yaxis_slider = Slider(
   ax=axyaxis,
   label="y-axis",
   valmin=-20,
   valmax=20,
   valinit=init_yaxis,
   orientation="vertical"
)

yaxis_slider.label.set_color("white")

##ANIMATION

#Animation function
def animate(i):

   x = np.linspace(0, 4, 1000)
   y1 = amp_slider_1.val*(np.sin(2 * np.pi *((x-freq_slider_1.val  * i) / wavelen_slider_1.val) )) #amp_slider.val takes a value from slider function on amplitude
   y2 = amp_slider_2.val*(np.sin(2 * np.pi *((x-freq_slider_2.val*1.5  * i) / wavelen_slider_2.val) )) #amp_slider.val takes a value from slider function on amplitude
   #y3 = np.sqrt(amp_slider.val **2 + amp_slider_2.val **2 + 2*amp_slider.val * amp_slider_2.val*np.cos(x*i))
   y3 = y1+y2

   #Auto adjust hight scale of y-axis with amplitude change
   #ax1.set_ylim((-(amp_slider.val+2),(amp_slider.val+2)))
   #ax2.set_ylim((-(amp_slider_2.val+2),(amp_slider_2.val+2)))

   ax1.set_ylim((-10,10))
   ax2.set_ylim((-10,10))
   ax3.set_ylim((-yaxis_slider.val,yaxis_slider.val))

   lambda_text_1.set_text('λ: {:.2f}'.format(round(wavelen_slider_1.val,2)))
   lambda_text_2.set_text('λ: {:.2f}'.format(round(wavelen_slider_2.val,2)))

   line1.set_data(x, y1)
   line2.set_data(x, y2)
   line3.set_data(x, y3)
   return line1, lambda_text_1, lambda_text_2, line2, line3

#Update sliders
# amp_slider.on_changed(animate)
# amp_slider_2.on_changed(animate)
# wavelen_slider.on_changed(animate)
# wavelen_slider_2.on_changed(animate)
# freq_slider.on_changed(animate)
# freq_slider_2.on_changed(animate)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=2000, interval=20, blit=True)
plt.show()



