#!/usr/bin/env python3
"""
Simple Assignment Tracker for managing schoolwork
"""
import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class AssignmentTracker:
    def __init__(self, data_file: str = "assignments.json"):
        self.data_file = data_file
        self.assignments: List[Dict] = []
        self.load_assignments()

    def load_assignments(self):
        """Load assignments from JSON file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.assignments = json.load(f)
        else:
            self.assignments = []

    def save_assignments(self):
        """Save assignments to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.assignments, f, indent=2)

    def add_assignment(self, title: str, course: str, due_date: str,
                      description: str = "", priority: str = "medium"):
        """Add a new assignment"""
        assignment = {
            "id": len(self.assignments) + 1,
            "title": title,
            "course": course,
            "due_date": due_date,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.assignments.append(assignment)
        self.save_assignments()
        print(f"✓ Added assignment: {title}")
        return assignment

    def list_assignments(self, show_completed: bool = False,
                        course_filter: Optional[str] = None):
        """List all assignments with optional filters"""
        filtered = self.assignments

        if not show_completed:
            filtered = [a for a in filtered if not a["completed"]]

        if course_filter:
            filtered = [a for a in filtered if a["course"].lower() == course_filter.lower()]

        if not filtered:
            print("No assignments found.")
            return

        print("\n" + "="*80)
        print(f"{'ID':<4} {'Course':<15} {'Title':<25} {'Due Date':<12} {'Priority':<10} {'Status':<10}")
        print("="*80)

        for assignment in filtered:
            status = "✓ Done" if assignment["completed"] else "Pending"
            priority_indicator = {
                "high": "🔴",
                "medium": "🟡",
                "low": "🟢"
            }.get(assignment["priority"], "⚪")

            print(f"{assignment['id']:<4} "
                  f"{assignment['course']:<15} "
                  f"{assignment['title'][:24]:<25} "
                  f"{assignment['due_date']:<12} "
                  f"{priority_indicator} {assignment['priority']:<8} "
                  f"{status:<10}")

        print("="*80 + "\n")

    def mark_complete(self, assignment_id: int):
        """Mark an assignment as completed"""
        for assignment in self.assignments:
            if assignment["id"] == assignment_id:
                assignment["completed"] = True
                assignment["completed_at"] = datetime.now().isoformat()
                self.save_assignments()
                print(f"✓ Marked assignment '{assignment['title']}' as complete!")
                return True
        print(f"✗ Assignment with ID {assignment_id} not found.")
        return False

    def delete_assignment(self, assignment_id: int):
        """Delete an assignment"""
        for i, assignment in enumerate(self.assignments):
            if assignment["id"] == assignment_id:
                deleted = self.assignments.pop(i)
                self.save_assignments()
                print(f"✓ Deleted assignment: {deleted['title']}")
                return True
        print(f"✗ Assignment with ID {assignment_id} not found.")
        return False

    def get_statistics(self):
        """Display assignment statistics"""
        total = len(self.assignments)
        completed = sum(1 for a in self.assignments if a["completed"])
        pending = total - completed

        courses = {}
        for assignment in self.assignments:
            course = assignment["course"]
            if course not in courses:
                courses[course] = {"total": 0, "completed": 0}
            courses[course]["total"] += 1
            if assignment["completed"]:
                courses[course]["completed"] += 1

        print("\n" + "="*50)
        print("ASSIGNMENT STATISTICS")
        print("="*50)
        print(f"Total Assignments: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")

        if completed > 0:
            completion_rate = (completed / total) * 100
            print(f"Completion Rate: {completion_rate:.1f}%")

        print("\nBy Course:")
        for course, stats in courses.items():
            print(f"  {course}: {stats['completed']}/{stats['total']} completed")
        print("="*50 + "\n")


def print_help():
    """Print help information"""
    help_text = """
Assignment Tracker - Manage your schoolwork

Commands:
  add       Add a new assignment
  list      List all pending assignments
  all       List all assignments (including completed)
  complete  Mark an assignment as complete
  delete    Delete an assignment
  stats     Show assignment statistics
  help      Show this help message
  exit      Exit the application

Examples:
  add "Math Homework" "MATH101" "2026-01-20" "Chapter 5 problems"
  complete 1
  delete 2
  list
"""
    print(help_text)


def main():
    """Main interactive loop"""
    tracker = AssignmentTracker()

    print("="*50)
    print("  Welcome to Assignment Tracker!")
    print("="*50)
    print("Type 'help' for available commands\n")

    while True:
        try:
            command = input(">> ").strip().lower()

            if not command:
                continue

            if command == "exit":
                print("Goodbye!")
                break

            elif command == "help":
                print_help()

            elif command == "add":
                title = input("Assignment title: ").strip()
                course = input("Course name: ").strip()
                due_date = input("Due date (YYYY-MM-DD): ").strip()
                description = input("Description (optional): ").strip()
                priority = input("Priority (high/medium/low) [medium]: ").strip() or "medium"

                tracker.add_assignment(title, course, due_date, description, priority)

            elif command == "list":
                tracker.list_assignments(show_completed=False)

            elif command == "all":
                tracker.list_assignments(show_completed=True)

            elif command == "complete":
                assignment_id = int(input("Assignment ID to mark complete: "))
                tracker.mark_complete(assignment_id)

            elif command == "delete":
                assignment_id = int(input("Assignment ID to delete: "))
                tracker.delete_assignment(assignment_id)

            elif command == "stats":
                tracker.get_statistics()

            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
