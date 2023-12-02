#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self):
        self._name = None  # Initializing _name as None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) < 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

# Example usage:
person = Person()
person.name = "john smith"  # Setting a valid name
print(person.name)  # Output: John Smith

person.name = "ThisIsAVeryLongNameForAPerson"  # Setting an invalid name
# Output: Name must be a string under 25 characters.

class Person:
    approved_jobs = ["Engineer", "Doctor", "Teacher", "Artist"]  # List of approved jobs

    def __init__(self):
        self._job = None  # Initializing _job as None

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

# Example usage:
person = Person()
person.job = "Engineer"  # Setting a valid job
print(person.job)  # Output: Engineer

person.job = "Manager"  # Setting an invalid job
# Output: Job must be in list of approved jobs.

