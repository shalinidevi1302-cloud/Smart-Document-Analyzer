import re


def analyze_text(text):

    result = {}

    # Name
    name = re.search(r"Name:\s*(.*)", text)
    if name:
        result["Name"] = name.group(1).strip()

    # College
    college = re.search(r"College:\s*(.*)", text)
    if college:
        result["College"] = college.group(1).strip()

    # Course
    course = re.search(r"Course:\s*(.*)", text)
    if course:
        result["Course"] = course.group(1).strip()

    # Amount
    amount = re.search(r"Amount:\s*(.*)", text)
    if amount:
        result["Amount"] = amount.group(1).strip()

    # Date
    date = re.search(r"Date:\s*(.*)", text)
    if date:
        result["Date"] = date.group(1).strip()

    return result


def generate_summary(result):

    summary = (
        f"This document belongs to {result.get('Name', 'the user')}. "
        f"The college mentioned is {result.get('College', 'not specified')}. "
        f"The course is {result.get('Course', 'not specified')}. "
        f"The document records an amount of {result.get('Amount', 'not specified')} "
        f"and the date is {result.get('Date', 'not specified')}."
    )

    return summary