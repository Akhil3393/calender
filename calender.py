import streamlit as st
import calendar

def display_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    st.table([[weekdays[i] for i in range(7)]])
    for week in cal:
        st.table([week])

def calendar_app():
    st.title("Simple Calendar")

    today = st.date_input("Select a date", value=None)
    year, month, _ = today.timetuple()[:3]

    display_calendar(year, month)

if _name_ == "_main_":
    calendar_app()
