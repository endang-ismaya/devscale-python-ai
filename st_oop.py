import streamlit as st


from libs.library import Library, Member

st.title("Library Management System")

page = st.sidebar.selectbox(label="Menu", options=["Add Member", "Manage Membership"])

# checking state
if "library" not in st.session_state:
    st.session_state["library"] = Library("My Library")


# create Lib object
library = st.session_state["library"]


if page == "Add Member":
    st.header("Add Member")

    name = st.text_input("Name")

    btn_add = st.button("Add Member", type="primary")

    if btn_add:
        new_member = Member(name)
        library.register_member(new_member)
        st.rerun()

elif page == "Manage Membership":
    st.header("Manage Membership")


df = library.get_members_df()
st.dataframe(df)
