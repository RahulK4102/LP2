import streamlit as st

st.header("Learn about Web Development!")

def get_Info(topic):
    if topic == "HTML":
        st.header("HTML (Hypertext Markup Language)")
        st.write("HTML is the standard markup language for creating web pages and web applications.")
        st.write("It describes the structure of a web page using markup tags.")
        st.write("HTML elements are represented by tags like <html>, <head>, <title>, <body>, <h1>, <p>, etc.")

    elif topic == "CSS":
        st.header("CSS (Cascading Style Sheets)")
        st.write("CSS is a style sheet language used for describing the presentation of a document written in HTML.")
        st.write("It describes how HTML elements are to be displayed on the screen, paper, or in other media.")
        st.write("CSS syntax consists of a set of rules that apply style properties to elements.")

    elif topic == "JavaScript":
        st.header("JavaScript")
        st.write("JavaScript is a high-level programming language that is commonly used for creating interactive effects within web browsers.")
        st.write("It allows developers to manipulate elements on a web page, handle events, and interact with the browser's Document Object Model (DOM).")
        st.write("JavaScript can be used for client-side scripting as well as server-side scripting using Node.js.")

    elif topic == "Bootstrap":
        st.header("Bootstrap")
        st.write("Bootstrap is a popular front-end framework for developing responsive and mobile-first websites.")
        st.write("It provides a collection of CSS and JavaScript components, such as grids, forms, buttons, navigation, and more.")
        st.write("Bootstrap makes it easier to design consistent and visually appealing web interfaces across different devices and screen sizes.")

    elif topic == "React":
        st.header("React")
        st.write("React is a JavaScript library for building user interfaces, developed by Facebook.")
        st.write("It allows developers to create reusable UI components and manage the state of the application efficiently.")
        st.write("React follows a component-based architecture and uses a virtual DOM for optimal performance.")

if __name__ == "__main__":
    topic = st.selectbox(
        'What do you want to learn about?',
        ("HTML", "CSS", "JavaScript", "Bootstrap", "React"),
        index=0,
    )

    col1, col2 = st.columns([1,0.1])
    with col1:
        ask = st.button("Learn")
    with col2:
        quit = st.button("Quit")
     
    if ask:
        get_Info(topic)
    if quit:
        st.write("Thank you for using the Expert system!")
