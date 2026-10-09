import streamlit as st
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
from datetime import datetime
import pandas as pd
from src.components.dialog_attendence_result import show_attendence_result

@st.dialog("Voice Attendence")
def voice_attendence_dialog(selected_subject_id):
    st.write('Record Audio of Student, Then AI will recognize the students')

    audio_data = None

    audio_data =st.audio_input("Record Class Room audio")

    if st.button('Analyze Audio', width='stretch',type='primary'):
        with st.spinner('Processing Audio Data'):
    
            enrolled_res = supabase.table('subjects_students').select('*, student(*)').eq('subject_id', selected_subject_id).execute()

            enrolled_students= enrolled_res.data

            if not enrolled_students:
                st.warning("No students are enrolled in this cource")
                return
            
            candidates_dict = {

                s['student'] ['student_id']: s['student'] ['voice_embedding']
                for s in enrolled_students if s['student'].get('voice_embedding')
            }
            
            if not candidates_dict:
                st.error('No enrolled student have voice profile registered')
                return
        
        
            audio_bytes = audio_data.read()

            detected_score = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendence_to_log = [], []
    
            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student =node['student']
                score = detected_score.get(student['student_id'], 0.0)
                is_present = bool(score>0)
                results.append({
                    "Name": student['name'],
                    "ID": student['student_id'],
                    "Source": score if is_present else "-",
                    "Status": "✅ Present" if is_present else "❌ Absent"
                })

                attendence_to_log.append({
                    'student_id':student['student_id'],
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestamp,
                    'is_present': bool(is_present)
                })
            st.session_state.voice_attendence_results = (pd.DataFrame(results), attendence_to_log)
    if st.session_state.get('voice_attendence_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendence_results
        show_attendence_result(df_results, logs)


