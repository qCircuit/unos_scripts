import matplotlib.pyplot as plt

def plotForest(grid_size, trees):
    fig, ax = plt.subplots()
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_xticks(range(grid_size + 1))
    ax.set_yticks(range(grid_size + 1))
    ax.grid(True, linestyle='dotted', color='gray', linewidth=1)
    
    items = []
    while len(items) != trees:
        items.append((random.randint(0, grid_size-1), random.randint(0, grid_size-1)))
        items = list(set(items))

    for x, y in items:
        ax.add_patch(plt.Rectangle((x, y), 1, 1, facecolor='green'))
        
    plt.show()
    
    return None

plotForest(8, 4)
