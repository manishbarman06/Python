import matplotlib.pyplot as plt

hours_studies = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [50, 55, 60, 65, 70, 75, 80, 85]

plt.scatter(hours_studies, exam_scores, color="green", marker="o", label="Student Data")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Relationship between Study Time and Exam Score")
plt.legend()
plt.grid(True)
plt.show()