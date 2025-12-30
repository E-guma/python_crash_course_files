import matplotlib.pyplot as plt
import numpy as np

def create_cheat_sheet():
    # 1. Define the options we want to visualize
    # Map of style code to description
    linestyles = {
        '-': 'Solid',
        '--': 'Dashed',
        '-.': 'Dash-dot',
        ':': 'Dotted'
    }

    # List of common markers
    markers = [
        '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 
        's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd'
    ]
    
    # Create the figure setup
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    fig.suptitle('Matplotlib Plot Parameters Cheat Sheet', fontsize=16, weight='bold')

    # --- LEFT PANEL: LINE STYLES ---
    y_pos = 0
    for style_code, style_name in linestyles.items():
        # Plot a line for each style
        ax1.plot(
            np.linspace(0, 10, 50), 
            [y_pos] * 50, 
            linestyle=style_code, 
            color='tab:blue', 
            linewidth=3
        )
        
        # Add text label
        ax1.text(0, y_pos + 0.2, f"'{style_code}' ({style_name})", fontsize=12, fontweight='bold')
        y_pos += 1

    # Formatting Left Panel
    ax1.set_title("Line Styles (linestyle=)", fontsize=14)
    ax1.set_ylim(-1, 4)
    ax1.axis('off') # Turn off the box/axis numbers for a cleaner look

    # --- RIGHT PANEL: MARKERS ---
    # We will plot markers in a grid-like structure
    rows = 5
    cols = 4
    
    # Generate grid coordinates
    x_coords = np.tile(np.arange(cols), rows)
    y_coords = np.repeat(np.arange(rows)[::-1], cols) # Reverse y so it fills top-down

    for i, marker in enumerate(markers):
        if i >= len(x_coords): break
        
        x = x_coords[i]
        y = y_coords[i]
        
        # Plot the marker
        ax2.plot(
            x, y, 
            marker=marker, 
            color='tab:red', 
            markersize=12, 
            linestyle='None' # No line, just the marker
        )
        
        # Label the marker
        ax2.text(x, y - 0.3, f"'{marker}'", ha='center', fontsize=11, family='monospace')

    # Formatting Right Panel
    ax2.set_title("Markers (marker=)", fontsize=14)
    ax2.set_xlim(-0.5, cols - 0.5)
    ax2.set_ylim(-1, rows)
    ax2.axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make room for suptitle
    plt.show()

if __name__ == "__main__":
    create_cheat_sheet() 