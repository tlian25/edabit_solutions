def grade_percentage(user_score, pass_score):
	
    user_score = int(user_score.replace("%", ""))
    pass_score = int(pass_score.replace("%", ""))

    if user_score >= pass_score:
        return "You PASSED the Exam"
    else:
        return "You FAILED the Exam"
