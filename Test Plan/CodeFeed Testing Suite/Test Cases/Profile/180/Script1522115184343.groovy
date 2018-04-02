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

WebUI.click(findTestObject('AlbertObjFolder/Email/a_Login'))

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_username'), 'username')

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_password'), 'password')

WebUI.sendKeys(findTestObject('AlbertObjFolder/Email/input_password'), Keys.chord(Keys.ENTER))

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_username'), 'username')

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_password'), 'password')

WebUI.sendKeys(findTestObject('AlbertObjFolder/Email/input_password'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('AlbertObjFolder/Email/a_Click here to register and j'))

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_name'), 'fullname')

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_email'), 'email@address.com')

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_username (1)'), 'username')

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_password (1)'), 'password')

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_verify_password'), 'password')

WebUI.sendKeys(findTestObject('AlbertObjFolder/Email/input_verify_password'), Keys.chord(Keys.ENTER))

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_username'), 'username')

WebUI.setText(findTestObject('AlbertObjFolder/Email/input_password'), 'password')

WebUI.sendKeys(findTestObject('AlbertObjFolder/Email/input_password'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('AlbertObjFolder/Email/a_emailaddress.com'))

WebUI.closeBrowser()

