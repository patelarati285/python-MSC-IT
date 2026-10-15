from datetime import datetime


class Course:
    def __init__(self, course_code, day, start_time, end_time):
        self.course_code = course_code
        self.day = day.strip().capitalize()

        # Validate time format: HH:MM (24-hour format)
        try:
            self.start_time = datetime.strptime(
                start_time.strip(), "%H:%M"
            ).time()
            self.end_time = datetime.strptime(
                end_time.strip(), "%H:%M"
            ).time()
        except ValueError:
            raise ValueError(
                "Invalid time! Enter time in HH:MM format."
            )

        if self.start_time >= self.end_time:
            raise ValueError(
                "End time must be later than start time."
            )

    def __str__(self):
        return (
            f"{self.course_code} | {self.day} | "
            f"{self.start_time.strftime('%H:%M')} - "
            f"{self.end_time.strftime('%H:%M')}"
        )


class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.registered_courses = []

    def register_course(self, course):
        self.registered_courses.append(course)

    def detect_conflicts(self):
        conflicts = []
        courses = self.registered_courses

        for i in range(len(courses)):
            for j in range(i + 1, len(courses)):
                course1 = courses[i]
                course2 = courses[j]

                # Courses must occur on the same day.
                if course1.day.lower() == course2.day.lower():
                    # Overlap exists if each course starts
                    # before the other course ends.
                    if (
                        course1.start_time < course2.end_time
                        and course2.start_time < course1.end_time
                    ):
                        conflicts.append((course1, course2))

        return conflicts

    def __str__(self):
        return (
            f"Student ID: {self.student_id}\n"
            f"Student Name: {self.student_name}\n"
            f"Total Registered Courses: "
            f"{len(self.registered_courses)}"
        )

    def display_timetable(self):
        print("\nTimetable:")
        if not self.registered_courses:
            print("No courses registered.")
            return

        # Display courses in day and start-time order.
        day_order = {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 7,
        }

        sorted_courses = sorted(
            self.registered_courses,
            key=lambda c: (
                day_order.get(c.day, 8),
                c.start_time,
            ),
        )

        for course in sorted_courses:
            print(course)


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input! Enter a whole number.")


def main():
    students = []

    n = get_positive_integer("Enter number of students: ")

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")

        student_id = input("Enter Student ID: ").strip()
        student_name = input("Enter Student Name: ").strip()

        student = Student(student_id, student_name)

        number_of_courses = get_positive_integer(
            "Enter number of registered courses: "
        )

        for j in range(number_of_courses):
            print(f"\nCourse {j + 1}")

            while True:
                try:
                    course_code = input("Enter Course Code: ").strip()
                    if not course_code:
                        raise ValueError("Course code cannot be empty.")

                    day = input("Enter Day of Week: ").strip()
                    valid_days = {
                        "monday", "tuesday", "wednesday",
                        "thursday", "friday", "saturday", "sunday"
                    }

                    if day.lower() not in valid_days:
                        raise ValueError("Enter a valid day of the week.")

                    start_time = input(
                        "Enter Start Time (HH:MM): "
                    )
                    end_time = input(
                        "Enter End Time (HH:MM): "
                    )

                    course = Course(
                        course_code,
                        day,
                        start_time,
                        end_time,
                    )

                    student.register_course(course)
                    break

                except ValueError as error:
                    print(f"Error: {error}")
                    print("Please enter the course details again.")

        students.append(student)

    # Display student details and analyze timetable.
    print("\n========== REGISTRATION REPORT ==========")

    for student in students:
        print("\n" + "=" * 40)
        print(student)

        conflicts = student.detect_conflicts()

        if conflicts:
            print("\nTimetable Conflicts Detected:")
            for course1, course2 in conflicts:
                print(f"  {course1.course_code} conflicts with "
                      f"{course2.course_code}")
                print(f"    {course1}")
                print(f"    {course2}")
        else:
            print("\nNo timetable conflicts found.")
            student.display_timetable()

    print("\n========== REPORT COMPLETE ==========")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram terminated by user.")