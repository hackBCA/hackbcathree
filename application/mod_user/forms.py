from wtforms import Form, TextField, PasswordField, SelectField, TextAreaField, BooleanField, validators, ValidationError, RadioField
import re

phone_regex = "(\+\d+-?)?((\(?\d{3}\)?)|(\d{3}))-?\d{3}-?\d{4}$"

type_account_choices = [
    ("hacker", "Hacker"),
    ("mentor", "Mentor")
]

class RegistrationForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address.")
    ], description = "Email")
    first_name = TextField("First Name", [
        validators.Required(message = "You must enter a first name.")
    ], description = "First Name")
    last_name = TextField("Last Name", [
        validators.Required(message = "You must enter a last name.")
    ], description = "Last Name")
    password = PasswordField("Password", [
        validators.Required(message = "You must enter a password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "Password")
    confirm_password = PasswordField("Confirm Password", description = "Confirm Password")
    type_account = RadioField("Hacker or Mentor?", [validators.Required(message = "Please select an account type.")], choices = type_account_choices, description = "Hacker or Mentor?")

    def validate_confirm_password(form, field):
        password = form['password'].data
        if len(password) >= 8 and password != field.data:
            raise ValidationError("Passwords must match.")

class ScholarshipRegistrationForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address.")
    ], description = "Email")
    first_name = TextField("First Name", [
        validators.Required(message = "You must enter a first name.")
    ], description = "First Name")
    last_name = TextField("Last Name", [
        validators.Required(message = "You must enter a last name.")
    ], description = "Last Name")
    password = PasswordField("Password", [
        validators.Required(message = "You must enter a password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "Password")
    confirm_password = PasswordField("Confirm Password", description = "Confirm Password")

    def validate_confirm_password(form, field):
        password = form['password'].data
        if len(password) >= 8 and password != field.data:
            raise ValidationError("Passwords must match.")

class LoginForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address."
    )], description = "Email")
    password = PasswordField("Password", [], description = "Password")

class EmailForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address."
    )], description = "Email")

class RecoverForm(Form):
    password = PasswordField("Password", [
        validators.Required(message = "You must enter a password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "Password")
    confirm_password = PasswordField("Confirm Password", description = "Confirm Password")

    def validate_confirm_password(form, field):
        password = form['password'].data
        if len(password) >= 8 and password != field.data:
            raise ValidationError("Passwords must match.")

class ChangeNameForm(Form):
    firstname = TextField("First Name", [
        validators.Required(message = "You must enter a first name.")
    ], description = "First Name")
    lastname = TextField("Last Name", [
        validators.Required(message = "You must enter a last name.")
    ], description = "Last Name")

class ChangePasswordForm(Form):
    password = PasswordField("Password", [
        validators.Required(message = "You must enter your current password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "Password")

    new_password = PasswordField("New Password", [
        validators.Required(message = "You must choose a new password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "New Password")
    confirm_password = PasswordField("Confirm New Password", description = "Confirm New Password")

    def validate_confirm_password(form, field):
        password = form['new_password'].data
        if len(password) >= 8 and password != field.data:
            raise ValidationError("Passwords must match.")

gender_choices = [
    ("", "Gender"),
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other"),
    ("rns", "Rather Not Say")
]

beginner_choices = [
    ("", "Are you a beginner?"),
    ("yes", "Yes"),
    ("no", "No")
]

ethnicity_choices = [
    ("", "Ethnicity"),
    ("white", "White"),
    ("african_american", "African American"),
    ("asian_pacific", "Asian or Pacific Islander"),
    ("american_indian_alaskan_native", "American Indian or Alaskan Native"),
    ("multiracial", "Multiracial"),
    ("hispanic", "Hispanic origin"),
    ("other", "Other"),
    ("rns", "Rather Not Say")
]

num_hackathons_choices = [
    ("", "How many hackathons have you been to?"),
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5+")
]

num_hackathons_choices_mentor = [
    ("", "How many hackathons have you mentored at?"),
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5+")
]

grade_choices = [
    ("", "What grade are you in?"),
    ("9", "9th"),
    ("10", "10th"),
    ("11", "11th"),
    ("12", "12th")
]

shirt_sizes = [
    ("", "What is your shirt size?"),
    ("XS", "Extra Small"),
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
    ("XL", "Extra Large")
]

intended_major_choices = [
    ("", "What is your intended major in college?"),
    ("computer science", "Computer Science"),
    ("engineering", "Engineering"),
    ("other", "Other"),
    ("unknown", "Unknown")
]
reduced_lunch_choices = [
    ("", "Do you receive free or reduced lunch?"),
    ("yes", "Yes"),
    ("no", "No")
]
hear_about_us_choices = [
    ("", "How did you hear about us?"),
    ("c/i", "C/I"),
    ("school", "School"),
    ("other", "Other")
]

free_response1_prompt = "What do you hope to learn and accomplish at hackBCA?"
free_response2_prompt = "What is something you’re proud of (it doesn’t have to be tech related)?"
free_response3_prompt = "Is there anything else you want us to know?"

free_response1_prompt_mentor = "Please list languages/frameworks/technologies that you would like to mentor students in."
free_response2_prompt_mentor = "Would you like to run a workshop? If so, please briefly describe your ideas."

class ApplicationForm(Form):
    school = TextField("School Name", [
        validators.Required(message = "Enter your school's name.")
    ], description = "School Name")

    gender = SelectField("Gender", [validators.Required(message = "You must select an option.")], choices = gender_choices, description = "Gender")
    other_gender = TextField("Other Gender", description = "Other Gender")
    beginner = SelectField("Are you a beginner?", [validators.Required(message = "You must select an option.")], choices = beginner_choices, description = "Are you a beginner?")
    ethnicity = SelectField("Ethnicity", [validators.Required(message = "You must select an option.")], choices = ethnicity_choices, description = "Ethnicity")
    grade = SelectField("Grade", [validators.Required(message = "You must select an option.")], choices = grade_choices, description = "Grade")
    num_hackathons = SelectField("How many hackathons have you attended?", [validators.Required(message = "You must select an option.")], choices = num_hackathons_choices, description = "How many hackathons have you attended?")

    github_link = TextField("Github Link", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Github Link (Optional)")
    linkedin_link = TextField("LinkedIn", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "LinkedIn Link (Optional)")
    site_link = TextField("Personal Site", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Personal Site Link (Optional)")
    other_link = TextField("other", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Other Link (Optional)")

    free_response1 = TextAreaField(free_response1_prompt, [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "500 character maximum.")

    free_response2 = TextAreaField(free_response2_prompt, [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "500 character maximum.")

    free_response3 = TextAreaField(free_response3_prompt, [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "500 character maximum.")

    mlh_terms = BooleanField("I agree", [
        validators.Required(message = "Please read and agree to the MLH Code of Conduct.")
        ], description = "I agree to the MLH Code of Conduct.", default = False)

    def validate(self): #Man I love validators.URL
        links = ["github_link", "linkedin_link", "site_link", "other_link"]
        originalValues = {}

        for link in links: #Temporarily prefix all links with http:// if they are missing it
            attr = getattr(self, link)
            val = attr.data
            originalValues[link] = val
            if re.match("^(http|https)://", val) is None:
                val = "http://" + val
            attr.data = val
            setattr(self, link, attr)

        rv = Form.validate(self)

        for link in links: #Revert link values back to actual values
            attr = getattr(self, link)
            attr.data = originalValues[link]
            setattr(self, link, attr)

        if not rv:
            return False
        return True

    def validate_other_gender(form, field):
        if form['gender'].data == 'other' and field.data == "":
            raise ValidationError("Enter your gender.")

class ScholarshipApplicationForm(Form):
    school = TextField("School Name", [
        validators.Required(message = "Enter your school's name.")
    ], description = "School Name")

    gender = SelectField("Gender", [validators.Required(message = "You must select an option.")], choices = gender_choices, description = "Gender")
    other_gender = TextField("Other Gender", description = "Other Gender")
    beginner = SelectField("Are you a beginner?", [validators.Required(message = "You must select an option.")], choices = beginner_choices, description = "Are you a beginner?")
    ethnicity = SelectField("Ethnicity", [validators.Required(message = "You must select an option.")], choices = ethnicity_choices, description = "Ethnicity")
    grade = SelectField("Grade", [validators.Required(message = "You must select an option.")], choices = grade_choices, description = "Grade")
    num_hackathons = SelectField("How many hackathons have you attended?", [validators.Required(message = "You must select an option.")], choices = num_hackathons_choices, description = "How many hackathons have you attended?")

    github_link = TextField("Github Link", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Github Link (Optional)")
    linkedin_link = TextField("LinkedIn", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "LinkedIn Link (Optional)")
    site_link = TextField("Personal Site", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Personal Site Link (Optional)")
    other_link = TextField("other", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Other Link (Optional)")

    intended_major = SelectField("What is your intended major in college?", [validators.Required(message = "You must select an option.")], choices = intended_major_choices, description = "What is your intended major in college?")
    other_intended_major = TextField("Intended Major", description = "Intended Major")

    reduced_lunch = SelectField("Do you receive free or reduced lunch?", [validators.Required(message = "You must select an option.")], choices = reduced_lunch_choices, description = "Do you receive free or reduced lunch?")

    hear_about_us = SelectField("How did you hear about us?", [validators.Required(message = "You must select an option.")], choices = hear_about_us_choices, description = "How did you hear about us?")
    other_hear_about_us = TextField("How did you hear about us?", description = "How did you hear about us?")

    free_response1 = TextAreaField(free_response1_prompt, [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "500 character maximum.")

    free_response2 = TextAreaField(free_response2_prompt, [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "500 character maximum.")

    free_response3 = TextAreaField(free_response3_prompt, [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "500 character maximum.")

    mlh_terms = BooleanField("I agree", [
        validators.Required(message = "Please read and agree to the MLH Code of Conduct.")
        ], description = "I agree to the MLH Code of Conduct.", default = False)

    def validate(self): #Man I love validators.URL
        links = ["github_link", "linkedin_link", "site_link", "other_link"]
        originalValues = {}

        for link in links: #Temporarily prefix all links with http:// if they are missing it
            attr = getattr(self, link)
            val = attr.data
            originalValues[link] = val
            if re.match("^(http|https)://", val) is None:
                val = "http://" + val
            attr.data = val
            setattr(self, link, attr)

        rv = Form.validate(self)

        for link in links: #Revert link values back to actual values
            attr = getattr(self, link)
            attr.data = originalValues[link]
            setattr(self, link, attr)

        if not rv:
            return False
        return True

    def validate_other_gender(form, field):
        if form['gender'].data == 'other' and field.data == "":
            raise ValidationError("Enter your gender.")
    def validate_other_intended_major(form, field):
        if form['intended_major'].data == 'other' and field.data == "":
            raise ValidationError("Enter your intended major.")
    def validate_other_hear_about_us(form, field):
        if form['hear_about_us'].data == 'other' and field.data == "":
            raise ValidationError("How did you hear about us?")

class MentorApplicationForm(Form):
    school = TextField("Company/School Name", [
        validators.Required(message = "Enter your company/schools's name.")
    ], description = "Company/School Name")

    phone = TextField("Phone Number", [
        validators.Required(message = "Enter your preferred contact number."),
        validators.Regexp(phone_regex, message = "Please enter a valid phone number.")
    ], description = "Phone Number")

    num_hackathons = SelectField("How many hackathons have you mentored at?", [validators.Required(message = "You must select an option.")], choices = num_hackathons_choices_mentor, description = "How many hackathons have you mentored at?")

    github_link = TextField("Github Link", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Github Link (Optional)")
    linkedin_link = TextField("LinkedIn", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "LinkedIn Link (Optional)")
    site_link = TextField("Personal Site", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Personal Site Link (Optional)")
    other_link = TextField("other", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Other Link (Optional)")

    free_response1 = TextAreaField(free_response1_prompt_mentor, [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "500 character maximum.")

    free_response2 = TextAreaField(free_response2_prompt_mentor, [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "500 character maximum.")

    mlh_terms = BooleanField("I agree",[
        validators.Required(message = "Please read and agree to the MLH Code of Conduct.")
        ], description = "I agree to the MLH Code of Conduct.", default = False)

    def validate(self):
        links = ["github_link", "linkedin_link", "site_link", "other_link"]
        originalValues = {}

        for link in links: #Temporarily prefix all links with http:// if they are missing it
            attr = getattr(self, link)
            val = attr.data
            originalValues[link] = val
            if re.match("^(http|https)://", val) is None:
                val = "http://" + val
            attr.data = val
            setattr(self, link, attr)

        rv = Form.validate(self)

        for link in links: #Revert link values back to actual values
            attr = getattr(self, link)
            attr.data = originalValues[link]
            setattr(self, link, attr)

        if not rv:
            return False
        return True

attending_choices = [
    ("Attending", "Yes, I will!"),
    ("Not Attending", "No, I won't.")
]

class RsvpForm(Form):
    attending = RadioField("Are you attending hackBCA III?", [validators.Required(message = "Please tell us if you are attending hackBCA III.")], choices = attending_choices)

    address = TextField("Hometown and State", [validators.required("Please enter your hometown and state.")], description = "Hometown and State")

    school = TextField("Confirm your school", [validators.required("Please confirm your school.")], description = "School Confirmation")

    phone = TextField("Phone #", [
        validators.Required(message = "Enter your preferred contact number."),
        validators.Regexp(phone_regex, message = "Please enter a valid phone number.")
    ], description = "Phone #")


    t_shirt_size = SelectField("What is your shirt size?", [validators.Required(message = "You must select an option.")], choices = shirt_sizes, description = "What is your shirt size?")

    emergency_contact_name1 = TextField("Full Name", [
        validators.Required(message = "Enter the name of your first emergency contact.")
    ], description = "Emergency Contact #1 Name")

    emergency_contact_relation1 = TextField("Relationship", [
        validators.Required(message = "Enter your relationship to your emergency contact.")
    ], description = "Emergency Contact #1 Relationship")

    emergency_contact_phone1 = TextField("Phone #", [
        validators.Required(message = "Enter your emergency contact's phone number."),
        validators.Regexp(phone_regex, message = "Please enter a valid phone number.")
    ], description = "Emergency Contact #1 Phone #")

    emergency_contact_name2 = TextField("Full Name", [
        validators.Required(message = "Enter the name of your second emergency contact.")
    ], description = "Emergency Contact #2 Name")

    emergency_contact_relation2 = TextField("Relationship", [
        validators.Required(message = "Enter your relationship to your emergency contact.")
    ], description = "Emergency Contact #2 Relationship")

    emergency_contact_phone2 = TextField("Phone #", [
        validators.Required(message = "Enter your emergency contact's phone number."),
        validators.Regexp(phone_regex, message = "Please enter a valid phone number.")
    ], description = "Emergency Contact #2 Phone #")

    food_allergies = TextAreaField("Allergies", [
        validators.optional(),
    ], description = "Do you have any allergies?")

    medical_information = TextAreaField("Medical Information", [
        validators.optional(),
    ], description = "Are there any other medical issues that we should know about? (ex. Other allergies, illnesses, etc.)")

    hackbca_rules = BooleanField("I agree",[
        validators.Required(message = "Please read and agree to our rules.")
    ], description = "I agree to the rules set forth by hackBCA.", default = False)

    mlh_terms = BooleanField("I agree",[
        validators.Required(message = "Please read and agree to the MLH Code of Conduct.")
    ], description = "I agree to the MLH Code of Conduct.", default = False)

class MentorRsvpForm(Form):
    attending = RadioField("Are you attending hackBCA III?", [validators.Required(message = "Please tell us if you are attending hackBCA III.")], choices = attending_choices)

    phone = TextField("Phone Number", [
        validators.Required(message = "Confirm your preferred contact number."),
        validators.Regexp(phone_regex, message = "Please enter a valid phone number.")
    ], description = "Phone Number Confirmation")

    t_shirt_size = SelectField("What is your shirt size?", [validators.Required(message = "You must select an option.")], choices = shirt_sizes, description = "What is your shirt size?")

    food_allergies = TextAreaField("Allergies", [
        validators.optional(),
    ], description = "Do you have any allergies?")

    medical_information = TextAreaField("Medical Information", [
        validators.optional(),
    ], description = "Are there any other medical issues that we should know about? (ex. Other allergies, illnesses, etc.)")

    hackbca_rules = BooleanField("I agree",[
        validators.Required(message = "Please read and agree to our rules.")
    ], description = "I agree to the rules set forth by hackBCA.", default = False)

    mlh_terms = BooleanField("I agree",[
        validators.Required(message = "Please read and agree to the MLH Code of Conduct.")
    ], description = "I agree to the MLH Code of Conduct.", default = False)
