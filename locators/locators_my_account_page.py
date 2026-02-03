class LocatorsMyAccount:
    my_account_title_xpath = './/*[@class="account-page__title lx-section-title"]'
    # info tab
    first_name_label_xpath = '//*[@id="name-employee-id"]/lytx-input[1]/div/div[1]'
    last_name_label_xpath = '//*[@id="name-employee-id"]/lytx-input[2]/div/div[1]'
    employee_id_xpath = '//*[@id="name-employee-id"]/lytx-input[3]/div/div[1]'
    contact_information_label_xpath = '//*[@id="contactInformation"]/div/div[1]/div[1]'
    email_address_label_xpath = '//*[@id="contactInformation"]/div/div[2]/form/lytx-input/div/div[1]'
    cellphone_label_xpath = '//*[@id="#phoneNumberTitle"]'
    lytx_badge_xpath = './/*[text()="Lytx Badge"]'
    group_role_assignment_label_xpath = './/*[@class="group-roles"]/div'
    login_label_xpath = '//*[@id="loginInformation"]/div/div[1]/div[1]'
    username_label_xpath = '//*[@id="loginInformation"]/div/div[2]/form/lytx-input[1]/div/div[1]'
    password_label_xpath = '//*[@id="loginInformation"]/div/div[2]/form/lytx-input[2]/div/div[1]'
    edit_email_button_xpath = '//*[@id="contactInformation"]/div/div[1]/div[2]/div'
    email_address_textbox_xpath = '//*[@id="contactInformation"]/div/div[2]/form/lytx-input/div/div[2]/input'
    updated_email_address_text = '//*[text()=" Email Address "]/following-sibling::div'
    save_button_xpath = '//*[text()=" Save "]'

    # report tab
    report_tab_xpath = '//*[contains(text(),"Report")]'
    report_subscription_text_xpath = '//*[text()="Driving Summary"]'

    # notification tab
    notification_tab_xpath = '//*[contains(text(),"Notifications")]'
    notification_subscription_text_xpath = '(//*[text()="Event Status"])[1]'
