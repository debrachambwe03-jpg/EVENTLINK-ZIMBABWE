import streamlit as st

st.set_page_config(
    page_title="EventLink Zimbabwe",
    page_icon="🎉"
)

st.title("🎉 EventLink Zimbabwe")
st.subheader("Connecting event businesses with the market")

st.write(
    "A platform connecting event organisers with event service providers."
)

st.divider()

role = st.radio(
    "How are you using EventLink?",
    [
        "👤 Customer / Event Organiser",
        "🏢 Event Service Provider"
    ]
)

st.divider()

if role == "👤 Customer / Event Organiser":

    st.header("🔎 Find an Event Service")

    service = st.selectbox(
        "What are you looking for?",
        [
            "Event Venue",
            "Catering",
            "Decoration",
            "Photography",
            "Entertainment",
            "Transport",
            "Accommodation"
        ]
    )

    location = st.text_input("📍 Enter your location")

    if st.button("🔍 Search"):

        providers = {
            "Event Venue": [
                ("Great Zimbabwe Conference Centre", "Masvingo", "$100+"),
                ("Royal Event Gardens", "Masvingo", "$80+")
            ],
            "Catering": [
                ("Taste of Masvingo Catering", "Masvingo", "$120+"),
                ("Delicious Events Catering", "Masvingo", "$100+")
            ],
            "Decoration": [
                ("Elegant Events Decor", "Masvingo", "$150+"),
                ("Royal Touch Decor", "Masvingo", "$120+")
            ],
            "Photography": [
                ("Perfect Moments Photography", "Masvingo", "$80+"),
                ("Capture Zimbabwe", "Masvingo", "$100+")
            ],
            "Entertainment": [
                ("Masvingo Events DJ", "Masvingo", "$100+"),
                ("Sound & Lights Zimbabwe", "Masvingo", "$150+")
            ],
            "Transport": [
                ("EventRide Zimbabwe", "Masvingo", "$60+"),
                ("Luxury Events Transport", "Masvingo", "$100+")
            ],
            "Accommodation": [
                ("Masvingo Guest Lodge", "Masvingo", "$50+"),
                ("Great Zimbabwe Lodge", "Masvingo", "$70+")
            ]
        }

        results = providers[service]

        for name, city, price in results:

            if location.strip() == "" or location.lower() in city.lower():

                st.subheader("🏢 " + name)
                st.write("📍 Location: " + city)
                st.write("💰 Starting price: " + price)

                st.button(
                    "📋 View Provider",
                    key=name
                )

                st.divider()

    st.header("📩 Send a Booking Enquiry")

    customer_name = st.text_input("Your name")
    customer_phone = st.text_input("Phone number")
    event_date = st.date_input("Event date")
    message = st.text_area("Tell the provider about your event")

    if st.button("📤 Send Enquiry"):

        if customer_name and customer_phone and message:
            st.success(
                "Your enquiry has been sent successfully! 🎉"
            )
        else:
            st.warning(
                "Please complete your name, phone number "
                "and event details."
            )

else:

    st.header("🏢 Event Service Provider")

    st.write(
        "Register your event business so customers can discover "
        "your services on EventLink Zimbabwe."
    )

    business_name = st.text_input("Business name")
    owner_name = st.text_input("Owner / Contact person")
    business_location = st.text_input("Business location")

    business_service = st.selectbox(
        "Service you provide",
        [
            "Event Venue",
            "Catering",
            "Decoration",
            "Photography",
            "Entertainment",
            "Transport",
            "Accommodation"
        ],
        key="provider_service"
    )

    business_phone = st.text_input("Business phone number")

    if st.button("📝 Register Business"):

        if (
            business_name
            and owner_name
            and business_location
            and business_phone
        ):
            st.success(
                "Business registration submitted successfully! 🎉"
            )
        else:
            st.warning(
                "Please complete all the required information."
            )
