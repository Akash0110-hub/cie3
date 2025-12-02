def student_registration(student_id, student_name, course_enrolled, academic_year):
    return (
        f"Student ID       : {student_id}\n"
        f"Student Name     : {student_name}\n"
        f"Course Enrolled  : {course_enrolled}\n"
        f"Academic Year    : {academic_year}"
    )

if __name__ == "__main__":
    # sample output values
    student_id = "0110"
    student_name = "Aakash"
    course_enrolled = "BCA"
    academic_year = "2025-26"

    print(student_registration(student_id, student_name, course_enrolled, academic_year))
