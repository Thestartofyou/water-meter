import time

def read_water_meter():
    # Simulate reading the water meter (replace this with actual code for your meter)
    meter_reading = float(input("Enter current water meter reading: "))
    return meter_reading

def calculate_water_consumption(previous_reading, current_reading):
    return current_reading - previous_reading

def main():
    # Initialize the script
    previous_meter_reading = read_water_meter()

    while True:
        try:
            # Read the current water meter reading
            current_meter_reading = read_water_meter()

            # Calculate water consumption
            water_consumption = calculate_water_consumption(previous_meter_reading, current_meter_reading)

            # Display the results
            print(f"Water consumption since last check: {water_consumption:.2f} units")

            # Update the previous meter reading for the next iteration
            previous_meter_reading = current_meter_reading

            # Wait for a specified time interval (e.g., 24 hours)
            time.sleep(24 * 60 * 60)

        except KeyboardInterrupt:
            print("\nScript terminated by user.")
            break

if __name__ == "__main__":
    main()
