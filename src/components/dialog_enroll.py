import streamlit as st
from src.database.config import supabase
from src.database.db import enroll_student_to_subject
import time


@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write('Enter the Subject code to Enroll')

    join_code = st.text_input('Subject Code')

    if st.button('Enroll now ', type='primary', width='stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']

                check = supabase.table('subjects_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                if check.data:
                    st.warning("You are already Enrolled")

                else:
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success('Successfully Enrolled')
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning("Please Enter the Subject Code")