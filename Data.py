## This file contains all the data required for the scripts to run.
## Please make necessary changes to this file as needed.

class credentials:
    username = "Admin"
    password = "admin123"
    ## Invalid password
    invalid_password = "invalid_password"

    ## Employee Information
    first_name = "Kumar"
    last_name = "Mani"


class element:
    ## Relative path for Username input box
    username_input_box_path = "//input[@placeholder='Username']"

    ## Relative path for Username input box
    password_input_box_path = "//input[@placeholder='Password']"

    ## Relative path for Login button
    login_button_path = "//button[@type='submit']"

    ## Relative path for Dashboard text
    Dashboard_text_path = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']]"

    ## Invalid credentials text
    invalid_credentials_path = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"


    ## Menu Options (It's all relative!)
    admin_menu_path = "//li[1]//a[1]//span[1]"
    pim_menu_path = "//span[normalize-space()='PIM']"
    leave_menu_path = "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[3]/a[1]/span[1]"
    time_menu_path = "//span[normalize-space()='Time']"
    recruitment_menu_path = "//span[normalize-space()='Recruitment']"
    myinfo_menu_path = "//span[normalize-space()='My Info']"
    performance_menu_path = "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[7]/a[1]/span[1]"
    dashboard_menu_path = "//span[normalize-space()='Dashboard']"
    directory_menu_path = "//span[normalize-space()='Directory']"
    maintenance_menu_path = "//span[normalize-space()='Maintenance']"
    buzz_menu_path = "//span[normalize-space()='Buzz']"

    search_box_path = "//input[@placeholder='Search']"

    user_management_path = "//span[normalize-space()='User Management']"
    users_path = "//ul[@class='oxd-dropdown-menu']//li"
    user_role_select_path = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
    user_role_admin_path = "//div[@class='oxd-select-text-input'][normalize-space()='Admin']"

    create_login_details_toggle_path = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    enabled_radio_button_path = "//input[@value='1']"

    username_text_box_path = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]"
    password_text_box_path = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]"
    confirm_password_path = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/input[1]"

    personal_details = "//h6[normalize-space()='Personal Details']"

    personal_details_menu = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]"
    contact_details_menu = "//a[normalize-space()='Contact Details']"
    emergency_contacts_menu = "//a[normalize-space()='Emergency Contacts']"
    dependents_menu = "//a[normalize-space()='Dependents']"
    immigration_menu = "//a[normalize-space()='Immigration']"
    job_menu = "//a[normalize-space()='Job']"
    salary_menu = "//a[normalize-space()='Salary']"
    tax_excemptions_menu = "//a[normalize-space()='Tax Exemptions']"
    report_to_menu = "//a[normalize-space()='Report-to']"
    qualifications_menu = "//a[normalize-space()='Qualifications']"
    memberships_menu = "//a[normalize-space()='Memberships']"