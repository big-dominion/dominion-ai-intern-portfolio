# Initialize baseline student profile variables
student_name = "Samson"
student_age = 18
student_level = "500 Level"
student_current_cgpa = 4.20  # Floating-point number for CGPA
did_student_pass_exam = True  # Boolean tracking exam status
student_score = 85  # Integer score representation

# Evaluate letter grade and pass/fail status based on score thresholds
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

# Perform basic mathematical projections
perfect_cgpa = 5.00
cgpa_gap = perfect_cgpa - student_current_cgpa  # Float subtraction
future_age = student_age + 5  # Integer addition

# Convert boolean status to a clean readable string
exam_status_text = "CLEARED" if did_student_pass_exam else "NOT CLEARED"

# Type casting: convert numbers to strings for text concatenation demonstrations
age_as_string = str(student_age)
cgpa_as_string = str(student_current_cgpa)
score_as_string = str(student_score)

# Store core records inside a basic list data structure
student_academic_record = [student_name, student_level, student_score]

# Define a uniform border length for dynamic terminal display
line_length = 70

# Terminal Report Card Display (using dynamic string multiplication and centering)
print("")
print("=" * line_length)
print(f"ACADEMIC PROFILE FOR: {student_name.upper()}".center(line_length))
print("=" * line_length)
print(f"• Student Age : {student_age} years old (Will be {future_age} in 5 years.)")
print(f"• Current Year: {student_level}")
print(f"• Entrance Exam Status: {exam_status_text}")
print("-" * line_length)
print(f"• Evaluation Score : {student_score}/100")
print(f"• Assigned Grade : {grade} ({status})")
print(f"• Current CGPA : {student_current_cgpa} / {perfect_cgpa}")
print(f"• Distance to 5.0 CGPA: {cgpa_gap:.2f} points")
print("-" * line_length)
print("--- UNDER THE HOOD DATA TYPE CHECKS ---")
print("Type Casting Concat -> Age: " + age_as_string + ", CGPA: " + cgpa_as_string + ", Score: " + score_as_string)
print(f"Compiled List Record Structure: {student_academic_record}")
print("=" * line_length)