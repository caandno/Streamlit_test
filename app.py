import streamlit as st
from datetime import datetime, timedelta
import platform

# Define the Streamlit app
def main():
    st.title(":bread: Brød beregneren :cookie:")
    platform = platform.system()
    st.write(platform)
    

    # Get the user's input time
    input_time = st.time_input("Vælg et start tidspunkt:")

    if input_time:
        input_datetime = datetime.combine(datetime.today(), input_time)

        # Calculate times with labels
        times = [
            ("Surdej friskes opp", input_datetime + timedelta(hours=0, minutes=0),input_datetime + timedelta(hours=0, minutes=0)),
            ("Dej samles", input_datetime + timedelta(hours=18, minutes=0),input_datetime + timedelta(hours=22, minutes=0)),
            ("Sett i ovnen", input_datetime + timedelta(hours=21, minutes=0), input_datetime + timedelta(hours=26, minutes=0)),
            ("Brød ferdig", input_datetime + timedelta(hours=22, minutes=20), input_datetime + timedelta(hours=26, minutes=20)),
        ]

        st.write("#### Tider:")
        for label, time1, time2 in times:
            st.write(f"- {label}: {time1.strftime('%H:%M')} - {time2.strftime('%H:%M')}")

if __name__ == "__main__":
    main()
