# exam_planner.py

def generate_plan(subject, days, hours_per_day):
    plan = []

    # Determine study phase
    if days <= 3:
        phase = "cram"
    elif days <= 10:
        phase = "balanced"
    else:
        phase = "learn_then_revise"

    # Create daily plan
    for day in range(1, days + 1):
        if subject == "science":
            focus = "Practice problems and formulas"
        elif subject == "business":
            focus = "Key concepts and case studies"
        elif subject == "humanities":
            focus = "Essay structures and arguments"
        elif subject == "it":
            focus = "Concepts + practice questions"
        else:
            focus = "Core topics"

        if phase == "cram":
            task = f"{focus}. No new topics."
        elif phase == "balanced":
            task = f"{focus}. Light revision."
        else:
            task = f"Learn new topics early, revise later."

        plan.append({
            "day": day,
            "hours": hours_per_day,
            "task": task
        })

    return {
        "summary": f"{days}-day exam plan",
        "plan": plan
    }
