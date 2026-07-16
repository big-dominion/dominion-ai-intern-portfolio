# 1. Student Information
student_name = "Samson"
student_age = 18
student_level = "500 Level"
student_current_cgpa = 4.20 # Float
did_student_name_passed_exam = True # Boolean
student_score = 85 # Integer


# Student Grading System
if student_score >= 90:
    grade = "A"
    status = "PASS"
elif student_score >= 80:
    grade = "B"
    status = "PASS"
elif student_score >= 70:
    grade = "C"
    status = "PASS"
elif student_score >= 60:
    grade = "D"
    status = "PASS"
else: 
    grade = "F"
    status = "FAIL"

# Present and Future Math Operation
perfect_cgpa = 5.00
cgpa_gap = perfect_cgpa - student_current_cgpa # Float Math
future_age = student_age + 5 # Integer Math

# Converting boolean to a meaningful text string response
if did_student_name_passed_exam == True:
    exam_status_text = "CLEARED"
else:
    exam_status_text = "NOT CLEARED"

# Converting integers and float for a raw report sentence
age_as_string = str(student_age)
cgpa_as_string = str(student_current_cgpa)
score_as_string = str(student_score)

# Initializing The Student Record List
student_academic_record = [student_name, student_level, student_score]



# Student Report Card
print("")
print("==============================================================================")
print(f"                            ACADEMIC PROFILE: {student_name.upper()}                   ")
print("==============================================================================")

# Printing Basic details Using F-Strings
print(f"• Student Age : {student_age} years old (Will be {future_age} in 5 years time.)")
print(f"• Current Year: {student_level}")
print(f"• Entrance Exam Status: {exam_status_text}")
print("------------------------------------------------------------------------------")


# Printing Academic Performance
print(f"• Week 1 Score : {student_score}/100")
print(f"• Week 1 Grade : {grade} ({status})")
print(f"• Current CGPA : {student_current_cgpa} / {perfect_cgpa}")
print(f"• Distance to Perfect CGPA: {cgpa_gap:.2f} points")
print("------------------------------------------------------------------------------")
'''
# Printing Type Conversions and Lists to prove execution
print("--- UNDER THE HOOD DATA CHECKS ---")
print(f"Raw Concatenation (Using Type Conversion Strings): Age " + age_as_string + ", CGPA " + cgpa_as_string + ", Score " + score_as_string)
print(f"Compiled List Record: {student_academic_record}")
print("==============================================================================")
'''