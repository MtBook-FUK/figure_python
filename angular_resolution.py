import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib.colors as mtc

# --- RGBA Color Codes ---
def rgba(color, opacity):
    data = [["black", 0.0, 0.0, 0.0],
            ["red", 1.0, 0.0, 0.0],
            ["green", 0.0, 1.0, 0.0],
            ["blue", 0.0, 0.0, 1.0],
            ["yellow", 1.0, 1.0, 0.0],
            ["magenta", 1.0, 0.0, 1.0],
            ["cyan", 0.0, 1.0, 1.0]
            ]
    for i in range(len(data)):
        if data[i][0].lower() == color.lower():
            return data[i][1], data[i][2], data[i][3], opacity

# Figureを設定
fig = plt.figure(figsize = (5,10), 
                 dpi = 150, 
                 facecolor = mtc.to_rgb("white"), 
                 linewidth = 1.0, 
                 edgecolor = mtc.to_rgb("gray"))

 # Axesを追加
ax = fig.add_subplot(111)

# 軸の範囲を設定
ax.set_xlim(0, 10)
ax.set_ylim(-10, 10)

# 角度(theta)方向の分割数
n = 256

# 線色の設定
lc = "black"

# -pi/2 ~ pi/2 までの扇型
for i in range(2, 14, 1):
# patches.Wedgeクラスのインスタンスを作成
    w = pat.Wedge(center = (0,0),
                  r = i, 
                  theta1 = -90, theta2 = 90, 
                  facecolor = rgba(lc, 0.0),  
                  edgecolor = rgba(lc, 0.7))
    ax.add_patch(w) # Axesに円wを追加

# y_j = x/tan(pi/n*j)の直線
for j in range(1, n+1):
    x = np.linspace(0, 10, 100)
    y = x/np.tan(np.pi/n*j)
    ax.plot(x,y, 
            color = rgba(lc, 0.5))
    
ax.tick_params(labelbottom = False, 
               labelleft = False, 
               labelright = False, 
               labeltop = False)

plt.title('n(θ) = {0}'.format(n), 
          fontsize = 20)

plt.savefig('angular_resolution{0}_{1}.jpg'.format(str(n).zfill(3), lc),
            bbox_inches = 'tight')

plt.show()
