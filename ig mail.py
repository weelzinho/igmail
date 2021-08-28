from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class DemoFindElementByID():
    def locate_by_id_demo(self):
        print ('abrindo o navegador')
        driver = webdriver.Chrome()
        print ('Definindo tamanho da janela')
        driver.set_window_size(624, 688)
        driver.get("https://www.instagram.com/accounts/emailsignup/")
        window_before = driver.window_handles[0]
        print (window_before)
        # abrir aba p/ ir pro temp mail
        print ('Indo até o mail TM')
        driver.execute_script("window.open('https://mail.tm/pt/', '_blank')")
        # mudar p temp mail
        print ('copiando o email')
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        print (window_after)
                                
        driver.switch_to.window(driver.window_handles[1])
        from time import sleep
        sleep(5)   
        driver.find_element_by_id('address').click()
        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.window(window_before)
        elem = driver.find_element_by_name("emailOrPhone")
        elem.clear()
        elem.send_keys(Keys.CONTROL, "v")
        from time import sleep
        sleep(3)
        from time import sleep
        sleep(2)
        name = driver.find_element_by_css_selector("input[name='fullName']")
        print('Escolhendo um nome...')
        name.send_keys("Lourena Silva Cambalhota")
        print('Escolhendo um usuário...')
        username = driver.find_element_by_css_selector("input[name='username']")
        username.click()
        driver.delete_all_cookies()
        username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[5]/div/div/div/button/span').click()
        from time import sleep
        sleep(2)
        print('Definindo uma senha...')
        password = driver.find_element_by_css_selector("input[name='password']")
        password.send_keys("123456789")
        login_button = driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        print ('Definindo a data de aniversário da conta...')
        from time import sleep
        sleep(3)
        ano = driver.find_element_by_css_selector("[title*='Ano:']")
        ano.click()
        anoo = driver.find_element_by_xpath("//option[text()='1991']")
        anoo.click()
        from time import sleep
        sleep(2)
        mes = driver.find_element_by_css_selector("[title*='Mês:']")
        mes.click()
        mess = driver.find_element_by_xpath("//option[text()='setembro']")
        mess.click()
        print('Data de aniversário inserida, avançando...')
        data = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
        data.click()
        print ('Esperando o codigo de confirmação...')
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)                   
        driver.switch_to.window(driver.window_handles[1])
        from time import sleep
        sleep(30)
        codigo = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/main/div/div[2]/ul/li/a/div')
        codigo.click()
        driver.find_element_by_xpath('td[style = "padding:10px;color:#565a5c;font-size:32px;font-weight:500;text-align:center;padding-bottom:25px;"]')
        print(text)
        driver.switch_to.window(driver.window_handles[0])
        driver.switch_to.window(window_before)
        driver.find_element_by_css_selector("input[name='email_confirmation_code']")
        elem.clear()
        elem.send_keys(Keys.CONTROL, "v")
        from time import sleep
        sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
        print('tentando avançar..')
        
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":


        findbyid = DemoFindElementByID()
        findbyid.locate_by_id_demo()
