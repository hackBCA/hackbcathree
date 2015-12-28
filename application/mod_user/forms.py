from wtforms import Form, TextField, PasswordField, SelectField, TextAreaField, validators, ValidationError

class RegistrationForm(Form):
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address.")
    ], description = "Email")
    first_name = TextField("First Name", [
        validators.Required(message = "You must enter a first name."),
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ], description = "First Name")
    last_name = TextField("Last Name", [
        validators.Required(message = "You must enter a last name."),
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
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
    password = PasswordField("Password", [
        validators.Required(message = "You must enter a password."),
        validators.Length(min = 8, message = "Password must be at least 8 characters.")
    ], description = "Password")

class ApplicationForm(Form):
    first_name = TextField("First Name", [
        validators.Required(message = "You must enter a first name."),
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ], description = "First Name")
    last_name = TextField("Last Name", [
        validators.Required(message = "You must enter a last name."),
        validators.Regexp("[-a-zA-Z0-9_ ]+", message = "Invalid name.")
    ], description = "Last Name")
    email = TextField("Email", [
        validators.Required(message = "Enter an email."),
        validators.Email(message = "Invalid email address.")
    ], description = "Email")
    school = TextField("School Name", [
        validators.Required(message = "Enter your school's name.")
    ], description = "School Name")

    gender = SelectField("Gender", choices = [("Male","Male"), ("Female","Female"), ("NA", "Rather Not Say")], description = "Gender")
    has_programmed = SelectField("Never Programmed?", choices = [("Yes", "Yes"), ("No", "No")], description = "Never Programmed?")
    ethnicity = SelectField("Ethnicity", choices = [("White", "White"), ("African American", "African American"), ("Asian or Pacific Islander", "Asian or Pacific Islander"), ("American Indian or Alaskan Native", "American Indian or Alaskan Native"), ("Multiracial", "Multiracial"), ("Hispanic origin", "Hispanic origin"), ("NA", "Rather Not Say")], description = "Ethnicity")
    grade = SelectField("Grade", choices = [("9", "9th"), ("10", "10th"), ("11", "11th"), ("12", "12th")], description = "Grade")
    num_hackathons = SelectField("How many hackathons have you attended?", choices = [("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5+", "5+")], description = "How many hackathons have you attended?")

    github = TextField("Github", [validators.optional()], description = "Github")
    linkedin = TextField("LinkedIn", [validators.optional()], description = "LinkedIn")
    personal_site = TextField("Personal Site", [validators.optional()], description = "Personal Website")
    other = TextField("other", [validators.optional()], description = "Other")

    free_response1 = TextAreaField("What do you hope to learn and accomplish?", [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "What do you hope to learn and accomplish?")

    free_response2 = TextAreaField("What is something you’re proud of (it doesn’t have to be tech related)?", [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "What is something you’re proud of (it doesn’t have to be tech related)?")

    free_response3 = TextAreaField("Is there anything else you want us to know?", [
        validators.Required(message = "You must answer this question."),
        validators.Length(max = 500, message = "Response must be less than 500 characters long.")
    ], description = "Is there anything else you want us to know?")
