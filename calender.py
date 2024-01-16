import streamlit as st
import calendar
from datetime import date

def display_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    st.table([[weekdays[i] for i in range(7)]])
    for week in cal:
        st.table([week])

def main():
    st.title("Calendar Web App")

    today = date.today()
    current_year = today.year
    current_month = today.month

    year = st.slider("Select Year", current_year - 10, current_year + 10, current_year)
    month = st.slider("Select Month", 1, 12, current_month)

    display_calendar(year, month)

if __name__ == "__main__":
    main()
