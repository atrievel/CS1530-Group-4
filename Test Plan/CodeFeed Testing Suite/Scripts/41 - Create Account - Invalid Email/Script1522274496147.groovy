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

WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:5000/register')

WebUI.setText(findTestObject('Page_Register  CodeFeed/input_name'), 'test test')

WebUI.setText(findTestObject('Page_Register  CodeFeed/input_email'), 'test test')

WebUI.setText(findTestObject('Page_Register  CodeFeed/input_username'), 'test41')

WebUI.setText(findTestObject('Page_Register  CodeFeed/input_password'), '123456789')

WebUI.setText(findTestObject('Page_Register  CodeFeed/input_verify_password'), '123456789')

WebUI.click(findTestObject('Page_Register  CodeFeed/input_btn btn-lg btn-primary m'))

WebUI.delay(2)

url = WebUI.getUrl()

WebUI.verifyEqual(url, 'http://localhost:5000/register')

WebUI.closeBrowser()
