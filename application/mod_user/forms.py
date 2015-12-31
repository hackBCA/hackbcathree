from wtforms import Form, TextField, PasswordField, SelectField, TextAreaField, BooleanField, validators, ValidationError

type_account_choices = [
    ("", "Hacker or Mentor?"),
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
    type_account = SelectField("Hacker or Mentor?", choices = type_account_choices, description = "Hacker or Mentor?")

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
    beginner = SelectField("Are you a beginner?", [validators.Required(message = "You must select an option.")], choices = beginner_choices, description = "Are you a beginner?")
    ethnicity = SelectField("Ethnicity", [validators.Required(message = "You must select an option.")], choices = ethnicity_choices, description = "Ethnicity")
    grade = SelectField("Grade", [validators.Required(message = "You must select an option.")], choices = grade_choices, description = "Grade")
    num_hackathons = SelectField("How many hackathons have you attended?", [validators.Required(message = "You must select an option.")], choices = num_hackathons_choices, description = "How many hackathons have you attended?")

    github_link = TextField("Github Link", [
        validators.optional(),
        validators.Regexp("^(http|https)://", message = "Please add 'https://' or 'http://' to the beginning of the URL."),
        validators.URL(message = "Invalid URL.")
    ], description = "Github Link (Optional)")
    linkedin_link = TextField("LinkedIn", [
        validators.optional(),
        validators.Regexp("^(http|https)://", message = "Please add 'https://' or 'http://' to the beginning of the URL."),
        validators.URL(message = "Invalid URL.")
    ], description = "LinkedIn Link (Optional)")
    site_link = TextField("Personal Site", [
        validators.optional(),
        validators.Regexp("^(http|https)://", message = "Please add 'https://' or 'http://' to the beginning of the URL."),
        validators.URL(message = "Invalid URL.")
    ], description = "Personal Site Link (Optional)")
    other_link = TextField("other", [
        validators.optional(),
        validators.Regexp("^(http|https)://", message = "Please add 'https://' or 'http://' to the beginning of the URL."),
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

    mlh_terms = BooleanField("I agree to the MLH Code of Conduct",[
        validators.Required(message = "Please read and agree to the MLH Code of Conduct.")
        ], description = "I agree to the MLH Code of Conduct.", default = False)

class MentorApplicationForm(Form):
    school = TextField("Company/School Name", [
        validators.Required(message = "Enter your company/schools's name.")
    ], description = "Company/School Name")

    phone = TextField("Phone Number", [
        validators.Required(message = "Enter your preferred contact number."),
        validators.Regexp("(\+\d+-)?\d{3}-\d{3}-\d{4}", message = "Phone number must be of the form +CC-xxx-xxx-xxxx. (Country code optional)")
    ], description = "Phone Number")

    num_hackathons = SelectField("How many hackathons have you mentored at?", [validators.Required(message = "You must select an option.")], choices = num_hackathons_choices_mentor, description = "How many hackathons have you mentored at?")

    github_link = TextField("Github Link", [
        validators.optional(),
        validators.Regexp("^(http|https)://", message = "Please add 'https://' or 'http://' to the beginning of the URL."),
        validators.URL(message = "Invalid URL.")
    ], description = "Github Link (Optional)")
    linkedin_link = TextField("LinkedIn", [
        validators.optional(),
        validators.Regexp("^(http|https)://", message = "Please add 'https://' or 'http://' to the beginning of the URL."),
        validators.URL(message = "Invalid URL.")
    ], description = "LinkedIn Link (Optional)")
    site_link = TextField("Personal Site", [
        validators.optional(),
        validators.Regexp("^(http|https)://", message = "Please add 'https://' or 'http://' to the beginning of the URL."),
        validators.URL(message = "Invalid URL.")
    ], description = "Personal Site Link (Optional)")
    other_link = TextField("other", [
        validators.optional(),
        validators.Regexp("^(http|https)://", message = "Please add 'https://' or 'http://' to the beginning of the URL."),
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

    mlh_terms = BooleanField("I agree to the MLH Code of Conduct",[
        validators.Required(message = "Please read and agree to the MLH Code of Conduct.")
        ], description = "I agree to the MLH Code of Conduct.", default = False)
