class Locators:
    # Login page Objects

    username_textbox_id = "username"
    password_textbox_id = "password"
    login_button_id = "submitButton"

    # Dashboard page Objects

    coaching_event_xpath = "/html/body/app/shell/div/div/navigation/div[1]/div[2]/div"
    tasks_tab_xpath = "/html/body/app/shell/div/div/navigation/div[1]/div[2]/div[2]/div[2]/div[1]"
    coaching_tab_xpath = "/html/body/app/shell/div/div/div/coaching-task-card-list/task-card-list" \
                         "/div/div[2]/coaching-task-card[1]/div/div[2]/div[2]/button"

    # Coaching Page Objects
    # Share
    share_button_xpath = '//*[@id="event-player-container"]/video-player/div[2]/div[2]/div[2]'
    share_copy_xpath = '/html/body/app/shell/div/div/div/coaching-session/lx-page-container' \
                       '/div/div[4]/action-bar/div[1]/div[1]/span'
    share_close_xpath = '/html/body/ngb-modal-window/div/div/share-event/lytx-modal-shell/div' \
                        '/div[2]/div[2]/lx-copy/div/div/button'
    share_closesecound_xpath = '//*[@id="modalShellSecondaryButton"]'

    # AddRecognition

    addrecognition_button_xpath = '//*[@id="action-bar-positive-recognition"]'
    recognition_edit_xpath = '/html/body/ngb-modal-window/div/div/positive-recognition/div[1]' \
                             '/div[2]/div[1]/div[2]/div[2]'
    recognition_reason_xpath = '/html/body/ngb-modal-window/div/div/positive-recognition/div[1]' \
                               '/div[2]/div[3]/div[2]/textarea'
    recognition_complete_xpath = '/html/body/ngb-modal-window/div/div/positive-recognition' \
                                 '/div[1]/div[2]/div[3]/button'
    recognition_delete_xpath = '/html/body/ngb-modal-window/div/div/positive-recognition/div[1]' \
                               '/div[2]/div[1]/div[2]/div[3]'
    recognition_close_xpath = '//*[@id="modalShellPrimaryButton"]'

    # ContactLytx
    contacttab_xpath = "/html/body/app/shell/div/div/div/coaching-session/lx-page-container/div" \
                       "/div[4]/action-bar/div[1]/div[3]/span"
    contact_issuedropdown_xpath = "/html/body/ngb-modal-window/div/div/contact-lytx" \
                                  "/lytx-modal-shell/div/div[2]/div[2]/div/div[2]" \
                                  "/dropdown/div/div/ul/li[2]"
    contact_messagebox_xpath = "/html/body/ngb-modal-window/div/div/contact-lytx" \
                               "/lytx-modal-shell/div/div[2]/div[2]/div/div[3]/textarea"
    contact_submit_xpath = "/html/body/ngb-modal-window/div/div/contact-lytx" \
                           "/lytx-modal-shell/div/div[2]/div[3]/button[2]"
    contact_done_xpath = "/html/body/ngb-modal-window/div/div/contact-lytx/lytx-modal-shell" \
                         "/div/div[2]/div[3]/button"

    # AddEventNotes
    addeventnotestab_xpath = "//*[@id='event-notes__add']"
    addevents_textbox_xpath = "/html/body/app/shell/div/div/div/coaching-session" \
                              "/lx-page-container/div/div[5]/old-event-comments/lx-section" \
                              "/section/div[2]/lx-section-content/div/div[2]/form/textarea"
    addevents_submitbutton_xpath = '//*[@id="addEventCommentButton"]'

    # AddSessionNotes
    addsessiontab_xpath = '//*[@id="event-notes__add"]'
    addsession_textbox_xpath = "/html/body/app/shell/div/div/div/coaching-session" \
                               "/lx-page-container/div/div[5]/old-event-comments" \
                               "/lx-section/section/div[2]/lx-section-content" \
                               "/div/div[2]/form/textarea"
    addsession_submitbutton_xpath = '//*[@id="addEventCommentButton"]'

    # CompleteSession
    completesession_xpath = '//*[@id="coaching-session-complete-button"]'
    completesession_save_xpath = '/html/body/ngb-modal-window/div/div' \
                                 '/coaching-session-confirmation/lytx-modal-shell' \
                                 '/div/div[2]/div[3]/button[2]'
    completesession_close_xpath = '/html/body/ngb-modal-window/div/div' \
                                  '/coaching-session-confirmation/lytx-modal-shell' \
                                  '/div/div[2]/div[3]/button[1]'
