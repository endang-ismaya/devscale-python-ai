import pandas as pd
import streamlit as st

st.title("CSV Operation")


user_id = st.number_input("User ID", step=1)
name = st.text_input("Name")
job = st.text_input("Job")
salary = st.number_input("Salary", step=100)

col1, col2 = st.columns(2)

submit_btn = col1.button("Add Employee", type="primary")
save_btn = col2.button("Save Changes", type="primary")

csv = pd.read_csv("data1.csv")
edited_df = st.data_editor(csv)


if submit_btn:
    new_data = pd.DataFrame(
        {
            "id": [user_id],
            "name": [name],
            "job": [job],
            "salary": [salary],
        }
    )

    csv = pd.concat([csv, new_data], ignore_index=True)
    csv.to_csv("data1.csv", index=False)

    st.rerun()


if save_btn:
    edited_df.to_csv("data1.csv", index=False)
    st.rerun()

st.bar_chart(csv.set_index("name")["salary"])
