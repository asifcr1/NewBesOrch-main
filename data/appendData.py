from data.schema import *
import data.datadict as dd

def check_duplicate( data_dict, key=None):
	if dd.data.get(data_dict):
		seen = set()
		new_list = []
		for d in dd.data.get(data_dict):
			if data_dict == "TrainingProvider":
				print(type(dd.data.get(data_dict)))
			t = tuple(sorted(d.items()))
			if t not in seen:
				seen.add(t)
				new_list.append(d)
		dd.data.get(data_dict).clear()
		for l in new_list:
			dd.data.get(data_dict).append(l)
	

def data_append(courses):
	for course in courses:
		if course.get("contactPerson"):
			for item in course.get("contactPerson"):
				data = ContactPersons(**item).dict()
				dd.data.get("ContactPersons").append(data)
			
		if course.get("support"):
			for item in course.get("support"):
				data = Period(**item).dict()
				dd.data.get("Period").append(data)
		
				data2 = Support(**item).dict()
				dd.data.get("Support").append(data2)

		if course.get("tags"):
			for item in course.get("tags"):
				data = Tags(**item).dict()
				dd.data.get("Tags").append(data)

		if course.get("runs"):
			for item in course.get("runs"):
				data = Runs(**item).dict()
				dd.data.get("Runs").append(data)
				
		if course.get("fees"):
			for item in course.get("fees"):
				data = Fees(**item).dict()
				dd.data.get("Fees").append(data)
		
		
		data = Course(**course).dict()
		dd.data.get("Course").append(data)

	check_duplicate("ContactPersons")
	check_duplicate("Period")
	# check_duplicate("Support")
	check_duplicate("Tags")
	check_duplicate("Runs")
	check_duplicate("Fees")

