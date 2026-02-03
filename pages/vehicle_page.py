from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators_vehicle_page import LocatorsVehiclePage as LVP
from locators.locators_location_page import LocatorsLocationPage as LLP
from locators.locators_navigation_menu import LocatorsNavigationMenu as LNM
from pages.base_page import BasePage
import csv
import os

class VehiclePage(BasePage):
    vehicles_imported = []
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_vehicle_nav_menu(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.click((By.XPATH,LVP.vehicle_menu_icon ))
        self.wait_till_element_disappear((By.XPATH,LNM.spinner_icon ))
        self.element_is_displayed((By.XPATH, LVP.highlighted_vehicle_menu_icon))

    def get_vehicle_page_title(self):
        self.element_is_displayed((By.XPATH, LVP.div_page_title))
        return self.get_text((By.XPATH, LVP.div_page_title)).strip()

    def click_add_vehicle_btn(self):
        self.click((By.XPATH ,LVP.add_vehicle_btn ))

    def get_pop_up_title(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.wait_for_element_is_clickable((By.XPATH, LVP.vehicle_name_txt_bx))
        return self.get_text((By.XPATH, LVP.popup_title)).strip()

    def get_popup_element_lbl(self,element_type,element):
        text = ""
        if element_type == "input":
            text = self.get_text((By.XPATH, "//input[@name='"+element+"']//parent::div//label")).strip()
        elif element_type == "select":
            text = self.get_text((By.XPATH, "//select[@name='"+element+"']//parent::div//label")).strip()
        elif element_type == "group":
            text = self.get_text((By.XPATH, "//form//label[contains(text(),'"+element+"')]")).strip()
        return text

    def get_btn_lbl(self,element):
        self.element_is_displayed((By.XPATH, "//button[@type='"+element+"']"))
        return self.get_text((By.XPATH, "//button[@type='"+element+"']")).strip()

    def get_group_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.group_lbl))
        return self.get_text((By.XPATH, LVP.group_lbl)).strip()

    def get_vehicle_name_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.vehicle_name_lbl))
        return self.get_text((By.XPATH, LVP.vehicle_name_lbl)).strip()

    def get_vin_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.vin_lbl))
        return self.get_text((By.XPATH, LVP.vin_lbl)).strip()

    def get_location_name_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.location_name_lbl))
        return self.get_text((By.XPATH, LVP.location_name_lbl)).strip()

    def get_dia_port_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.dia_port_lbl))
        return self.get_text((By.XPATH, LVP.dia_port_lbl)).strip()

    def get_additional_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.optional_section_lbl))
        return self.get_text((By.XPATH, LVP.optional_section_lbl)).strip()

    def get_order_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.order_lbl))
        return self.get_text((By.XPATH, LVP.order_lbl)).strip()

    def get_license_state_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.license_state_lbl))
        return self.get_text((By.XPATH, LVP.license_state_lbl)).strip()

    def get_dvir_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.dvir_lbl))
        return self.get_text((By.XPATH, LVP.dvir_lbl)).strip()

    def get_license_plate_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.license_plate_lbl))
        return self.get_text((By.XPATH, LVP.license_plate_lbl)).strip()

    def get_cancel_lbl(self):
        self.element_is_displayed((By.XPATH, LLP.cancel_btn))
        return self.get_text((By.XPATH, LLP.cancel_btn)).strip()

    def get_inactive_save_btn_lbl(self):
        self.element_is_displayed((By.XPATH, LLP.inactive_save_btn))
        return self.get_text((By.XPATH, LLP.inactive_save_btn)).strip()

    def get_reset_btn_lbl(self):
        self.element_is_displayed((By.XPATH, LVP.inactive_reset_btn))
        return self.get_text((By.XPATH, LVP.inactive_reset_btn)).strip()

    def set_group(self,group):
        self.element_is_displayed((By.XPATH, LVP.group_txt_bx ))
        self.click((By.XPATH, LVP.group_txt_bx))
        self.find((By.XPATH, LVP.group_search)).send_keys(Keys.TAB)
        self.element_is_displayed((By.XPATH, "//div[@class='groups-column-wrapper']//span[contains(text(), '"+group+"')]"))
        self.click((By.XPATH, "//div[@class='groups-column-wrapper']//span[contains(text(), '"+group+"')]"))
        self.click((By.XPATH, LVP.done_btn))

    def set_vehicle_name(self, vehicle_name):
        self.element_is_displayed((By.XPATH, LVP.vehicle_name_txt_bx))
        self.type((By.XPATH, LVP.vehicle_name_txt_bx), vehicle_name)

    def set_vin(self, vin):
        self.element_is_displayed((By.XPATH, LVP.vin_txt_bx))
        self.type((By.XPATH, LVP.vin_txt_bx), vin)

    def set_location_name(self,location_name):
        self.element_is_displayed((By.XPATH, LVP.location_name_txt_bx ))
        self.click((By.XPATH, LVP.location_name_txt_bx))
        self.element_is_displayed((By.XPATH, "//ngb-highlight[contains(text(),'"+location_name+"')]"))
        self.click((By.XPATH, "//ngb-highlight[contains(text(),'"+location_name+"')]"))


    def set_diagnostic_port(self,dia):
        self.element_is_displayed((By.XPATH, LVP.dia_port_txt_bx ))
        self.click((By.XPATH, LVP.dia_port_txt_bx))
        self.element_is_displayed((By.XPATH, "//select[@name='diagnosticPort']//option[@value='"+dia+"']"))
        self.click((By.XPATH, "//select[@name='diagnosticPort']//option[@value='"+dia+"']"))

    def set_order(self,order):
        self.element_is_displayed((By.XPATH, LVP.order_txt_bx ))
        self.click((By.XPATH, LVP.order_txt_bx))
        self.element_is_displayed((By.XPATH, "//select[@name='quote_number']//option[contains(@value,'"+order+"')]"))
        self.click((By.XPATH, "//select[@name='quote_number']//option[contains(@value,'"+order+"')]"))

    def set_license_state(self,license_state):
        self.element_is_displayed((By.XPATH, LVP.license_state_txt_bx ))
        self.click((By.XPATH, LVP.license_state_txt_bx))
        self.element_is_displayed((By.XPATH, "//select[@name='licenseState']//option[contains(@value,'"+license_state+"')]"))
        self.click((By.XPATH, "//select[@name='licenseState']//option[contains(@value,'"+license_state+"')]"))

    def select_dvir(self,dvir):
        self.element_is_displayed((By.XPATH, LVP.dvir_txt_bx ))
        self.click((By.XPATH, LVP.dvir_txt_bx))
        self.element_is_displayed((By.XPATH, "//select[@name='dvir']//option[@value='"+dvir+"']"))
        self.click((By.XPATH, "//select[@name='dvir']//option[@value='"+dvir+"']"))

    def set_license_plate(self, license_plate):
        self.element_is_displayed((By.XPATH, LVP.license_plate_txt_bx))
        self.type((By.XPATH, LVP.license_plate_txt_bx), license_plate)

    def validate_vehicle_name(self):
        return self.get_text((By.XPATH, LVP.recent_vehicle_name)).strip()

    def validate_date_added(self):
        return self.get_text((By.XPATH, LVP.recent_date)).strip()

    def validate_vin(self):
        return self.get_text((By.XPATH, LVP.recent_vin)).strip()

    def validate_model(self):
        return self.get_text((By.XPATH, LVP.recent_model)).strip()

    def validate_location_name(self):
        return self.get_text((By.XPATH, LVP.recent_location_name)).strip()

    def validate_quote(self):
        return self.get_text((By.XPATH, LVP.recent_quote)).strip()

    def validate_install_status(self):
        return self.get_text((By.XPATH, LVP.recent_install_status)).strip()

    def delete_vehicle(self):
        vehicle_names = ['updated_automation_vehicle' ] +  self.vehicles_imported
        for vehicle_name in vehicle_names:
            self.click((By.XPATH, '//a[contains(text(),"'+vehicle_name+'")]//ancestor::td//preceding-sibling::td//input'))
        self.click((By.XPATH, LVP.delete_vehicle_btn))

    def click_vehicle_edit_btn(self):
        self.click((By.XPATH,LVP.recent_vehicle_edit_btn))

    def popup_heading(self):
        self.wait_till_element_disappear((By.XPATH,LNM.spinner_icon ))
        return self.get_text((By.XPATH,LVP.popup_title)).strip()

    def validate_group_edit_popup(self):
        return self.get_text((By.XPATH,LVP.group_txt)).strip()

    def validate_vehicle_name_edit_popup(self):
        return  self.get_attribute((By.XPATH, LVP.vehicle_name_txt_bx),'value').strip()

    def validate_vin_edit_popup(self):
        return  self.get_attribute((By.XPATH, LVP.vin_txt_bx),'value').strip()

    def validate_location_name_edit_popup(self):
        return  self.get_attribute((By.XPATH, LVP.location_name_txt_bx),'value').strip()

    def validate_dia_edit_popup(self):
        return  self.get_attribute((By.XPATH, LVP.dia_port_txt_bx),'value').strip()

    def validate_order_edit_popup(self):
        return  self.get_attribute((By.XPATH, LVP.order_txt_bx),'value').strip()

    def validate_license_state_edit_popup(self):
        return  self.get_attribute((By.XPATH, LVP.license_state_txt_bx),'value').strip()

    def validate_dvir_edit_popup(self):
        return  self.get_attribute((By.XPATH, LVP.dvir_txt_bx),'value').strip()

    def validate_license_plate_popup(self):
        return  self.get_attribute((By.XPATH, LVP.license_plate_txt_bx),'value').strip()

    def clear_location_name(self):
        return  self.clear((By.XPATH, LVP.location_name_txt_bx))

    def set_updated_vehicle_name(self, vehicle_name):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.element_is_displayed((By.XPATH, LVP.vehicle_name_txt_bx))
        self.type((By.XPATH, LVP.vehicle_name_txt_bx), vehicle_name)

    def clear_vehicle_name(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        return self.clear((By.XPATH, LVP.vehicle_name_txt_bx))

    def clear_vin(self):
        return self.clear((By.XPATH, LVP.vin_txt_bx))

    def clear_license_plate(self):
        return self.clear((By.XPATH, LVP.license_plate_txt_bx))

    def validate_search_result_vin(self,vin):
        records = self.find_elements((By.XPATH, LLP.table_result))
        first_record_txt = records[0].text
        return (vin in first_record_txt)

    def download_vehicle_template(self):
        self.click((By.XPATH, LVP.import_vehicle_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.wait_for_element_is_clickable((By.XPATH, LVP.download_template_btn ))
        dir_list_before_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        self.click((By.XPATH, LVP.download_template_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        dir_list_after_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        downloaded_file = set(dir_list_after_download) - set(dir_list_before_download)
        downloaded_file_name = list(downloaded_file)[0]
        return downloaded_file_name

    def create_vehicles_in_template(self, file_name, headers, vin,vehicle_data, records):
        file_path = os.path.join(os.path.expanduser('~'), 'Downloads',file_name)
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            field_names = headers
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for i in range(records):
                vehicle_name = 'Automation test import ' + self.get_random_name(10)
                self.vehicles_imported.append(vehicle_name)
                writer.writerow({headers[0] : vehicle_name,
                                 headers[1] : vin[i],
                                 headers[2] : vehicle_data[0],
                                 headers[3] : vehicle_data[1],
                                 headers[4] : vehicle_data[2],
                                 headers[5] : vehicle_data[3],
                                 headers[6] : vehicle_data[4],
                                 headers[7] : vehicle_data[5],
                                 headers[8] : vehicle_data[6]
                                 })

    def upload_template(self,file_name):
        file_path = os.path.join(os.path.expanduser('~'), 'Downloads',file_name)
        self.type((By.XPATH, LVP.import_vehicle), file_path)
        self.wait_for_element_is_clickable((By.XPATH, LVP.next_btn))
        self.click((By.XPATH, LVP.next_btn))
        self.wait_for_element_is_clickable((By.XPATH, LVP.primary_btn))
        self.click((By.XPATH, LVP.primary_btn ))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.click((By.XPATH, LVP.primary_btn))