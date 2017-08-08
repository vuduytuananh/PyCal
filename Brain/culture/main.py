from PyCal.Memory.data_factory import DataFactory
import math
class IF_3_1:
	def __init__(self):
		self.__data_factory = DataFactory()
		self.__data_type = "DataTab"
	def getScore(self, fid):
		result = {}
		eg_3_1 = "EG_3_1"
		fl = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
		nationalities = fl["Nationality Location"].values
		result[eg_3_1] = {nationalities[0]: 100}
		return result
class IF_3_2:
	def __init__(self):
		self.__data_type = "DataTab"
		self.__data_factory = DataFactory()
	def __pil_duration(self, fid, consultancyOrNot):
		fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID":[], "Location": [], "Industry/Domain":[], "Duration": []})
		#consultancyOrNot
		"""
		1. Check the INDUSTRY (Sub-Domain) column (Job tab)
		"""
		if consultancyOrNot:
			"""
			A) If the input is "Consultancy" then
			"""
			fl_job = fl_job[fl_job["Industry/Domain"] == "Consultancy"]
		else:
			"""
			B) If the input is not "Consultancy" then
			"""
			fl_job = fl_job[fl_job["Industry/Domain"] != "Consultancy"]
		fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
		fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID": [], "Duration": [], "Location": []})
		fl_language = self.__data_factory.getTab(self.__data_type, "Language", {"FID":[fid], "Country": [], "Level": []})

		nationality_location = fl_personal["Nationality Location"].values
		# ignore the Country which is the same with nationality
		fl_assignment = fl_assignment[~fl_assignment["Location"].isin(nationality_location)]

		"""
		2. Check the LOCATION column in the Job tab
		AA) If the LOCATION (job tab) is the same as the NATIONALITY LOCATION (personal tab) then (you already have given that LOCATION the highs CULTURE score possible) so skip it
		AB) If the LOCATION (job tab) is not the same as the NATIONALITY LOCATION (personal tab) then
		"""
		diff_nationality = fl_job[~fl_job["Location"].isin(nationality_location)]#
		diff_nationality_grouped = diff_nationality.groupby("Location")["Duration"]
		diff_nationality_out = {k: math.fsum(list(v)) for k,v in diff_nationality_grouped}
		"""
		3. Use the next formula to calculate the duration (months):
		DURATION (months) related to the specific LOCATION (Job tab)
		"""
		diff_nationality_jid = diff_nationality["JID"].values
		diff_nationality_location = diff_nationality["Location"].values
		jid_location = dict(zip(diff_nationality_jid, diff_nationality_location))

		"""
		-(minus)- the sum of DURATIONS (months) related to the ASSIGNMENTS of the same Job ID
		which have LOCATION (assignment tab) different from the LOCATION in the job tab.
		"""
		jid_diff_nationality_duration = {}
		for i in jid_location:
			df = fl_assignment[(fl_assignment["JID"] == i) & (fl_assignment["Location"] != jid_location[i])] #LOCATION (assignment tab) different from the LOCATION in the job tab.
			total = math.fsum(df["Duration"].values)
			if i in jid_diff_nationality_duration:
				jid_diff_nationality_duration[i] += total
			else:
				jid_diff_nationality_duration[i] = total
		for i in jid_diff_nationality_duration:
			location = jid_location[i]
			diff_nationality_out[location] -= jid_diff_nationality_duration[i]
		"""
		4. then go to assignment tab and work only with Assignments related to that specific Job ID
		5. sum up only the DURATION (months) related to each particular LOCATION (Assignment tab) which is different from the LOCATION in the job tab
		"""
		adf = fl_assignment[fl_assignment["JID"].isin(diff_nationality_jid)][~fl_assignment["Location"].isin(diff_nationality_location)]
		adf_grouped = adf.groupby("Location")["Duration"]
		temp = {k: math.fsum(list(v)) for k, v in adf_grouped}
		result = {**diff_nationality_out, **temp}
		return result
	"""
	STEP 1 - (PROJECT -/LINE/INTERIM)
	"""
	def __step1(self, fid):
		"""
		6. Sum all the obtained DURATIONS (months) related to each LOCATION and multiply them by the factor x 0.4 (zero point four)
		"""
		consultancy = self.__pil_duration(fid, True)
		for i in consultancy:
			consultancy[i] *= 0.4
		"""
		6. Sum all the obtained DURATIONS(months) related to each LOCATION and multiply them by the factor x 1 (one)
		"""
		notConsultancy = self.__pil_duration(fid, False)
		return {k: consultancy.get(k, 0) + notConsultancy.get(k, 0) for k in set(consultancy) | set(notConsultancy)}
	"""
	STEP 2 (INTERIM)
	"""
	def __step2(self, fid):
		fl_job = self.__data_factory.getTab(self.__data_type, "Job", {"FID": [fid], "JID": [], "Self Employed":[]})
		fl_assignment = self.__data_factory.getTab(self.__data_type, "Assignment", {"FID": [fid], "JID":[], "Location": [], "Interim Position": [], "Duration": []})
		fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
		nationality_location = fl_personal["Nationality Location"].values
		"""
		1. Check the SELF EMPLOYED column (Job tab)
		A) if the input is "yes" then
		"""
		fl_job_se = fl_job[fl_job["Self Employed"] == "yes"]
		fl_job_se_jid = fl_job_se["JID"].values
		"""
		2. Check the INTERIM POSITION column (Assignment tab) related to that specific JOB ID
		"""
		fl_assignment_jid = fl_assignment[fl_assignment["JID"].isin(fl_job_se_jid)]
		"""
		AA) If the input is "yes" then
		3. Check the LOCATION (Assignment tab) related to that specific JOB ID
		"""
		fl_assignment_jid_ip = fl_assignment_jid[fl_assignment_jid["Interim Position"] == "yes"]
		"""
		AAA) If the LOCATION is the same as the NATIONALITY LOCATION (personal tab) then you already have given that LOCATION the highest CULTURE score possible) so skip it
		AAB) If the LOCATION is not the same then
		4. Count the DURATION (months) related to each particular LOCATION (Assignment tab)
		"""
		fl_assignment_jid_ip_lc = fl_assignment_jid_ip[~fl_assignment_jid_ip["Location"].isin(nationality_location)]
		fl_assignment_grouped = fl_assignment_jid_ip_lc.groupby("Location")["Duration"]
		"""
		AB) If the input is "no" then do not count or count the DURATION as "0"
		"""
		"""
		B) If the input is "no" then do not count or count the DURATION as "0"
		"""
		return {k: math.fsum(list(v)) for k,v in fl_assignment_grouped}
	"""
	STEP 3 (EDUCATION)
	"""
	def __step3(self, fid):
		fl_education = self.__data_factory.getTab(self.__data_type, "Education", {"FID": [fid], "Location": [], "Duration": []})
		fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
		nationality_location = fl_personal["Nationality Location"].values
		#ignore same nationality_location
		"""
		1. Check the LOCATION column in the Education tab
		A) If the LOCATION (education tab) is the same as the NATIONALITY LOCATION (personal tab) then you already have given that LOCATION the highest CULTURE score possible) so skip it
		B) If the LOCATION (education tab) is not the same as the NATIONALITY LOCATION (personal tab) then
		"""
		fl_education = fl_education[~fl_education["Location"].isin(nationality_location)]
		fl_education_grouped = fl_education.groupby("Location")["Duration"]
		"""
		5. Sum all the obtained DURATIONS (months) related to each LOCATION and multiply them by the factor x  0.5 (zero point five)
		"""
		return {k: math.fsum(list(v))*0.5 for k, v in fl_education_grouped}
	"""
	STEP 4 (CERTIFICATES and TRAININGS)
	"""
	def __step4(self, fid):
		fl_training = self.__data_factory.getTab(self.__data_type, "Trainings & Certificates", {"FID": [], "Location": [], "Duration": [], "Course type": []})
		fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": []})
		"""
		For each TRAINING & CERTIFICATE ID:
		1. Check the LOCATION column in the Training & Certificate tab
		"""
		nationality_location = fl_personal["Nationality Location"].values
		"""
		A) If the LOCATION (training & certificate tab) is the same as the NATIONALITY LOCATION (personal tab) then you already have given that LOCATION the highest CULTURE score possible) so skip it
		B) If the LOCATION is not the same as the NATIONALITY LOCATION (personal tab) then
		"""
		fl_training = fl_training[~fl_training["Location"].isin(nationality_location)]
		"""
		2. Check the TRAINING COURSE TYPE column (Training & Certificates tab)
		AA) If the input is "Language course" then
		"""
		fl_training_lang_course = fl_training[fl_training["Course type"] == "Language course"]
		"""
		3. Count the DURATION (months) related to each particular LOCATION (Training & Certificate tab)
		"""
		fl_training_lang_course_grouped = fl_training_lang_course.groupby("Location")["Duration"]
		"""
		4. Sum all the obtained DURATIONS (months) related to each LOCATION and multiply them by the factor x  0.4 (zero point four)
		"""
		out_lang_course = {k: math.fsum(list(v)) * 0.4 for k,v in fl_training_lang_course_grouped}
		"""
		AB) If the input is not "Language course" then
		"""
		fl_training_not_lang_course = fl_training[fl_training["Course type"] != "Language course"]
		"""
		3. Count the DURATION (months) related to each particular LOCATION (Training & Certificate tab)
		"""
		fl_training_not_lang_course_grouped = fl_training_not_lang_course.groupby("Location")["Duration"]
		"""
		4. Sum all the obtained DURATIONS (months) related to each LOCATION and multiply them by the factor x  0.2 (zero point two)
		"""
		out_not_lang_course = {k: math.sum(list(v)) * 0.2 for k, v in fl_training_not_lang_course_grouped}

		return {k: out_lang_course.get(k,0) + out_not_lang_course.get(k,0) for k in set(out_lang_course) | set(out_not_lang_course)}

	"""
	STEP 5 (PERSONAL REASONS)
	"""
	def __step5(self, fid):
		fl_personal = self.__data_factory.getTab(self.__data_type, "Personal", {"FID": [fid], "Nationality Location": [], "Location Personal Reasons": [], "Duration For Location": []})
		nationality_location = fl_personal["Nationality Location"].values
		#ignore same nationality
		"""
		1. Check the LOCATION PERSONAL REASONS column in the Personal tab
		A) If the LOCATION PERSONAL REASONS is the same as the NATIONALITY LOCATION (personal tab) then you already have given that LOCATION the highest CULTURE score possible) so skip it
		"""
		fl_personal = fl_personal[~fl_personal["Location Personal Reasons"].isin(nationality_location)]
		"""
		B) If the LOCATION PERSONAL REASONS is not the same as the NATIONALITY LOCATION (personal tab) then
		2. Count all the obtained DURATIONS (months) related to each LOCATION PERSONAL REASONS
		"""
		fl_personal_grouped = fl_personal.groupby("Location Personal Reasons")["Duration For Location"]
		"""
		3. Sum all the obtained DURATIONS (months) related to each LOCATION and multiply them by the factor x  0.5 (zero point five)
		"""
		return {k: math.fsum(list(v))*0.5 for k,v in fl_personal_grouped}
	def getScore(self, fid):
		"""
		STEP 7 (BOOSTING FACTOR)
		"""
		def lang_boost(locations):
			"""
			A) If the specific LOCATION is the same as the COUNTRY(language tab)  then check the LANGUAGE LEVEL column (language tab)
			"""
			fl_language = self.__data_factory.getTab(self.__data_type, "Language", {"FID":[fid], "Country": [], "Level": []})
			for i in locations:
				level = fl_language[fl_language["Country"] == i]["Level"].values
				"""
				AA) If the LANGUAGE LEVEL column has an input of >=3 (grater or equal of 3) then multiply the sum of DURATIONS related to the specific LOCATION per (x2)
				"""
				if len(level) > 0:
					level = max(level)
					if level >= 3: locations[i] *= 2
			"""
			AB)  If the LANGUAGE LEVEL column has an input of < 3 (lower than 3) then don't multiply by any factor or multiply the sum of DURATIONS related to this LOCATION per (x1)
			AAB) if the specific LOCATION is not the same as the COUNTRY then don't multiply by any factor (or by x1)
			"""
			return locations
		step1 = self.__step1(fid)
		step2 = self.__step2(fid)
		step3 = self.__step3(fid)
		step4 = self.__step4(fid)
		step5 = self.__step5(fid)
		no_boost = {k: step1.get(k,0) + step5.get(k,0) + step2.get(k,0) + step3.get(k,0) + step4.get(k,0) for k in set(step1) | set(step2) | set(step3) | set(step4) | set(step5)}
		result = lang_boost(no_boost)
		return {"EG_3_2": result}

# print(IF_3_2().getScore("FL-00001"))
# print(IF_3_1().getScore("FL-00001"))
