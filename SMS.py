import tkinter as tk
from tkinter import messagebox


class Student:
    """Class representing a student with basic attributes."""

    def __init__(self, name, age, gender, address, phone, school):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.school = school


class StudentManagementApp:
    """Class representing the student management application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.students = []

        # Initialize the user interface 
        self.setup_gui()

    def setup_gui(self):
        """Setup the main menu and buttons."""
        # Create a frame to hold the menu buttons
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        # Add buttons for each operation
        tk.Button(frame, text="Add New Student", command=self.add_student, width=30, height=2).pack(pady=5)
        tk.Button(frame, text="Show All Students", command=self.show_students, width=30, height=2).pack(pady=5)
        tk.Button(frame, text="Delete Student", command=self.delete_student, width=30, height=2).pack(pady=5)
        tk.Button(frame, text="Search Student", command=self.search_student, width=30, height=2).pack(pady=5)
        tk.Button(frame, text="Exit", command=self.root.quit, width=30, height=2, bg="red", fg="white").pack(pady=5)

    def add_student(self):
        """Open a window to add a new student."""
        def save_student():
            name = entry_name.get()
            age = entry_age.get()
            gender = entry_gender.get()
            phone = entry_phone.get()
            address = entry_address.get()
            school = entry_school.get()

            if not name or not age or not gender or not phone or not address or not school:
                messagebox.showwarning("Input Error", "All fields are required.")
                return

            try:
                age = int(age)
            except ValueError:
                messagebox.showwarning("Input Error", "Age must be a number.")
                return

            student = Student(name, age, gender, address, phone, school)
            self.students.append(student)
            messagebox.showinfo("Success", f"{name} has been added.")

            # Ask the user if they want to continue adding students
            if messagebox.askyesno("Continue?", "Do you want to add another student?"):
                # Clear the entries for new input
                entry_name.delete(0, tk.END)
                entry_age.delete(0, tk.END)
                entry_gender.delete(0, tk.END)
                entry_phone.delete(0, tk.END)
                entry_address.delete(0, tk.END)
                entry_school.delete(0, tk.END)
            else:
                add_window.destroy()

        # Create a new window for adding a student
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Student")

        # Layout for the form
        labels = ["Name", "Age", "Gender", "Phone", "Address", "School"]
        entries = {}

        for label in labels:
            tk.Label(add_window, text=f"{label}:").pack(anchor="w")
            entry = tk.Entry(add_window)
            entry.pack(fill="x", padx=10, pady=5)
            entries[label.lower()] = entry

        entry_name = entries['name']
        entry_age = entries['age']
        entry_gender = entries['gender']
        entry_phone = entries['phone']
        entry_address = entries['address']
        entry_school = entries['school']

        tk.Button(add_window, text="Save", command=save_student, width=20).pack(pady=10)

    def delete_student(self):
        """Open a window to delete a student."""
        def confirm_delete():
            name = entry_name.get()
            for i, student in enumerate(self.students):
                if student.name.lower() == name.lower():
                    del self.students[i]
                    messagebox.showinfo("Success", f"Deleted student {name}")

                    # Ask the user if they want to continue deleting students
                    if messagebox.askyesno("Continue?", "Do you want to delete another student?"):
                        # Clear the entry for new input
                        entry_name.delete(0, tk.END)
                    else:
                        delete_window.destroy()
                    return
            messagebox.showwarning("Not Found", f"{name} not found")

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Student")

        tk.Label(delete_window, text="Enter the name of the student to delete:").pack(anchor="w")
        entry_name = tk.Entry(delete_window)
        entry_name.pack(fill="x", padx=10, pady=5)
        tk.Button(delete_window, text="Delete", command=confirm_delete, width=20).pack(pady=10)

    def show_students(self):
        """Display all students in a new window."""
        show_window = tk.Toplevel(self.root)
        show_window.title("List of Students")

        if not self.students:
            tk.Label(show_window, text="No students available.").pack(pady=10)
        else:
            for i, student in enumerate(self.students):
                tk.Label(show_window, text=f"Student {i+1}: {student.name}").pack(anchor="w")

    def search_student(self):
        """Open a window to search for a student."""
        def perform_search():
            name = entry_name.get()
            for student in self.students:
                if student.name.lower() == name.lower():
                    messagebox.showinfo("Student Found",
                                        f"Name: {student.name}\n"
                                        f"Age: {student.age}\n"
                                        f"Gender: {student.gender}\n"
                                        f"Phone: {student.phone}\n"
                                        f"Address: {student.address}\n"
                                        f"School: {student.school}")
                    search_window.destroy()
                    return
            messagebox.showwarning("Not Found", f"{name} not found")

        search_window = tk.Toplevel(self.root)
        search_window.title("Search Student")

        tk.Label(search_window, text="Enter the name of the student to search:").pack(anchor="w")
        entry_name = tk.Entry(search_window)
        entry_name.pack(fill="x", padx=10, pady=5)
        tk.Button(search_window, text="Search", command=perform_search, width=20).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()
