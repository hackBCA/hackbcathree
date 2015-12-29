from wtforms import Form, TextField, PasswordField, SelectField, TextAreaField, validators, ValidationError

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
    ("Male", "Male"), 
    ("Female", "Female"), 
    ("NA", "Rather Not Say")
]

has_programmed_choices = [
    ("Yes", "Yes"),
    ("No", "No")
]

ethnicity_choices = [
    ("White", "White"), 
    ("African American", "African American"), 
    ("Asian or Pacific Islander", "Asian or Pacific Islander"), 
    ("American Indian or Alaskan Native", "American Indian or Alaskan Native"), 
    ("Multiracial", "Multiracial"), 
    ("Hispanic origin", "Hispanic origin"), 
    ("NA", "Rather Not Say")
]

num_hackathons_choices = [
    ("0", "0"), 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5+", "5+")
]

grade_choices = [
    ("9", "9th"), 
    ("10", "10th"), 
    ("11", "11th"), 
    ("12", "12th")
]

free_response1_prompt = "What do you hope to learn and accomplish?"
free_response2_prompt = "What is something you’re proud of (it doesn’t have to be tech related)?"
free_response3_prompt = "Is there anything else you want us to know?"

class ApplicationForm(Form):
    first_name = TextField("First Name", [
        validators.Required(message = "You must enter a first name.")
    ], description = "First Name")
    last_name = TextField("Last Name", [
        validators.Required(message = "You must enter a last name.")
    ], description = "Last Name")
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address.")
    ], description = "Email")
    school = TextField("School Name", [
        validators.Required(message = "Enter your school's name.")
    ], description = "School Name")

    gender = SelectField("Gender", choices = gender_choices, description = "Gender")
    has_programmed = SelectField("Never Programmed?", choices = has_programmed_choices, description = "Never Programmed?")
    ethnicity = SelectField("Ethnicity", choices = ethnicity_choices, description = "Ethnicity")
    grade = SelectField("Grade", choices = grade_choices, description = "Grade")
    num_hackathons = SelectField("How many hackathons have you attended?", choices = num_hackathons_choices, description = "How many hackathons have you attended?")

    github = TextField("Github Link", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Github Link (Optional)")
    linkedin = TextField("LinkedIn", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "LinkedIn Link (Optional)")
    personal_site = TextField("Personal Site", [
        validators.optional(),
        validators.URL(message = "Invalid URL.")
    ], description = "Personal Site Link (Optional)")
    other = TextField("other", [
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
