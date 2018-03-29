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

WebUI.setText(findTestObject('Thread Testing/input_username (3)'), 'test')

WebUI.setText(findTestObject('Thread Testing/input_password (3)'), '123456789')

WebUI.click(findTestObject('Thread Testing/input_login (3)'))

WebUI.navigateToUrl('http://localhost:5000/category/?category_id=1')

WebUI.click(findTestObject('Thread Testing/button_New thread (1)'))

WebUI.setText(findTestObject('Thread Testing/input_txtTitle'), 'test test test test test test test test test test test ')

WebUI.setText(findTestObject('Thread Testing/textarea_txtBody (1)'), '1231312414')

WebUI.click(findTestObject('Thread Testing/button_Submit thread (1)'))

WebUI.verifyElementNotVisible(findTestObject('Thread Testing/div_Your new thread was create'))

WebUI.verifyElementNotVisible(findTestObject('Thread Testing/button_OK'))

WebUI.closeBrowser()

