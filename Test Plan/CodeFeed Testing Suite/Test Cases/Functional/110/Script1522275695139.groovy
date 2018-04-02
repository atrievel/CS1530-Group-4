import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:5000/')

WebUI.click(findTestObject('AlbertObjFolder/FunctionalFriends/a_Login (4)'))

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalFriends/input_username (4)'), 'username')

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalFriends/input_password (4)'), 'password')

WebUI.click(findTestObject('AlbertObjFolder/FunctionalFriends/input_login (4)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalFriends/a_Messages (3)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalFriends/button_Reply (1)'))

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalFriends/textarea_txtBody (1)'), 'guh')

WebUI.click(findTestObject('AlbertObjFolder/FunctionalFriends/button_Send Message (2)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalFriends/button_OK (3)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalFriends/div_To rasta at 0622 on 032820'))

WebUI.closeBrowser()

