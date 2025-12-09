import streamlit as st


st.title('Airline Data Dictionary 📖')
st.image('imgs/online.jpg', width=400)

st.write('Survey scale from 0-5 worst to best')
left, middle, right = st.columns(3, vertical_alignment='top')

#left column
with left:
    container = st.container(border=True)
    container.markdown("""
    1. age: Traveler age
    2. sex:
    - 0: Female
    - 1: Male
    3. customer_type:
    - 0: Disloyal
    - 1: Loyal
    4. type_of_travel:
    - 0: Personal
    - 1: Business
    5. class_business:
    - 0: Not business class
    - 1: Business class
    6. class_eco:
    - 0: Not economy class
    - 1: Economy class
    7. class_eco_plus:
    - 0: Not economy plus
    - 1: Economy plus
    8. satisfaction:
    - 0: Neutral or not satisfied
    - 1: Satisfied     
    """)
    
    
with middle:
    container = st.container(border=True)
    container.markdown("""
    9. flight_distance (nautical miles)   
    10. inflight_wifi_service:
     - 0-5 scale
    11. departure/arrival_
    time_convenient:
     - 0-5 scale,
    12. ease_of_online_booking:
     - 0-5 scale,
    13. gate_location:
     - 0-5 scale,
    14. food_and_drink:
     - 0-5 scale,
    15. inflight_entertainment:
     - 0-5 scale,
    16. on_board service:
     - 0-5 scale,
    17. leg_room service:
     - 0-5 scale,
    18. baggage handling:
     - 0-5 scale,             
""")

with right:
    container = st.container(border=True)
    container.markdown("""
    19. checkin_service:
     - 0-5 scale,
    20. online_boarding:
     - 0-5 scale,
    21. seat_comfort:
     - 0-5 scale,
    22. checkin_service:
     - 0-5 scale,
    23. inflight_service:
     - 0-5 scale,
    24. cleanliness:
     - 0-5 scale,
    25. dep_delay_log:
     - departure delay (log)
    26. arr_dely_log:
     - arrival delay (log)
    27. flight_dist_log:
     - distance (nautical miles log)
""")