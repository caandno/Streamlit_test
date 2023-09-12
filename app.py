import streamlit as st
from datetime import datetime, timedelta

# Define the Streamlit app
def main():
    st.title("Bread Baking Time Calculator")

    # Get the user's input time
    input_time = st.time_input("Enter a time:")

    if input_time:
        input_datetime = datetime.combine(datetime.today(), input_time)

        # Calculate times with labels
        times = [
            ("Surdej friskes opp", input_datetime + timedelta(hours=18)),
            ("Dej samles", input_datetime + timedelta(hours=21)),
            ("Sett i ovnen", input_datetime + timedelta(hours=22, minutes=20)),
            ("Brød ferdig", input_datetime + timedelta(hours=22, minutes=20)),
        ]

        st.write("#### Times:")
        for label, time in times:
            st.write(f"- {label}: {time.strftime('%H:%M')}")

if __name__ == "__main__":
    main()
