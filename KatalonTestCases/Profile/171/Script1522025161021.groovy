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

WebUI.navigateToUrl('http://localhost:5000/login')

WebUI.setText(findTestObject('Page_Login  CodeFeed (2)/input_username'), 'username')

WebUI.setText(findTestObject('Page_Login  CodeFeed (2)/input_password'), 'password')

WebUI.sendKeys(findTestObject('Page_Login  CodeFeed (2)/input_password'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('Page_username  Profile Page (2)/button_Edit Profile'))

WebUI.setText(findTestObject('Page_username  Profile Page (2)/input_txtName'), '123')

WebUI.click(findTestObject('Page_username  Profile Page (2)/button_Update Profile'))

WebUI.click(findTestObject('Page_username  Profile Page (2)/button_OK'))

WebUI.verifyElementText(findTestObject('Page_username  Profile Page (2)/h2_123'), '')

WebUI.verifyElementVisible(findTestObject('Page_username  Profile Page (2)/h2_123'))

WebUI.closeBrowser()

