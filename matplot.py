import matplotlib.pyplot as plt
import datetime

# 1. Create some dummy data (similar to your Sitka weather data)
dates = [
    datetime.datetime(2014, 7, 1),
    datetime.datetime(2014, 7, 2),
    datetime.datetime(2014, 7, 3),
    datetime.datetime(2014, 7, 4),
    datetime.datetime(2014, 7, 5)
]
highs = [64, 71, 64, 59, 69]

# 2. Get the list of all available styles
available_styles = plt.style.available

print(f"Found {len(available_styles)} styles. Cycling through them now...\n")
print("Press CTRL+C in your terminal to stop early.")

# 3. Loop through every style
for style_name in available_styles:
    try:
        # Use a context manager so the style only applies to this one plot
        with plt.style.context(style_name):
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Plot the data
            ax.plot(dates, highs, c='red')

            # Format the plot
            ax.set_title(f"Style: '{style_name}'", fontsize=20)
            ax.set_xlabel('', fontsize=16)
            fig.autofmt_xdate()
            ax.set_ylabel("Temperature (F)", fontsize=16)
            
            # This line fixes the 'floating' issue you asked about earlier!
            ax.margins(x=0) 
            
            # Draw the plot
            plt.draw()
            
            # Pause for 1.5 seconds so you can see it. 
            plt.pause(5)
            
            # Close the figure so we can open the next one
            plt.close(fig)
            
            print(f"Displayed: {style_name}")

    except Exception as e:
        print(f"Could not load style '{style_name}': {e}")

print("\nDone! cycled through all styles.")