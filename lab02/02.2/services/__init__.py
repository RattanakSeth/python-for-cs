from .student import StudentService

write_a_student_to_json = StudentService().write_a_students_to_json
read_students_from_json = StudentService().read_students_from_json

__all__ = ['write_a_students_to_json', 'read_students_from_json']