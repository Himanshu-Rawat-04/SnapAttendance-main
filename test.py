from src.database.config import supabase

student_id = 2
subject_id = 1

try:
    response = supabase.table('subjects_students') \
        .insert({
            'student_id': student_id,
            'subject_id': subject_id
        }) \
        .execute()

    print("INSERT SUCCESS:")
    print(response.data)

except Exception as e:
    print("INSERT FAILED:")
    print(type(e).__name__)
    print(e)