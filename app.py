import streamlit as st
from datetime import datetime, timedelta

# Function to calculate time based on input hours and minutes
def calculate_time(start_time, hours, minutes):
    start_datetime = datetime.combine(datetime.today(), start_time)
    target_time = start_datetime + timedelta(hours=hours, minutes=minutes)
    return target_time.strftime("%H:%M:%S")

def main():
    st.title("Bread Baking Timer")

    # Allow the user to pick the start time
    start_time = st.time_input("Choose a start time:", value=(datetime.now() + timedelta(minutes=10)).time())

    # Calculate times based on the selected start time and the current time
    current_time = datetime.now()
    
    times = [
        ("Surdej friskes opp", 1, 0),
        ("Dej samles", 1 0),
        ("Sett i ovnen", 1, 20),
        ("Brød ferdig", 0, 0)
    ]

    for label, hours, minutes in times:
        target_time = calculate_time(start_time, hours, minutes)
        display_time = current_time + timedelta(hours=hours, minutes=minutes)
        st.write(f"{label}: {display_time.strftime('%H:%M:%S')}")

    st.write(f"Current Time: {current_time.strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
