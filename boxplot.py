import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0.1, size=(100,6))
data[76:79, :] = np.ones((3,6))+0.2

print(data.shape)

plt.figure(figsize=(4,3))

# option1 specify props dictionaries
c = 'red'
plt.boxplot(data[:,:3], positions=[1,2,3], notch=True, patch_artist=True,
            boxprops=dict(facecolor=c, color=c),
            capprops=dict(color=c),
            whiskerprops=dict(color=c),
            flierprops=dict(color=c, markeredgecolor=c),
            medianprops=dict(color=c),
            )
# plt.show()

# option 2, set all colors individually
c2 = "purple"
box1 = plt.boxplot(data[:,::-2]+1, positions=[1.5,2.5,3.5], notch=True, patch_artist=True)
for item in ['boxes', 'whiskers', 'fliers', 'medians', 'caps']:
        plt.setp(box1[item], color=c2)
plt.setp(box1["boxes"], facecolor=c2)
plt.setp(box1["fliers"], markeredgecolor=c2)
            

plt.xlim(0.5,4)
plt.xticks([1,2,3], [1,2,3])
plt.show()
