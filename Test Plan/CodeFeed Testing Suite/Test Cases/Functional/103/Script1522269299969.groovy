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

WebUI.click(findTestObject('AlbertObjFolder/FunctionalProfile/a_Login (1)'))

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalProfile/input_username (1)'), 'rasta')

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalProfile/input_password (1)'), '12345678')

WebUI.click(findTestObject('AlbertObjFolder/FunctionalProfile/input_login (1)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalProfile/button_Edit Profile (1)'))

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalProfile/input_txtName (1)'), 'Rasta Rambo')

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalProfile/input_txtEmail (1)'), 'what@some.com')

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalProfile/input_txtPass1 (1)'), 'ramboman')

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalProfile/input_txtPass2 (1)'), 'ramboman')

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalProfile/textarea_txtBio'), 'hmm')

WebUI.click(findTestObject('AlbertObjFolder/FunctionalProfile/button_Update Profile (1)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalProfile/div_i  AwesomeYour profile was'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalProfile/button_OK (1)'))

WebUI.closeBrowser()

